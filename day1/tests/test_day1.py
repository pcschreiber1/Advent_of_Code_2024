from io import StringIO

import pytest
import pandas as pd

from auxiliary import solve_exercise1, solve_exercise2


@pytest.fixture()
def data():
    data = """
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3
    """
    # Read the data into a DataFrame
    df = pd.read_csv(StringIO(data), sep=r"\s+", header=None)

    # Extract the left and right columns as separate Series
    return df[0].copy(), df[1].copy()


def test_exercise1(data):
    a, b = data
    assert solve_exercise1(a, b) == 11


def test_exercise2(data):
    a, b = data
    assert solve_exercise2(a, b) == 31
