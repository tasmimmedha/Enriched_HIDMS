"""Model definitions, training, and prediction.

TODO(thesis): implement and benchmark risk-prediction models
(e.g. Logistic Regression, Random Forest, Gradient Boosting, XGBoost).
"""

from __future__ import annotations

from typing import Any

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

from hidms.config import ExperimentConfig
from hidms.utils import set_seed


def build_model(config: ExperimentConfig) -> Pipeline:
    """Build a scikit-learn pipeline for risk prediction."""
    set_seed(config.random_state)
    return Pipeline(
        steps=[
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=config.n_estimators,
                    max_depth=config.max_depth,
                    random_state=config.random_state,
                    n_jobs=-1,
                ),
            )
        ]
    )


def train_model(model: Any, X_train: np.ndarray, y_train: np.ndarray) -> Any:
    """Fit the model on training data."""
    return model.fit(X_train, y_train)


def predict(model: Any, X: np.ndarray) -> np.ndarray:
    """Return class predictions."""
    return model.predict(X)


def predict_proba(model: Any, X: np.ndarray) -> np.ndarray:
    """Return predicted class probabilities."""
    return model.predict_proba(X)
