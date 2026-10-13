[Русская версия](README.ru.md)

# Numerical Methods: Interpolation and ODEs

A small Python coursework repository for experimenting with numerical interpolation, cubic splines, and step-size error in a stiff first-order differential equation.

## What's included

| File | Purpose |
|---|---|
| `mmc.py` | Interpolation experiments using evenly spaced and Chebyshev nodes, Newton divided differences, and cubic splines. Includes plotting for visual comparison. |
| `MMC2.py` | A separate numerical experiment for an implicit Euler scheme, comparing numerical values against an exact solution across several step sizes. |

The two scripts are separate exercises; they are not a single command-line application.

## Requirements

Python 3, NumPy, and Matplotlib. Install the direct dependencies with:

```bash
python -m pip install -r requirements.txt
```

## Run

From the repository root:

```bash
python mmc.py
python MMC2.py
```

Run each script independently. `mmc.py` saves 24 plots in the current directory; `MMC2.py` prints the maximum error for each listed step size and reports when the requested tolerance is not reached. Both scripts ran successfully during review with Python 3.14.4. On Windows, `MMC2.py` uses ASCII output for compatibility with the default console encoding.

## Scope and limitations

This is coursework rather than a packaged numerical library. The algorithms and boundary cases still need independent mathematical validation, and automated tests are not included in this snapshot. Generated plot files are local output and are not part of the source.
