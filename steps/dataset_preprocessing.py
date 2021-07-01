import json
from src.utils import save_dict, load_dict
from src.data import get_dataset


def load_dataset(url: str, names=List[str]) -> None:
    save_dict(
        to_save=get_dataset(url=url, names=names).to_dict(),
        output_file='dataset.json'
    )


def preprocess_dataset(features: List[str], target: str) -> None:
    dataset = load_dict('dataset.json')

    df = pd.DataFrame.from_dict(dataset)

    x, y = preprocess_data(dataset=df, features=features, target=target)

    save_dict(
        to_save={
            'x': x.tolist(),
            'y': y.tolist()
        },
        output_file='preprocessed_dataset.json'
    )
