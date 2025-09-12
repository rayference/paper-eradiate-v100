<!-- PROJECT LOGO -->

<p align="center">
<img src="fig/logo.png#gh-light-mode-only" alt="Logo" />
<img src="fig/logo_darkmode.png#gh-dark-mode-only" alt="Logo" />
</p>

<h1 align="center">v1.0.0</h1>

<p align="center">
    Geoscientific Model Development <!-- ADD JOURNAL ISSUE WHEN PUBLISHED -->
    <br />
    <a href="https://github.com/leroyvn/"><strong>Vincent Leroy</strong></a>
    ·
    <strong>Claudia Emde</strong>
    ·
    <strong>Nicolae Marton</strong>
    ·
    <strong>Nicolas Misk</strong>
    ·
    <strong>Misael Gonzalez Almeida</strong>
    ·
    <strong>Sebastian Schunke</strong>
    ·
    <strong>Noelle Cremer</strong>
    ·
    <a href="https://www.linkedin.com/in/ferran-gascon-roca-570b44243/"><strong>Ferran Gascon</strong></a>
    ·
    <strong>Yves Govaerts</strong>
    <br />
    🖥️&nbsp;<a href="https://github.com/eradiate/eradiate/">Source code</a>
    |
    📚&nbsp;<a href="https://eradiate.readthedocs.io/en/v1.0.0/">Documentation</a>
    |
    🗒️&nbsp;Paper PDF
    |
    🌐&nbsp;<a href="https://www.eradiate.eu/">Project website</a>
</p>

<!-- ADD LINK TO AUTHORS -->
<!-- ADD LINK TO PAPER PDF -->

## About

This repository contains the code used for the applications presented in the paper "Eradiate: An Accurate and Flexible Radiative Transfer Model for Earth Observation and Atmospheric Science" submitted to *Geoscientific Model Development*.

This repository contains the code and input data required to reproduce the results presented in the paper and demonstrate some features of the Eradiate radiative transfer model.

> [!IMPORTANT]
> This code is *not* part of the Eradiate documentation and is consequently not updated upon new Eradiate releases.

## Getting started

The examples provided in this repository can be run in several ways:

* **Reproducible setup with Pixi**

  1. Install [Pixi](https://pixi.sh/) and run `pixi install` at the root of this
     repository.
  2. Run `pixi run download` to download the support data.
  3. Run `pixi run jupyter lab` to open a Jupyter Lab session and start browsing
     the examples.

* **Classic Conda environment**

  1. Install [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main).
  2. Create a Conda environment from the provided environment file by calling
     `conda env create -f environment.yml -n paper-eradiate-v100`.
  3. Activate the environment by calling `conda activate paper-eradiate-v100`.
  4. Run `python download.py` to download the core support data.
  5. Run `jupyter lab` to open a Jupyter Lab session and start browsing the
     examples.

> [!IMPORTANT]
> The Algeria and Dakar scenes require additional resources, which can be
> downloaded with the `download.py` utility (accessible with `pixi download` if
> you are using Pixi).

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Citation

*TBD*

<!-- ADD BibTeX citation -->
