"""Interactive demo for the HIDMS diabetes-risk model.

Run the trained model on a patient's measurements and get a plain-language
risk interpretation.

    python -m hidms.demo            # interactive prompt
    python -m hidms.demo --patient "45,f,1.65,70,120,80,95,190,50,110,130,0,1,0"
    python -m hidms.demo --sample   # three pre-built example patients

⚠️  Demo only — simulated data, not for clinical use.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import joblib
import numpy as np

from hidms.config import MODELS_DIR
from hidms.synthetic import FEATURE_COLUMNS, patient_record

DEFAULT_MODEL_PATH = MODELS_DIR / "demo_diabetes_risk.joblib"

RISK_LEVELS = [
    (0.20, "Low", "Keep up the healthy habits - recheck annually or as advised."),
    (
        0.50,
        "Moderate",
        "Some risk factors present — consider lifestyle changes and a check-up with a doctor.",
    ),
    (1.01, "High", "Strong risk signals - please consult a healthcare professional soon."),
]


def load_model(model_path: Path = DEFAULT_MODEL_PATH):
    """Load the saved demo model, or train it on the fly if missing."""
    if not model_path.exists():
        from scripts.train_demo import train_and_save  # type: ignore[import-not-found]

        train_and_save(model_path=model_path)
    return joblib.load(model_path)


def predict_risk(model, patient: dict | list) -> dict:
    """Predict diabetes risk for a single patient.

    Parameters
    ----------
    model : fitted sklearn estimator
        The trained demo model.
    patient : dict or list
        Raw measurements (keys understood by :func:`hidms.synthetic.patient_record`)
        or a pre-built feature row.

    Returns
    -------
    dict
        With keys ``risk`` (probability), ``level``, ``message`` and ``features``.
    """
    if isinstance(patient, dict):
        patient = patient_record(**patient)
    else:
        patient = patient[FEATURE_COLUMNS]

    proba = model.predict_proba(patient)[0][1]
    risk = float(proba)

    for threshold, level, message in RISK_LEVELS:
        if risk < threshold:
            break
    return {
        "risk": round(risk, 3),
        "level": level,
        "message": message,
        "features": patient,
    }


def print_report(result: dict) -> None:
    """Pretty-print a prediction report."""
    risk = result["risk"]
    level = result["level"]
    print("=" * 58)
    print("  HIDMS - Diabetes Risk Assessment (demo)")
    print("=" * 58)
    print(f"  Predicted risk      : {risk * 100:5.1f}%")
    print(f"  Risk level          : {level}")
    print("-" * 58)
    print(f"  {result['message']}")
    print("=" * 58)


def parse_patient_arg(raw: str) -> dict:
    """Parse the ``--patient`` CSV argument into keyword inputs.

    Expected order (14 values):
    age,sex,height_m,weight_kg,systolic_bp,diastolic_bp,fasting_glucose,
    total_cholesterol,hdl,ldl,triglycerides,smoker,physical_activity,family_history
    """
    vals = [v.strip() for v in raw.split(",")]
    if len(vals) != 14:
        sys.exit(
            "Expected 14 comma-separated values: "
            "age,sex(m/f),height_m,weight_kg,systolic_bp,diastolic_bp,glucose,"
            "total_chol,hdl,ldl,triglycerides,smoker(0/1),activity(0/1),family_history(0/1)"
        )
    return {
        "age": float(vals[0]),
        "sex": vals[1],
        "height_m": float(vals[2]),
        "weight_kg": float(vals[3]),
        "systolic_bp": float(vals[4]),
        "diastolic_bp": float(vals[5]),
        "fasting_glucose": float(vals[6]),
        "total_cholesterol": float(vals[7]),
        "hdl": float(vals[8]),
        "ldl": float(vals[9]),
        "triglycerides": float(vals[10]),
        "smoker": bool(int(vals[11])),
        "physical_activity": bool(int(vals[12])),
        "family_history": bool(int(vals[13])),
    }


def interactive_prompt(model) -> None:
    """Ask for measurements one by one on the command line."""
    print("\nEnter patient measurements (press Enter to keep the default):\n")
    defaults = {
        "age": 45, "sex": "female", "height_m": 1.65, "weight_kg": 70,
        "systolic_bp": 120, "diastolic_bp": 80, "fasting_glucose": 95,
        "total_cholesterol": 190, "hdl": 50, "ldl": 110, "triglycerides": 130,
        "smoker": "no", "physical_activity": "yes", "family_history": "no",
    }
    prompts = {
        "age": "Age (years)",
        "sex": "Sex (male/female)",
        "height_m": "Height (m)",
        "weight_kg": "Weight (kg)",
        "systolic_bp": "Systolic BP (mmHg)",
        "diastolic_bp": "Diastolic BP (mmHg)",
        "fasting_glucose": "Fasting glucose (mg/dL)",
        "total_cholesterol": "Total cholesterol (mg/dL)",
        "hdl": "HDL cholesterol (mg/dL)",
        "ldl": "LDL cholesterol (mg/dL)",
        "triglycerides": "Triglycerides (mg/dL)",
        "smoker": "Smoker? (yes/no)",
        "physical_activity": "Physically active? (yes/no)",
        "family_history": "Family history of diabetes? (yes/no)",
    }
    values = {}
    for key, label in prompts.items():
        raw = input(f"  {label:>32} [{defaults[key]}]: ").strip()
        values[key] = raw if raw else defaults[key]

    def _to_bool(v: str) -> bool:
        return v.lower().startswith("y") or v == "1"

    patient = {
        **values,
        "sex": values["sex"],
        "smoker": _to_bool(values["smoker"]),
        "physical_activity": _to_bool(values["physical_activity"]),
        "family_history": _to_bool(values["family_history"]),
    }
    for key in ("age", "height_m", "weight_kg", "systolic_bp", "diastolic_bp",
                "fasting_glucose", "total_cholesterol", "hdl", "ldl", "triglycerides"):
        patient[key] = float(patient[key])

    print_report(predict_risk(model, patient))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="HIDMS diabetes-risk demo")
    parser.add_argument("--patient", help="14 comma-separated measurements (see --help)")
    parser.add_argument("--sample", action="store_true", help="Run three example patients")
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL_PATH, help="Model file path")
    args = parser.parse_args(argv)

    model = load_model(args.model)

    if args.patient:
        print_report(predict_risk(model, parse_patient_arg(args.patient)))
    elif args.sample:
        samples = [
            {"age": 32, "sex": "female", "height_m": 1.65, "weight_kg": 58, "physical_activity": True},
            {"age": 52, "sex": "male", "height_m": 1.75, "weight_kg": 92,
             "fasting_glucose": 140, "family_history": True, "physical_activity": False},
            {"age": 61, "sex": "male", "height_m": 1.72, "weight_kg": 88,
             "fasting_glucose": 175, "systolic_bp": 150, "smoker": True,
             "physical_activity": False, "family_history": True},
        ]
        for i, s in enumerate(samples, start=1):
            print(f"\n--- Example patient #{i} ---")
            print_report(predict_risk(model, s))
    else:
        interactive_prompt(model)


if __name__ == "__main__":
    main()
