"""Evaluation metrics and reporting.

Clinical risk prediction should be evaluated with both standard ML metrics
and decision-support metrics (sensitivity/specificity trade-offs).
"""

from __future__ import annotations

import numpy as np
from sklearn.metrics import accuracy_score, f1_score, precision_recall_fscore_support, roc_auc_score


def classification_report(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    """Compute standard classification metrics."""
    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average="weighted")
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def auc_score(y_true: np.ndarray, y_proba: np.ndarray) -> float:
    """Area under the ROC curve."""
    return float(roc_auc_score(y_true, y_proba))


def save_figure(fig, name: str, figures_dir=None) -> None:
    """Save a matplotlib figure to the reports/figures directory."""
    from hidms.config import FIGURES_DIR

    out_dir = figures_dir or FIGURES_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_dir / name, dpi=300, bbox_inches="tight")
