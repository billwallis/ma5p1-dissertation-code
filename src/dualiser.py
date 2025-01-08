"""
Points, duals, and plotting functions.
"""

from __future__ import annotations

import abc
import math
from collections.abc import Callable
from typing import Any, Literal

import matplotlib.cm
import matplotlib.pyplot as plt
import numpy as np


class Point:
    """
    A projective point in 3D space.
    """

    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float = 1.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, y={self.z})"

    @property
    def dual(self) -> tuple[tuple[float, float], tuple[float, float]]:
        """
        The line corresponding to the projective point at ``[a : b : c]`` is
        given by ``aX + bY + cZ = 0``.

        Note that this can only be re-arranged to be given in terms of ``Y``
        when ``b`` is non-zero. If ``b`` is zero, then the line will either be
        at infinity (if ``X == 0``) or a vertical line (if ``X != 0``).
        """
        if self.y == 0:
            if self.x == 0:
                return (
                    (math.inf, math.inf),
                    (math.inf, math.inf),
                )
            return (
                (-self.z / self.x, -1),
                (-self.z / self.x, 1),
            )

        m = -self.x / self.y
        c = -self.z / self.y
        return (
            (-1, -m + c),
            (1, m + c),
        )


class Points(abc.ABC):
    """
    A set of points that can be plotted.
    """

    x_lim: tuple[float, float]
    y_lim: tuple[float, float]
    aspect: Literal["equal", "auto"] = "equal"

    @abc.abstractmethod
    def plot_points(self, size: float) -> None:
        """
        Plot the points on a graph.

        :param size: The size of the points on the graph.
        """

    @abc.abstractmethod
    def plot_duals(self, width: float) -> None:
        """
        Plot the duals of the points on a graph.

        :param width: The width of the lines on the graph.
        """

    def plot(
        self,
        size: float | None = None,
        width: float | None = None,
        save: bool = False,
        path: str | None = None,
    ) -> None:
        """
        Plot the points and/or duals and display the graph.

        :param size: The size of the points on the graph. If not provided, the
            points will not be plotted.
        :param width: The width of the lines on the graph. If not provided, the
            duals will not be plotted.
        :param save: Whether to save the image to a file.
        :param path: The path to save the image to.
        """
        if not size and not width:
            raise ValueError("Either size or width must be provided to plot.")

        plt.xlim(*self.x_lim)
        plt.ylim(*self.y_lim)
        plt.gca().set_aspect(self.aspect)
        plt.axis("off")

        self.plot_points(size=size) if size else None
        self.plot_duals(width=width) if width else None

        if save:
            if not path:
                raise ValueError("Path must be provided to save the image.")
            plt.savefig(
                path,
                # bbox_inches="tight",
                bbox_inches=0,
                dpi=1080,
                format="png",
            )
            print(f"Image saved to {path}")

        plt.show()


def _plot_point(point: Point, color: str, **kwargs) -> None:
    """
    Plot the point on a matplotlib graph.
    """
    if point.z != 0:
        plt.scatter(
            point.x / point.z,
            point.y / point.z,
            color=color,
            **kwargs,
        )


def _plot_dual(point: Point, **kwargs) -> None:
    """
    Plot the dual of the point on a matplotlib graph.
    """
    plt.axline(*point.dual, **kwargs)


def _plot_rainbow(
    plotter: Callable,
    points: list[Point],
    **kwargs,
) -> None:
    """
    Plot the points on a matplotlib graph using a colour rainbow.

    Credit to the following Stack Overflow answer:

    - https://stackoverflow.com/a/33905962/8213085
    """
    colors = [matplotlib.cm.jet(x) for x in np.linspace(0.0, 1.0, len(points))]
    for i, point in enumerate(points):
        plotter(point=point, color=colors[i], **kwargs)


def plot_points(points: list[Point], color: str, **kwargs) -> None:
    """
    Plot the points on a matplotlib graph.
    """
    if color.casefold() == "rainbow":
        _plot_rainbow(plotter=_plot_point, points=points, **kwargs)
    else:
        for point in points:
            _plot_point(point=point, color=color, **kwargs)


def plot_duals(points: list[Point], color: Any, **kwargs) -> None:
    """
    Plot the dual of the points on a matplotlib graph.
    """
    if color.casefold() == "rainbow":
        _plot_rainbow(plotter=_plot_dual, points=points, **kwargs)
    else:
        for point in points:
            _plot_dual(point=point, color=color, **kwargs)
