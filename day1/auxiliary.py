import pandas as pd


def get_data(path):
    with open(path, "r") as f:
        list_a = []
        list_b = []
        for row in f:
            a, b = row.split()
            list_a.append(a)
            list_b.append(b)

    s_a = pd.Series(list_a).astype(int)
    s_b = pd.Series(list_b).astype(int)
    return s_a, s_b


def solve_exercise1(data1: pd.Series, data2: pd.Series):
    data1.sort_values(ascending=True, ignore_index=True, inplace=True)
    data2.sort_values(ascending=True, ignore_index=True, inplace=True)
    return data1.sub(data2).abs().sum()


def solve_exercise2(data1: pd.Series, data2: pd.Series):
    return data1.apply(lambda x: x * (data2 == x).sum()).sum()
