"""
Plot points and their duals.
"""
import abc
import math

import matplotlib.pyplot as plt

import dualiser


class Points(abc.ABC):
    """
    A set of points that can be plotted.
    """
    @abc.abstractmethod
    def plot_points(self, size: float) -> None:
        """
        Plot the points on a graph.
        """
        pass

    @abc.abstractmethod
    def plot_duals(self, width: float) -> None:
        """
        Plot the duals of the points on a graph.
        """
        pass

    @abc.abstractmethod
    def plot(self, size: float = None, width: float = None) -> None:
        """
        Plot the points and display the graph.
        """
        pass


class SimpleTriangularGrid(Points):
    """
    A simple triangular grid.
    """
    def __init__(self):
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

    def plot_points(self, size: float = 5) -> None:
        dualiser.plot_points(self.p_points, color="r", s=size)
        dualiser.plot_points(self.q_points, color="g", s=size)
        dualiser.plot_points(self.r_points, color="b", s=size)

    def plot_duals(self, width: float = 1) -> None:
        dualiser.plot_duals(self.p_points, color="r", linewidth=width)
        dualiser.plot_duals(self.q_points, color="g", linewidth=width)
        dualiser.plot_duals(self.r_points, color="b", linewidth=width)

    # noinspection DuplicatedCode
    def plot(self, size: float = None, width: float = None) -> None:
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        plt.axis("off")
        plt.gca().set_aspect("equal")

        self.plot_points(size=size) if size else None
        self.plot_duals(width=width) if width else None
        plt.show()


class UnitCircle(Points):
    """
    The roots of unity on a circle, with the corresponding points at infinity.
    """
    def __init__(self, roots: int):
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

    def plot_points(self, size: float = 5) -> None:
        dualiser.plot_points(self.roots_of_unity, color="black", s=size)
        # dualiser.plot_points(self.points_at_infinity, color="black", s=size)

    def plot_duals(self, width: float = 1) -> None:
        dualiser.plot_duals(self.roots_of_unity, color="black", linewidth=width)
        dualiser.plot_duals(self.points_at_infinity, color="rainbow", linewidth=width)

    # noinspection DuplicatedCode
    def plot(self, size: float = None, width: float = None) -> None:
        plt.xlim(-5, 5)
        plt.ylim(-5, 5)
        plt.axis("off")
        plt.gca().set_aspect("equal")

        self.plot_points(size=size) if size else None
        self.plot_duals(width=width) if width else None
        plt.show()


class CubicCurve(Points):
    """
    Equally spaced points on a cubic curve, given by ``Y = X^3``.
    """
    def __init__(self, number: int):
        if number < 2:
            raise ValueError(f"Must have at least 2 points, found {number}")

        lower, upper = -10, 10
        diff = upper - lower
        denominator = number - 1

        self.cubic_points = []
        for i in range(number):
            x = lower + (i * diff / denominator)
            self.cubic_points.append(dualiser.Point(x, x ** 3))

    def plot_points(self, size: float = 5) -> None:
        dualiser.plot_points(self.cubic_points, color="rainbow", s=size)

    def plot_duals(self, width: float = 1) -> None:
        dualiser.plot_duals(self.cubic_points, color="rainbow", linewidth=width)

    # noinspection DuplicatedCode
    def plot(self, size: float = None, width: float = None, save: bool = False) -> None:
        if size and width:
            raise ValueError(
                "For the cubic curve, the points and duals cannot both be printed."
            )

        if not size:
            plt.xlim(-1.5, 1.5)
            plt.ylim(-0.04, 0.04)
        plt.axis("off")

        self.plot_points(size=size) if size else None
        self.plot_duals(width=width) if width else None

        if save:
            plt.savefig(
                "cubic-curve.png" if size else "cubic-dual.png",
                # bbox_inches="tight",
                bbox_inches=0,
                dpi=1080,
                format="png",
            )
        plt.show()


def main() -> None:
    SimpleTriangularGrid().plot(size=5, width=0.75)
    UnitCircle(20).plot(width=0.75)

    CubicCurve(19).plot(width=0.75)
    CubicCurve(19).plot(width=2)
    CubicCurve(19).plot(width=3)
    CubicCurve(41).plot(width=0.75)
    CubicCurve(61).plot(width=0.75)
    CubicCurve(101).plot(width=0.75)
    CubicCurve(151).plot(width=0.75, save=True)


if __name__ == "__main__":
    main()
