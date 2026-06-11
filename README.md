# UWS Droplet Reduced Model (Tabulated Framework)

**Tabulated Reduced Model for Urea Decomposition in Urea–Water-Solution (UWS) Sprays for CFD Applications**

**Manuscript status:** Submitted to Chemical Engineering Journal

**Author:** Shlomo Hareli  
Karlsruhe Institute of Technology (KIT)  
Institute of Technical Thermodynamics

---

## 📋 Project Overview

This repository provides a tabulated reduced-order model for the simulation of urea–water-solution (UWS) droplet evaporation and decomposition in selective catalytic reduction (SCR) systems.

The model replaces computationally expensive detailed droplet chemistry with a compact surrogate formulation based on a progress-variable representation and interpolation in precomputed simulation data.

It is designed for integration into Euler–Lagrange CFD spray frameworks.

---

## 🎯 Scientific Objective

The objective is to provide a computationally efficient surrogate model that accurately reproduces:

- Droplet heating and evaporation
- Urea decomposition pathways
- Ammonia formation
- Solid residue formation
- Coupled heat and mass transfer

...while significantly reducing computational cost compared to full detailed simulations.

---

## 📐 Model Formulation

The thermochemical state of a droplet is represented as:

```
Psi = Psi(phi, T0, r0)
```

**where:**
- `phi` = progress variable
- `T0` = ambient temperature
- `r0` = initial droplet radius

The evolution of the system is governed by:

```
dphi/dt = phi_dot(phi, T0, r0)
```

**Time integration:**

```
phi(t+dt) = phi(t) + phi_dot * dt
```

All additional thermochemical variables are reconstructed as functions of phi.

---

## 🔢 State Vector (24 Variables)

| Index | Variable | Description |
|-------|----------|-------------|
| 0 | `phi` | Progress variable |
| 1 | `dphi_dt` | Source term |
| 2 | `d2eq` | Normalized droplet diameter |
| 3 | `md` | Droplet mass |
| 4 | `temp` | Droplet temperature |
| 5 | `rho` | Density |
| 6 | `w_h2o` | Water mass fraction |
| 7 | `w_ur_s` | Urea solid |
| 8 | `w_ur_l` | Urea liquid |
| 9 | `w_hnco` | Isocyanic acid |
| 10 | `w_biu_l` | Biuret liquid |
| 11 | `w_biu_s` | Biuret solid |
| 12 | `w_triu` | Triuret |
| 13 | `w_cya_s` | Cyanuric acid |
| 14 | `w_amd_s` | Ammelide |
| 15 | `e_h2o` | Evaporation rate (H₂O) |
| 16 | `e_nh3` | Evaporation rate (NH₃) |
| 17 | `e_cya` | Evaporation rate (CYA) |
| 18 | `e_amd` | Evaporation rate (AMD) |
| 19 | `e_ur` | Evaporation rate (urea) |
| 20 | `e_hnco` | Evaporation rate (HNCO) |
| 21 | `qdot` | Heat flux |
| 22 | `t` | Time |
| 23 | `mdot` | Total mass loss rate |

---

## 📊 Parameter Space

| Parameter | Range |
|-----------|-------|
| **Temperature** | 400 – 650 K |
| **Droplet radius** | 2.5×10⁻⁶ – 1.05×10⁻⁴ m |
| **Progress variable** | 0 – 1 |

---

## 🔧 Numerical Method

The model consists of three main components:

1. **Bilinear interpolation in (T, r) space**
   - Selects four neighboring tabulated states
   - Constructs local reduced trajectory

2. **Progress-variable reconstruction**
   - Reduces system evolution to a single scalar variable

3. **Explicit time integration**
   - Advances phi using interpolated source term

---

## ⭐ Model Features

- ✅ Fully tabulated reduced-order droplet chemistry model
- ✅ Captures evaporation, decomposition, and residue formation
- ✅ Compatible with Euler–Lagrange CFD solvers
- ✅ Deterministic surrogate without on-the-fly chemistry integration
- ✅ Efficient evaluation suitable for spray-scale simulations

---

## ⚠️ Validity and Assumptions

- Spherical droplets
- Spatially homogeneous liquid and solid phases
- Dilute spray conditions
- Negligible droplet–droplet interaction
- Valid only within tabulated parameter ranges

---

## ✅ Validation Concept

The reduced model is validated against detailed one-dimensional droplet simulations.

It reproduces:

- Evaporation dynamics
- Temperature evolution
- Ammonia release
- Solid formation kinetics

...with controlled errors depending on tabulation resolution.

---

## ⚡ Computational Efficiency

The reduced model replaces stiff coupled thermo-chemical integration with:

- Interpolation operations
- A single ODE in phi

resulting in a **significant reduction in computational cost**.

---

## 💰 Funding

**German Research Foundation (DFG)**  
SFB TRR 150 (TP-B07), Project No. 237267381

---

## 📖 Publication

**Manuscript submitted to:** Chemical Engineering Journal

**Title:** Tabulated Reduced Model for Urea Decomposition in Urea–Water-Solution (UWS) Sprays for CFD Applications

---

## 🔄 Reproducibility

To reproduce results:

1. Load precomputed table
2. Choose (T₀, r₀)
3. Perform bilinear interpolation
4. Integrate phi evolution
5. Reconstruct state variables

---

## 📬 Contact

**Karlsruhe Institute of Technology (KIT)**  
Institute of Technical Thermodynamics
