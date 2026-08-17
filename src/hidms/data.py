"""Data loading and preprocessing.

TODO(thesis): implement loaders for the consented/de-identified HIDMS datasets
(e.g. health questionnaires, IoT measurements, symptom reports).
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from hidms.config import PROCESSED_DATA_DIR, RAW_DATA_DIR


def load_raw_data(name: str, data_dir: Path = RAW_DATA_DIR) -> pd.DataFrame:
    """Load a raw dataset (CSV) from the data directory.

    Parameters
    ----------
    name : str
        Dataset filename, e.g. ``"health_records.csv"``.
    data_dir : Path
        Directory to read from.

    Returns
    -------
    pd.DataFrame
        The loaded dataset.
    """
    return pd.read_csv(data_dir / name)


def save_processed(df: pd.DataFrame, name: str, data_dir: Path = PROCESSED_DATA_DIR) -> Path:
    """Persist a cleaned/processed dataset."""
    data_dir.mkdir(parents=True, exist_ok=True)
    out_path = data_dir / name
    df.to_csv(out_path, index=False)
    return out_path


def train_test_split(
    df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split a dataset into train and test sets (stratified on the target)."""
    from sklearn.model_selection import train_test_split as sk_split

    return sk_split(df, test_size=test_size, random_state=random_state, stratify=df.get("target"))
