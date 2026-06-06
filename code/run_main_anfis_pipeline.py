"""
Main ANFIS pipeline (Python version)
Implements the ANFIS workflow as described in the manuscript.
"""

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from skfuzzy import control as ctrl
import skfuzzy as fuzz

from utils import (
    load_and_prepare_data,
    define_membership_functions,
    build_fis,
    extract_rules
)


def main():
    X, y = load_and_prepare_data()
    mf = define_membership_functions()
    fis = build_fis(mf)
    predictions = fis.predict(X)
    rmse = np.sqrt(mean_squared_error(y, predictions))
    print(f"ANFIS RMSE: {rmse:.4f}")
    extract_rules(fis)


if __name__ == "__main__":
    main()
