"""
Plot points and their duals.
"""

from __future__ import annotations

import graphs


def main() -> None:
    """
    Plot points and their duals.
    """
    graphs.SimpleTriangularGrid().plot(size=5, width=0.75)
    graphs.UnitCircle(20).plot(width=0.75)

    graphs.CubicCurve(19).plot(width=0.75)
    graphs.CubicCurve(19).plot(width=2)
    graphs.CubicCurve(19).plot(width=3)
    graphs.CubicCurve(41).plot(width=0.75)
    graphs.CubicCurve(61).plot(width=0.75)
    graphs.CubicCurve(101).plot(width=0.75)
    graphs.CubicCurve(151).plot(width=0.75, save=True)


if __name__ == "__main__":
    main()
