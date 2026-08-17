"""Train the HIDMS diabetes-risk demo model end-to-end.

Generates a synthetic patient dataset, trains a Random Forest using the
``src/hidms`` pipeline, evaluates it, and saves the model plus a metrics
report.

    python scripts/train_demo.py

Outputs
-------
- ``data/raw/demo_health_records.csv``     simulated patient records
- ``models/demo_diabetes_risk.joblib``     trained model
- ``reports/demo_metrics.json``            evaluation metrics
- ``reports/figures/demo_feature_importance.png``  feature-importance chart

⚠️  Demo only — simulated data, not for clinical use.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import joblib
import numpy as np

# Make ``src`` importable when running this file directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hidms.config import ExperimentConfig, MODELS_DIR, PROCESSED_DATA_DIR, RAW_DATA_DIR, REPORTS_DIR
from hidms.evaluation import auc_score, classification_report
from hidms.models import build_model, predict, predict_proba, train_model
from hidms.synthetic import FEATURE_COLUMNS, TARGET_COLUMN, generate_synthetic_patients
from hidms.utils import get_logger, set_seed

logger = get_logger("hidms.demo")


def train_and_save(
    n_patients: int = 2000,
    seed: int = 42,
    model_path: Path | None = None,
) -> dict:
    """Generate data, train the model, evaluate, and persist everything."""
    set_seed(seed)

    # 1. Simulated data (de-identified by construction).
    logger.info("Generating %d synthetic patients (seed=%d) ...", n_patients, seed)
    df = generate_synthetic_patients(n=n_patients, seed=seed)

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    raw_path = RAW_DATA_DIR / "demo_health_records.csv"
    df.to_csv(raw_path, index=False)
    logger.info("Saved raw records -> %s", raw_path)

    # 2. Features & split.
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=seed, stratify=y
    )
    logger.info("Train: %d rows | Test: %d rows | positive rate: %.1f%%",
                len(X_train), len(X_test), 100 * y.mean())

    # 3. Train the pipeline from src/hidms/models.py.
    config = ExperimentConfig(
        target_col=TARGET_COLUMN,
        test_size=0.2,
        random_state=seed,
        n_estimators=200,
        features=FEATURE_COLUMNS,
    )
    model = build_model(config)
    train_model(model, X_train, y_train)

    # 4. Evaluate with src/hidms/evaluation.py.
    y_pred = predict(model, X_test)
    y_proba = predict_proba(model, X_test)[:, 1]
    metrics = classification_report(y_test, y_pred)
    metrics["roc_auc"] = auc_score(y_test, y_proba)
    logger.info("Test metrics: %s", metrics)

    # 5. Persist model.
    out_model = model_path or (MODELS_DIR / "demo_diabetes_risk.joblib")
    out_model.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, out_model)
    logger.info("Saved model -> %s", out_model)

    # 6. Metrics report.
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "dataset": "synthetic (simulated, de-identified)",
        "n_patients": int(n_patients),
        "seed": seed,
        "model": "RandomForestClassifier (n_estimators=200)",
        **metrics,
    }
    metrics_path = REPORTS_DIR / "demo_metrics.json"
    metrics_path.write_text(json.dumps(report, indent=2))
    logger.info("Saved metrics -> %s", metrics_path)

    # 7. Feature-importance chart (optional, needs matplotlib).
    _save_feature_importance(model, X.columns)

    return report


def _save_feature_importance(model, feature_names) -> None:
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:  # pragma: no cover - optional dependency
        logger.warning("matplotlib not installed; skipping feature-importance chart.")
        return

    importances = np.asarray(model.named_steps["classifier"].feature_importances_)
    order = np.argsort(importances)[::-1]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh([feature_names[i] for i in order][::-1], importances[order][::-1], color="#2a9d8f")
    ax.set_xlabel("Feature importance")
    ax.set_title("Diabetes-risk demo — top predictive features")
    fig.tight_layout()

    out_dir = REPORTS_DIR / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_dir / "demo_feature_importance.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    logger.info("Saved figure -> %s", out_dir / "demo_feature_importance.png")


def main() -> None:
    report = train_and_save()
    print("\n" + "=" * 58)
    print("  Demo training complete")
    print(f"  Accuracy : {report['accuracy'] * 100:.1f}%")
    print(f"  F1       : {report['f1'] * 100:.1f}%")
    print(f"  ROC-AUC  : {report['roc_auc'] * 100:.1f}%")
    print("=" * 58)


if __name__ == "__main__":
    main()
