import json


def save_dict(to_save: dict, output_file: Union[TextIOBase, IO[str], str, PathLike]) -> None:
    try:
        json.dump(to_save, output_file)
    except AttributeError:
        with open(output_file, "w") as output_file:
            json.dump(to_save, output_file)


def load_dict(input_file: Union[TextIOBase, IO[str], str, PathLike]):
    try:
        to_load = json.load(input_file)
    except AttributeError:
        with open(input_file, "r") as input_file:
            to_load = json.load(input_file)

    return to_load
