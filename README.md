# Numerical Methods: Interpolation and ODEs

A small Python coursework repository for experimenting with numerical interpolation, cubic splines, and step-size error in a stiff first-order differential equation.

## What's included

| File | Purpose |
|---|---|
| `mmc.py` | Interpolation experiments using evenly spaced and Chebyshev nodes, Newton divided differences, and cubic splines. Includes plotting for visual comparison. |
| `MMC2.py` | A separate numerical experiment for an implicit Euler scheme, comparing numerical values against an exact solution across several step sizes. |

The two scripts are separate exercises; they are not a single command-line application.

## Requirements

Python 3, NumPy, Matplotlib, and SciPy.

```bash
python -m pip install numpy matplotlib scipy
```

## Run

From the repository root:

```bash
python mmc.py
python MMC2.py
```

Run each script independently. The interpolation script opens plots; the ODE experiment prints its step-size error results. These commands describe the source entry points; execution has not been verified in this environment.

## Scope and limitations

This is coursework rather than a packaged numerical library. The algorithms and boundary cases still need independent mathematical validation, and automated tests are not included in this snapshot.