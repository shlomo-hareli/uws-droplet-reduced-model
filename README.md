UWS Droplet Reduced Model (Tabulated Framework)

Title:
Tabulated Reduced Model for Urea Decomposition in Urea–Water-Solution (UWS) Sprays for CFD Applications

Manuscript status:
Submitted to Chemical Engineering Journal

Author:
Shlomo Hareli
Karlsruhe Institute of Technology (KIT)
Institute of Technical Thermodynamics

Project Overview

This repository provides a tabulated reduced-order model for the simulation of urea–water-solution (UWS) droplet evaporation and decomposition in selective catalytic reduction (SCR) systems.

The model replaces computationally expensive detailed droplet chemistry with a compact surrogate formulation based on a progress-variable representation and interpolation in precomputed simulation data.

It is designed for integration into Euler–Lagrange CFD spray frameworks.

Scientific Objective

The objective is to provide a computationally efficient surrogate model that accurately reproduces:

droplet heating and evaporation
urea decomposition pathways
ammonia formation
solid residue formation
coupled heat and mass transfer

while significantly reducing computational cost compared to full detailed simulations.

Model Formulation

The thermochemical state of a droplet is represented as:

Psi = Psi(phi, T0, r0)

where:
phi = progress variable
T0 = ambient temperature
r0 = initial droplet radius

The evolution of the system is governed by:

dphi/dt = phi_dot(phi, T0, r0)

Time integration:

phi(t+dt) = phi(t) + phi_dot * dt

All additional thermochemical variables are reconstructed as functions of phi.

State Vector (24 Variables)

0 phi progress variable
1 dphi_dt source term
2 d2eq normalized droplet diameter
3 md droplet mass
4 temp droplet temperature
5 rho density

6 w_h2o water mass fraction
7 w_ur_s urea solid
8 w_ur_l urea liquid
9 w_hnco isocyanic acid

10 w_biu_l biuret liquid
11 w_biu_s biuret solid
12 w_triu triuret
13 w_cya_s cyanuric acid
14 w_amd_s ammelide

15 e_h2o evaporation rate (H2O)
16 e_nh3 evaporation rate (NH3)
17 e_cya evaporation rate (CYA)
18 e_amd evaporation rate (AMD)
19 e_ur evaporation rate (urea)
20 e_hnco evaporation rate (HNCO)

21 qdot heat flux
22 t time
23 mdot total mass loss rate

Parameter Space

Temperature range:
400 – 650 K

Droplet radius range:
2.5e-06 – 1.05e-04 m

Progress variable range:
0 – 1

Numerical Method

The model consists of three main components:

Bilinear interpolation in (T, r) space
selects four neighboring tabulated states
constructs local reduced trajectory
Progress-variable reconstruction
reduces system evolution to a single scalar variable
Explicit time integration
advances phi using interpolated source term

Model Features

Fully tabulated reduced-order droplet chemistry model
Captures evaporation, decomposition, and residue formation
Compatible with Euler–Lagrange CFD solvers
Deterministic surrogate without on-the-fly chemistry integration
Efficient evaluation suitable for spray-scale simulations

Validity and Assumptions

Spherical droplets
Spatially homogeneous liquid and solid phases
Dilute spray conditions
Negligible droplet–droplet interaction
Valid only within tabulated parameter ranges


Validation Concept

The reduced model is validated against detailed one-dimensional droplet simulations.

It reproduces:

evaporation dynamics
temperature evolution
ammonia release
solid formation kinetics

with controlled errors depending on tabulation resolution.

Computational Efficiency

The reduced model replaces stiff coupled thermo-chemical integration with:

interpolation operations
a single ODE in phi

resulting in a significant reduction in computational cost.

Funding

German Research Foundation (DFG)
SFB TRR 150 (TP-B07), Project No. 237267381

Publication

Manuscript submitted to:

Chemical Engineering Journal

Title:
Tabulated Reduced Model for Urea Decomposition in Urea–Water-Solution (UWS) Sprays for CFD Applications

Reproducibility

To reproduce results:

Load precomputed table
Choose (T0, r0)
Perform bilinear interpolation
Integrate phi evolution
Reconstruct state variables

Contact

Karlsruhe Institute of Technology (KIT)
Institute of Technical Thermodynamics
