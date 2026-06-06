# esg-interpretable-ai-tp-anfis-dro
Hybrid TP–ANFIS framework for interpretable ESG modeling with Dynamic Rule Obsolescence (DRO)


Interpretable ESG Modeling using Hybrid TP–ANFIS Framework with Dynamic Rule Obsolescence (DRO)

## Project Overview

This repository contains the data, models, and implementation supporting the study:

"Interpretable ESG Modeling using Hybrid TP–ANFIS Framework with Dynamic Rule Obsolescence"

The project develops a hybrid interpretable artificial intelligence framework for ESG-based sustainability assessment under uncertainty.

## Key Contributions

- Hybrid TP–ANFIS modeling framework for ESG–return analysis
- Compact rule extraction using Tensor-Product (TP) decomposition
- Comparative analysis of TP vs ANFIS under controlled rule complexity
- Dynamic Rule Obsolescence (DRO) for temporal rule stability analysis

## Data

The dataset contains firm-level ESG and financial data:

Inputs:
- Environmental Score
- Social Score
- Governance Score
- ESG Momentum

Output:
- Annual Stock Returns

Processed datasets used in modeling are included in the `/data` folder.

## Models

### ANFIS
- 625-rule fuzzy inference system
- Gaussian membership functions
- GA-optimized parameters

### TP Model
- Tensor-based representation (4D grid)
- HOSVD decomposition
- Low-rank structure extraction
- Compact rule sets (25–40 rules)

## Dynamic Rule Obsolescence (DRO)

The DRO framework evaluates temporal rule reliability using:
- Firing strength decay
- Prediction error drift
- Coverage decay

It identifies stable vs obsolete rules over time.

## Reproducibility

- MATLAB implementation (primary)
- Python scripts (supporting)
- All processed datasets included

## Results Summary

- TP model: ~35% variance explained using compact rules
- ANFIS: R² ≈ 0.74 (full), degrades under compression
- DRO: ~40.64% rules remain temporally stable

## Author

Asefeh Asemi

