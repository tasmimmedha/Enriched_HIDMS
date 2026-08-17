"""Shared utilities: reproducibility seeds and logging setup."""

from __future__ import annotations

import logging
import random

import numpy as np


def set_seed(seed: int = 42) -> None:
    """Set the random seed for reproducibility across Python/numpy (and torch if installed)."""
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch  # noqa: PLC0415

        torch.manual_seed(seed)
    except ImportError:
        pass


def get_logger(name: str = "hidms") -> logging.Logger:
    """Return a configured module logger."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s"))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
