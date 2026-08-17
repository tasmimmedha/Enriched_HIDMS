"""Tests for the synthetic data generator and demo pipeline."""

import numpy as np
import pandas as pd

from hidms.synthetic import FEATURE_COLUMNS, TARGET_COLUMN, generate_synthetic_patients, patient_record


def test_generate_synthetic_patients_shape():
    df = generate_synthetic_patients(n=500, seed=7)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 500
    assert TARGET_COLUMN in df.columns
    assert set(FEATURE_COLUMNS).issubset(df.columns)


def test_generate_is_reproducible():
    a = generate_synthetic_patients(n=200, seed=42)
    b = generate_synthetic_patients(n=200, seed=42)
    pd.testing.assert_frame_equal(a, b)


def test_generated_labels_are_balanced_enough():
    df = generate_synthetic_patients(n=2000, seed=42)
    rate = df[TARGET_COLUMN].mean()
    assert 0.10 < rate < 0.40, f"positive rate {rate:.3f} out of expected range"


def test_feature_ranges_are_plausible():
    df = generate_synthetic_patients(n=2000, seed=42)
    assert df["bmi"].between(14, 50).all()
    assert df["systolic_bp"].between(90, 200).all()
    assert df["fasting_glucose"].between(65, 300).all()


def test_patient_record_feature_order():
    row = patient_record(age=50, sex="male", height_m=1.75, weight_kg=80)
    assert list(row.columns) == FEATURE_COLUMNS
    assert row.iloc[0]["sex_male"] == 1
    assert np.isclose(row.iloc[0]["bmi"], 80 / 1.75**2)


def test_demo_predict_risk_runs():
    from hidms.demo import predict_risk, load_model

    model = load_model()
    result = predict_risk(model, patient_record(age=30, physical_activity=True))
    assert 0.0 <= result["risk"] <= 1.0
    assert result["level"] in {"Low", "Moderate", "High"}
    assert result["message"]
