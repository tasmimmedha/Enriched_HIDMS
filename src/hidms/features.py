"""Feature engineering.

TODO(thesis): encode clinical/symptom data into features suitable for
risk-prediction models (e.g. BMI, trends over time, comorbidity flags).
"""

from __future__ import annotations

import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Transform raw measurements into model-ready features.

    Parameters
    ----------
    df : pd.DataFrame
        Processed dataset with at least numeric measurement columns.

    Returns
    -------
    pd.DataFrame
        Feature matrix.
    """
    features = df.copy()

    # Example: body-mass index from height (m) and weight (kg) if present.
    if {"height_m", "weight_kg"}.issubset(features.columns):
        features["bmi"] = features["weight_kg"] / features["height_m"] ** 2

    return features


def select_features(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Keep only the selected feature columns."""
    missing = [c for c in columns if c not in df.columns]
    if missing:
        raise ValueError(f"Columns not found in dataframe: {missing}")
    return df[columns]
