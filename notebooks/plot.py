"""Plotting helpers."""


def figsize(
    width: float = 8.3,  # default: 8.3 units
    width_units=1.0 / 2.54 * 1.95,  # 1 cm with arbitrary multiplier
    aspect_ratio: float = 4.0 / 3.0,  # width-to-height ratio
):
    width *= width_units
    return [width, width / aspect_ratio]
