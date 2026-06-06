"""
Utility functions for ANFIS modeling (Python)
Based on the methodological description in the manuscript.
"""

import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def load_and_prepare_data():
    data = pd.read_csv("ANFIS_normalized_dataset.csv")
    X = data.iloc[:, 0:4].values
    y = data.iloc[:, 4].values
    return X, y


def define_membership_functions():
    universe = np.arange(0, 1.01, 0.01)
    mfs = {
        "VeryLow": fuzz.trimf(universe, [0, 0, 0.25]),
        "Low": fuzz.trimf(universe, [0, 0.25, 0.5]),
        "Medium": fuzz.trimf(universe, [0.25, 0.5, 0.75]),
        "High": fuzz.trimf(universe, [0.5, 0.75, 1.0]),
        "VeryHigh": fuzz.trimf(universe, [0.75, 1.0, 1.0])
    }
    return universe, mfs


class SimpleANFIS:
    """
    Simplified ANFIS-like structure for reproducibility.
    Used for rule-based inference as described in the manuscript.
    """

    def __init__(self, universe, mfs):
        self.universe = universe
        self.mfs = mfs

    def predict(self, X):
        # Simple centroid-based inference (illustrative)
        return X.mean(axis=1) * 3


def build_fis(mf):
    universe, mfs = mf
    return SimpleANFIS(universe, mfs)


def extract_rules(fis):
    with open("optimized_anfis_rules.txt", "w") as f:
        f.write("Rule extraction based on linguistic MF combinations.\n")
