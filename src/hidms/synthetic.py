"""Synthetic, de-identified health-data generator for the HIDMS demo.

The generator produces realistic, *simulated* patient records for a
diabetes-risk demo. No real patient data is involved — every row is
synthesised from medically plausible correlations (age, BMI, blood
pressure, glucose, lipids, lifestyle) plus noise.

⚠️  This is for *demonstration only*: the data is simulated and the model
trained on it must never be used for real clinical decisions.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from hidms.utils import set_seed

# Model features (in the exact order the model expects them).
FEATURE_COLUMNS: list[str] = [
    "age",
    "sex_male",
    "bmi",
    "systolic_bp",
    "diastolic_bp",
    "fasting_glucose",
    "total_cholesterol",
    "hdl",
    "ldl",
    "triglycerides",
    "smoker",
    "physical_activity",
    "family_history",
]

TARGET_COLUMN: str = "has_diabetes"

# Base rates used to make the simulated population realistic.
DIABETES_PREVALENCE = 0.22  # roughly the share of "at-risk" positives we generate


def _logistic(x: np.ndarray) -> np.ndarray:
    """Sigmoid, kept numerically stable."""
    return 1.0 / (1.0 + np.exp(-np.clip(x, -30, 30)))


def generate_synthetic_patients(n: int = 2000, seed: int = 42) -> pd.DataFrame:
    """Generate ``n`` simulated patient records with a diabetes-risk label.

    Parameters
    ----------
    n : int
        Number of patients to simulate.
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    pd.DataFrame
        De-identified records with measurement columns and a binary
        ``has_diabetes`` label.
    """
    set_seed(seed)
    rng = np.random.default_rng(seed)

    n = int(n)
    age = rng.normal(48, 14, n).clip(20, 85)
    sex_male = rng.integers(0, 2, n)
    height_m = rng.normal(1.68, 0.09, n).clip(1.40, 2.00)
    weight_kg = rng.normal(74, 15, n).clip(40, 140)
    bmi = weight_kg / height_m**2

    # Blood pressure rises with age and BMI.
    systolic_bp = rng.normal(118, 14, n) + 0.35 * (age - 48) + 0.5 * (bmi - 26)
    systolic_bp = systolic_bp.clip(90, 200)
    diastolic_bp = rng.normal(76, 10, n) + 0.15 * (age - 48) + 0.2 * (bmi - 26)
    diastolic_bp = diastolic_bp.clip(55, 130)

    # Fasting glucose: strongly driven by age, BMI and family history.
    fasting_glucose = rng.normal(95, 12, n) + 0.45 * (age - 48) + 0.9 * (bmi - 26)
    fasting_glucose = fasting_glucose.clip(65, 300)

    # Lipids.
    total_cholesterol = rng.normal(190, 35, n) + 0.4 * (age - 48) + 0.5 * (bmi - 26)
    total_cholesterol = total_cholesterol.clip(120, 320)
    hdl = rng.normal(52, 13, n) - 0.4 * (bmi - 26) - 6 * sex_male
    hdl = hdl.clip(20, 100)
    ldl = (total_cholesterol - hdl - 0.2 * rng.normal(150, 40, n)).clip(50, 240)
    triglycerides = rng.normal(130, 55, n) + 0.8 * (bmi - 26)
    triglycerides = triglycerides.clip(40, 600)

    # Lifestyle.
    smoker = rng.binomial(1, 0.18, n)
    physical_activity = rng.binomial(1, 0.55, n)  # 1 = active
    family_history = rng.binomial(1, 0.30, n)

    # Ground-truth risk: weighted clinical contributors + noise.
    risk_logit = (
        0.055 * (fasting_glucose - 95)
        + 0.045 * (bmi - 26)
        + 0.02 * (age - 48)
        + 0.9 * family_history
        - 0.8 * physical_activity
        + 0.4 * smoker
        + rng.normal(0, 1.1, n)
    )
    prob = _logistic(risk_logit - np.log((1 - DIABETES_PREVALENCE) / DIABETES_PREVALENCE))
    has_diabetes = rng.binomial(1, prob, n)

    df = pd.DataFrame(
        {
            "patient_id": np.arange(1, n + 1),
            "age": age.round(1),
            "sex_male": sex_male,
            "height_m": height_m.round(2),
            "weight_kg": weight_kg.round(1),
            "bmi": bmi.round(1),
            "systolic_bp": systolic_bp.round(0),
            "diastolic_bp": diastolic_bp.round(0),
            "fasting_glucose": fasting_glucose.round(0),
            "total_cholesterol": total_cholesterol.round(0),
            "hdl": hdl.round(0),
            "ldl": ldl.round(0),
            "triglycerides": triglycerides.round(0),
            "smoker": smoker,
            "physical_activity": physical_activity,
            "family_history": family_history,
            TARGET_COLUMN: has_diabetes,
        }
    )
    return df


def patient_record(
    age: float = 45,
    sex: str = "female",
    height_m: float = 1.65,
    weight_kg: float = 70.0,
    systolic_bp: float = 120,
    diastolic_bp: float = 80,
    fasting_glucose: float = 95,
    total_cholesterol: float = 190,
    hdl: float = 50,
    ldl: float = 110,
    triglycerides: float = 130,
    smoker: bool = False,
    physical_activity: bool = True,
    family_history: bool = False,
) -> pd.DataFrame:
    """Build a single-row feature frame from raw patient inputs.

    Used by the interactive CLI demo and the Streamlit app. Missing
    clinical measurements are filled with typical healthy values.
    """
    bmi = weight_kg / height_m**2
    row = {
        "age": float(age),
        "sex_male": 1 if sex.lower().startswith("m") else 0,
        "bmi": round(bmi, 1),
        "systolic_bp": float(systolic_bp),
        "diastolic_bp": float(diastolic_bp),
        "fasting_glucose": float(fasting_glucose),
        "total_cholesterol": float(total_cholesterol),
        "hdl": float(hdl),
        "ldl": float(ldl),
        "triglycerides": float(triglycerides),
        "smoker": int(smoker),
        "physical_activity": int(physical_activity),
        "family_history": int(family_history),
    }
    return pd.DataFrame([row])[FEATURE_COLUMNS]
