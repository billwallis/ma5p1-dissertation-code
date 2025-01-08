"""
Define graphs with interesting duals.
"""

from __future__ import annotations

import math

import dualiser

MIN_NUMBER_OF_POINTS = 2


class SimpleTriangularGrid(dualiser.Points):
    """
    A simple triangular grid.
    """

    def __init__(self):
        """
        Define the points on a simple triangular grid.

        The points lie on three lines: ``P``, ``Q``, and ``R``.
        """
        self.x_lim = (-2, 2)
        self.y_lim = (-2, 2)

        self.p_points = [
            dualiser.Point(1, -1, 1),
            dualiser.Point(-1, 1, 0),
            dualiser.Point(-1, 1, 1),
        ]
        self.q_points = [
            dualiser.Point(1, 3, -3),
            dualiser.Point(1, 3, 0),
            dualiser.Point(1, 3, 3),
        ]
        self.r_points = [
            dualiser.Point(4, 0, 3),
            dualiser.Point(1, 0, 0),
            dualiser.Point(4, 0, -3),
        ]

    def plot_points(self, size: float) -> None:
        """
        Plot each of the points that lie on the lines ``P``, ``Q``, and ``R``.

        :param size: The size of the points on the graph.
        """
        dualiser.plot_points(self.p_points, color="r", s=size)
        dualiser.plot_points(self.q_points, color="g", s=size)
        dualiser.plot_points(self.r_points, color="b", s=size)

    def plot_duals(self, width: float) -> None:
        """
        Plot the duals of the points that lie on the lines ``P``, ``Q``, and
        ``R``.

        :param width: The width of the lines on the graph.
        """
        dualiser.plot_duals(self.p_points, color="r", linewidth=width)
        dualiser.plot_duals(self.q_points, color="g", linewidth=width)
        dualiser.plot_duals(self.r_points, color="b", linewidth=width)


class UnitCircle(dualiser.Points):
    """
    The roots of unity on a circle, with the corresponding points at infinity.
    """

    def __init__(self, roots: int):
        """
        Define the points on a unit circle.

        The points will be the roots of unity with their corresponding points at
        infinity.
        """
        self.x_lim = (-5, 5)
        self.y_lim = (-5, 5)

        self.roots_of_unity = [
            dualiser.Point(
                x=math.cos(2 * t * math.pi / roots),
                y=math.sin(2 * t * math.pi / roots),
            )
            for t in range(roots)
        ]
        self.points_at_infinity = [
            dualiser.Point(
                x=-math.sin(t * math.pi / roots),
                y=math.cos(t * math.pi / roots),
                z=0,
            )
            for t in range(roots)
        ]

    def plot_points(self, size: float) -> None:
        """
        Plot the roots of unity.

        There's no point in plotting the points at infinity, as they are
        infinitely far away!

        :param size: The size of the points on the graph.
        """
        dualiser.plot_points(self.roots_of_unity, color="black", s=size)

    def plot_duals(self, width: float) -> None:
        """
        Plot the duals of the roots of unity and their corresponding points at
        infinity.

        :param width: The width of the lines on the graph.
        """
        dualiser.plot_duals(self.roots_of_unity, color="black", linewidth=width)
        dualiser.plot_duals(
            self.points_at_infinity, color="rainbow", linewidth=width
        )


class CubicCurve(dualiser.Points):
    """
    Equally spaced points on a cubic curve, given by ``Y = X^3``.
    """

    def __init__(self, number: int):
        """
        Define the points on a cubic curve.
        """
        if number < MIN_NUMBER_OF_POINTS:
            raise ValueError(f"Must have at least 2 points, found {number}")

        self.x_lim = (-1.5, 1.5)
        self.y_lim = (-0.04, 0.04)
        self.aspect = "auto"

        lower, upper = -10, 10
        diff = upper - lower
        denominator = number - 1

        self.cubic_points = []
        for i in range(number):
            x = lower + (i * diff / denominator)
            self.cubic_points.append(dualiser.Point(x, x**3))

    def plot_points(self, size: float) -> None:
        """
        Plot the points on the cubic curve.

        :param size: The size of the points on the graph.
        """
        dualiser.plot_points(self.cubic_points, color="rainbow", s=size)

    def plot_duals(self, width: float) -> None:
        """
        Plot the duals of the points on the cubic curve.

        :param width: The width of the lines on the graph.
        """
        dualiser.plot_duals(self.cubic_points, color="rainbow", linewidth=width)

    def plot(
        self,
        size: float | None = None,
        width: float | None = None,
        save: bool = False,
        path: str | None = None,
    ) -> None:
        """
        Plot the points and/or duals and display the graph, as per the
        superclass.

        Note that the cubic curve cannot plot both the points and the duals at
        the same time.

        :raises ValueError: If both the size and width are given.
        """
        if size and width:
            raise ValueError(
                "For the cubic curve, the points and duals cannot both be printed."
            )

        super().plot(size, width, save, path)
