UWS Droplet Reduced Model (Tabulated Framework)

Tabulated Reduced Model for Urea Decomposition in Urea–Water-Solution (UWS) Sprays for CFD Applications

Manuscript status: Submitted to Chemical Engineering Journal

Author: Shlomo Hareli
Karlsruhe Institute of Technology (KIT)
Institute of Technical Thermodynamics

Project Overview

This repository provides a tabulated reduced-order model for simulation of urea–water-solution (UWS) droplet evaporation and decomposition in selective catalytic reduction (SCR) systems.

The model replaces expensive detailed droplet chemistry with a surrogate formulation based on a progress-variable representation and interpolation in precomputed simulation data.

It is designed for integration into Euler–Lagrange CFD spray solvers.

Scientific Objective

The objective is to reproduce the following processes:

Droplet heating and evaporation
Urea decomposition pathways
Ammonia formation
Solid residue formation
Coupled heat and mass transfer

while significantly reducing computational cost compared to full chemistry simulations.

Model Formulation

The thermochemical state is represented as:

Psi = Psi(phi, T0, r0)

where:

phi = progress variable
T0 = ambient temperature
r0 = initial droplet radius

The system evolves as:

dphi/dt = phi_dot(phi, T0, r0)

Time integration:

phi(t+dt) = phi(t) + phi_dot * dt

All other variables are reconstructed from phi.

State Vector (24 Variables)

0 phi Progress variable
1 dphi_dt Source term
2 d2eq Normalized droplet diameter
3 md Droplet mass
4 temp Temperature
5 rho Density
6 w_h2o Water mass fraction
7 w_ur_s Urea solid
8 w_ur_l Urea liquid
9 w_hnco Isocyanic acid
10 w_biu_l Biuret liquid
11 w_biu_s Biuret solid
12 w_triu Triuret
13 w_cya_s Cyanuric acid
14 w_amd_s Ammelide
15 e_h2o Evaporation rate H2O
16 e_nh3 Evaporation rate NH3
17 e_cya Evaporation rate CYA
18 e_amd Evaporation rate AMD
19 e_ur Evaporation rate Urea
20 e_hnco Evaporation rate HNCO
21 qdot Heat flux
22 t Time
23 mdot Mass loss rate

Parameter Space

Temperature: 400 – 650 K
Droplet radius: 2.5e-6 – 1.05e-4 m
Progress variable: 0 – 1

Numerical Method
Bilinear interpolation in (T, r) space
Progress-variable reconstruction
Explicit time integration
Model Features
Fully tabulated reduced-order droplet chemistry model
Captures evaporation and decomposition
Compatible with Euler–Lagrange CFD solvers
Deterministic (no stochastic sampling)
Efficient evaluation for spray-scale simulations
Validity and Assumptions
Spherical droplets
Homogeneous phases
Dilute spray regime
No droplet–droplet interaction
Valid only within tabulated range
Validation Concept

Validated against detailed droplet simulations:

Evaporation dynamics
Temperature evolution
Ammonia formation
Solid formation

Accuracy depends on table resolution.

Computational Efficiency

The model replaces stiff chemistry integration with:

Interpolation operations
Single ODE in phi

resulting in a significant reduction in computational cost.

Funding

German Research Foundation (DFG)
SFB TRR 150 (TP-B07), Project No. 237267381

Publication

Manuscript submitted to: Chemical Engineering Journal

Title: Tabulated Reduced Model for Urea Decomposition in Urea–Water-Solution (UWS) Sprays for CFD Applications

Reproducibility
Load precomputed table
Choose T0 and r0
Interpolate
Integrate phi
Reconstruct variables
Contact

Karlsruhe Institute of Technology (KIT)
Institute of Technical Thermodynamics
