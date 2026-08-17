"""Central configuration: project paths and experiment settings."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

# Repository root (three levels up from this file: src/hidms/config.py -> repo root)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Common directory layout
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

MODELS_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
TESTS_DIR = PROJECT_ROOT / "tests"


@dataclass
class ExperimentConfig:
    """Configuration for a training experiment."""

    target_col: str = "risk_score"
    test_size: float = 0.2
    random_state: int = 42
    n_estimators: int = 100
    max_depth: int | None = None
    features: list[str] = field(default_factory=list)
