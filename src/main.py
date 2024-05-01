"""
Plot points and their duals.
"""

from __future__ import annotations

import graphs


def main() -> None:
    """
    Plot points and their duals.
    """
    # fmt: off
    graphs.SimpleTriangularGrid().plot(size=5, width=0.75, save=False, path="assets/triangular-grid.png")
    graphs.UnitCircle(20).plot(width=0.75, save=False, path="assets/unit-circle.png")

    graphs.CubicCurve(19).plot(width=0.75, save=False, path="assets/cubic-dual-19.png")
    graphs.CubicCurve(19).plot(width=2, save=False, path="assets/cubic-dual-19-thick.png")
    graphs.CubicCurve(19).plot(width=3, save=False, path="assets/cubic-dual-19-thicker.png")
    graphs.CubicCurve(41).plot(width=0.75, save=False, path="assets/cubic-dual-41.png")
    graphs.CubicCurve(61).plot(width=0.75, save=False, path="assets/cubic-dual-61.png")
    graphs.CubicCurve(101).plot(width=0.75, save=False, path="assets/cubic-dual-101.png")
    graphs.CubicCurve(151).plot(width=0.75, save=False, path="assets/cubic-dual-151.png")
    # fmt: on


if __name__ == "__main__":
    main()
