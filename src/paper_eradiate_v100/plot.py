import eradiate
import numpy as np
import seaborn as sns
import matplotlib.tri as tri
import matplotlib.pyplot as plt


def set_style():
    sns.set_theme(style="ticks")


def plot_polarfilm(
    da,
    levels=16,
    show_contour=True,
    show_azimuth=False,
    figsize=(3, 3),
    azimuth_convention=None,
    vmin=None,
    vmax=None,
    theta_max=90.0,
):
    # Filter grazing angles
    da = (
        da.where(da.vza <= theta_max)
        .dropna("x_index", how="all")
        .dropna("y_index", how="all")
    )
    theta_max = float(da.vza.max())
    rscale = 90.0 / theta_max

    # Prepare data for plotting
    azimuth_convention = (
        eradiate.frame.AzimuthConvention.convert(azimuth_convention)
        if azimuth_convention is not None
        else eradiate.config.settings.AZIMUTH_CONVENTION
    )
    values = da.transpose("x_index", "y_index").values.ravel()
    zeniths = da["vza"].values.ravel()  # Degree
    azimuths = np.deg2rad(da["vaa"].values).ravel()  # Radian

    # Create triangulation
    x = zeniths * np.cos(azimuths) * rscale
    y = zeniths * np.sin(azimuths) * rscale
    triangles = tri.Triangulation(x, y)

    # Make plot
    fig = plt.figure(0, figsize=figsize)
    rect = [0, 0, 1, 1]

    ## Main plot in Cartesian coordinates
    ax_cartesian = fig.add_axes(rect, aspect="equal")
    ax_cartesian.axis("off")  # Hide axis
    ctr = ax_cartesian.tricontourf(
        triangles,
        values,
        levels=levels,
        cmap="viridis",
        vmin=vmin,
        vmax=vmax,
    )

    if show_contour:
        ax_cartesian.tricontour(
            triangles,
            values,
            levels=levels,
            linewidths=0.5,
            colors="w",
            alpha=0.5,
            vmin=vmin,
            vmax=vmax,
        )

    if show_azimuth:
        ax_cartesian.scatter(x, y, c=azimuths, cmap="plasma", s=3)

    ax_cartesian.set_xlim([-90, 90])  ## Match limits with the full zenith range
    ax_cartesian.set_ylim([-90, 90])

    ## Polar axes
    ax_polar = fig.add_axes(rect, polar=True, facecolor="none")
    ax_polar.set_rlim([0, theta_max])  # Cover the full zenith value range
    ax_polar.grid(False, axis="x")
    ax_polar.grid(axis="y", alpha=0.25)
    ax_polar.tick_params(axis="y", colors="white")
    ax_polar.set_rlabel_position(120)

    ax_polar.set_theta_offset(azimuth_convention.value[0])
    ax_polar.set_theta_direction(azimuth_convention.value[1])

    # Add the color bar (important: both axes must be adjusted)
    fig.colorbar(ctr, ax=[ax_cartesian, ax_polar], shrink=0.75, pad=0.15)

    return fig
