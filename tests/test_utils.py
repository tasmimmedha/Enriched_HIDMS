"""Smoke tests for the hidms package."""

import numpy as np

from hidms import __version__
from hidms.utils import set_seed


def test_version():
    assert isinstance(__version__, str) and __version__


def test_set_seed_is_reproducible():
    set_seed(42)
    a = np.random.rand(5)
    set_seed(42)
    b = np.random.rand(5)
    np.testing.assert_array_equal(a, b)


def test_imports():
    import hidms.config  # noqa: F401
    import hidms.data  # noqa: F401
    import hidms.evaluation  # noqa: F401
    import hidms.features  # noqa: F401
    import hidms.models  # noqa: F401
