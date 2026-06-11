Reduced Droplet Model – Usage

This repository provides a reduced-order model for urea–water solution (UWS) droplet decomposition based on a precomputed tabulated dataset. The model uses bilinear interpolation in ambient temperature (T0) and initial droplet radius (r0), followed by reconstruction of all thermochemical state variables along a progress variable (φ).

------------------------------------------------------------
DATA

File: reduced_model_droplet.npy

Grid resolution:

Temperature grid (T_GRID):
400 K to 650 K with 26 discrete points:
[400, 410, 420, ..., 650] K

Radius grid (R_GRID):
2.5e-6 m to 1.05e-4 m with 22 discrete points:
[2.5e-6, 7.5e-6, 1.25e-5, ..., 1.05e-4] m

This defines the interpolation resolution of the reduced model database.

------------------------------------------------------------
USAGE

1) Define input conditions:

T0 = 523.0       # ambient temperature [K]
r0 = 3.5e-5      # initial droplet radius [m]

2) Interpolate tabulated data:

I = bilinear_interpolation(table, T_GRID, R_GRID, T0, r0)

3) Generate reduced model trajectory:

red_drop = generate_reduced_model_data(I, n_points=10000)

------------------------------------------------------------
OUTPUT

red_drop is a reduced-order trajectory array:

Shape: (n_points, 24)

Column definition (full state vector indexing 0–23):

0  φ (progress variable)
1  dφ/dt
2  droplet radius^2 / initial radius^2
3  droplet mass
4  droplet temperature
5  density
6  H2O mass fraction
7  urea(s) mass fraction
8  urea(l) mass fraction
9  HNCO(l) mass fraction
10 BIU(l) mass fraction
11 BIU(s) mass fraction
12 triuret (TRIU) mass fraction
13 cyanuric acid (CYA) mass fraction
14 ammelide/ammeline species mass fraction
15 H2O evaporation rate
16 NH3 evaporation rate
17 CYA gas formation rate
18 ammelide gas formation rate
19 urea gas formation rate
20 HNCO gas formation rate
21 heat release rate
22 time (pseudo-time variable)
23 total evaporation rate

------------------------------------------------------------
NOTES

- All thermochemical variables are reconstructed as functions of the progress variable φ.
- The integration uses a pseudo-time formulation; time is not a physical CFD time step.
- Input values (T0, r0) must lie within the defined grid range; no extrapolation is performed.
- The grid resolution defines the fidelity of the tabulated surrogate model.

------------------------------------------------------------
PHYSICAL MODEL

The reduced-order formulation assumes:

Y(t) = Y(φ(t))

with:

dφ/dt = f(φ)

All state variables are stored in a precomputed lookup table and reconstructed via interpolation in (T, r) space.

------------------------------------------------------------
AUTHOR

Shlomo Hareli
Postdoctoral Researcher
Institute of Technical Thermodynamics (ITT)
Karlsruhe Institute of Technology (KIT)
