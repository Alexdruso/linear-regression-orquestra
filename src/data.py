import numpy as np
from typing import List, Tuple
import pandas as pd
from scipy.stats import zscore


def get_dataset(url: str, names: List[str]) -> pd.DataFrame:
    return pd.read_csv(url, names=names)


def preprocess_data(dataset: pd.DataFrame, features: List[str], target: str) -> Tuple[np.array, np.array]:
    dataset = dataset[features + [target]].apply(func=zscore)

    return zscore(dataset[features].values).reshape(-1, 1), zscore(dataset[target].values)
