import json
from io import TextIOBase
from os import PathLike
from typing import Union, IO
from zquantum.core.utils import SCHEMA_VERSION

def save_dict(to_save: dict, output_file: Union[TextIOBase, IO[str], str, PathLike]) -> None:
    to_save["schema"] = SCHEMA_VERSION + "-dict"
    try:
        json.dump(to_save, output_file)
    except AttributeError:
        with open(output_file, "w") as output_file:
            json.dump(to_save, output_file)


def load_dict(input_file: Union[TextIOBase, IO[str], str, PathLike]) -> dict:
    try:
        to_load = json.load(input_file)
    except AttributeError:
        with open(input_file, "r") as input_file:
            to_load = json.load(input_file)

    del to_load["schema"]

    return to_load
