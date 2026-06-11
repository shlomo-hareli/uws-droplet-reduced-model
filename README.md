# UWS Droplet Reduced Model (Tabulated Framework)

**Tabulated Reduced Model for Urea Decomposition in Urea–Water-Solution (UWS) Sprays for CFD Applications**

**Manuscript status:** Submitted to *Chemical Engineering Journal*

**Author:** Shlomo Hareli  
**Affiliation:** Karlsruhe Institute of Technology (KIT), Institute of Technical Thermodynamics

---

## Project Overview

This repository provides a **tabulated reduced-order model** for simulation of **urea–water-solution (UWS) droplet evaporation and decomposition** in selective catalytic reduction (SCR) systems.

The model replaces expensive detailed droplet chemistry with a **surrogate formulation** based on a **progress-variable representation** and **interpolation in precomputed simulation data**. It is designed for seamless integration into **Euler–Lagrange CFD spray solvers**.

---

## Scientific Objective

The model reproduces the following coupled processes:

- **Droplet heating and evaporation**
- **Urea decomposition pathways**
- **Ammonia formation**
- **Solid residue formation**
- **Coupled heat and mass transfer**

All while **significantly reducing computational cost** compared to full chemistry simulations.

---

## Model Formulation

### Thermochemical State Representation

The thermochemical state is represented as:

$$\Psi = \Psi(\phi, T_0, r_0)$$

where:
- **φ** = progress variable
- **T₀** = ambient temperature
- **r₀** = initial droplet radius

### System Evolution

The system evolves according to:

$$\frac{d\phi}{dt} = \dot{\phi}(\phi, T_0, r_0)$$

**Time integration scheme:**

$$\phi(t+\Delta t) = \phi(t) + \dot{\phi} \cdot \Delta t$$

All other variables are **reconstructed from φ**.

---

## State Vector (24 Variables)

| Index | Variable | Description |
|-------|----------|-------------|
| 0 | **φ** | Progress variable |
| 1 | **dφ/dt** | Source term |
| 2 | **d₂ₑq** | Normalized droplet diameter |
| 3 | **mₐ** | Droplet mass |
| 4 | **T** | Temperature |
| 5 | **ρ** | Density |
| 6 | **w_H₂O** | Water mass fraction |
| 7 | **w_UR_S** | Urea solid |
| 8 | **w_UR_L** | Urea liquid |
| 9 | **w_HNCO** | Isocyanic acid |
| 10 | **w_BIU_L** | Biuret liquid |
| 11 | **w_BIU_S** | Biuret solid |
| 12 | **w_TRIU** | Triuret |
| 13 | **w_CYA_S** | Cyanuric acid |
| 14 | **w_AMD_S** | Ammelide |
| 15 | **ė_H₂O** | Evaporation rate H₂O |
| 16 | **ė_NH₃** | Evaporation rate NH₃ |
| 17 | **ė_CYA** | Evaporation rate CYA |
| 18 | **ė_AMD** | Evaporation rate AMD |
| 19 | **ė_UR** | Evaporation rate Urea |
| 20 | **ė_HNCO** | Evaporation rate HNCO |
| 21 | **q̇** | Heat flux |
| 22 | **t** | Time |
| 23 | **ṁ** | Mass loss rate |

---

## Parameter Space

The model is valid within the following parametric ranges:

- **Temperature:** 400 – 650 K
- **Droplet radius:** 2.5 × 10⁻⁶ – 1.05 × 10⁻⁴ m
- **Progress variable:** 0 – 1

---

## Numerical Method

- **Interpolation:** Bilinear interpolation in (T, r) space
- **Reconstruction:** Progress-variable reconstruction
- **Time integration:** Explicit time integration scheme

---

## Model Features

- **Fully tabulated** reduced-order droplet chemistry model
- **Captures** evaporation and decomposition mechanisms
- **Compatible** with Euler–Lagrange CFD solvers
- **Deterministic** (no stochastic sampling)
- **Efficient** evaluation for spray-scale simulations

---

## Validity and Assumptions

The model is valid under the following assumptions:

- **Spherical droplets** (geometric assumption)
- **Homogeneous phases** (composition uniformity)
- **Dilute spray regime** (low liquid volume fraction)
- **No droplet–droplet interaction** (Lagrangian decoupling)
- **Valid only within tabulated parameter ranges**

---

## Validation Concept

The model is **validated against detailed droplet simulations** for:

- Evaporation dynamics
- Temperature evolution
- Ammonia formation
- Solid formation

**Accuracy depends on table resolution and interpolation method.**

---

## Computational Efficiency

The model achieves significant performance gains by replacing **stiff chemistry integration** with:

- **Interpolation operations** (lookup in precomputed table)
- **Single ODE in φ** (reduced model dimension)

This results in a **dramatic reduction in computational cost** relative to full chemistry solvers.

---

## Funding

**German Research Foundation (DFG)**  
*SFB TRR 150* (TP-B07), Project No. 237267381

---

## Publication

**Manuscript:** Submitted to *Chemical Engineering Journal*

**Title:** Tabulated Reduced Model for Urea Decomposition in Urea–Water-Solution (UWS) Sprays for CFD Applications

---

## Reproducibility Workflow

1. Load precomputed table
2. Choose T₀ and r₀
3. Interpolate table at (T₀, r₀)
4. Integrate ODE in φ
5. Reconstruct all 24 state variables

---

## Contact

**Karlsruhe Institute of Technology (KIT)**  
Institute of Technical Thermodynamics

**Author:** Shlomo Hareli
