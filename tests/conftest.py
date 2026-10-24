"""Define shared fixtures for uncertainty tests."""

import itertools
import pytest

CASES = ((10, 1), (10, 2), (20, 0.1), (10, 0.1), (0.1234, 0.02))

@pytest.fixture(params=list(itertools.permutations(CASES, 2)))
def ab(request):
    """Provide pairs of test cases for uncertainty calculations."""
    return request.param
