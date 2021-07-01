from src.linear_regression import build_precision_matrix, build_precision_two_complement_fixed_point, build_Q
from src.utils import load_dict, save_dict
import dimod
import numpy as np


def get_precision(num_bits: int, num_weights: int, point_position: float) -> None:
    save_dict(
        to_save={
            'precision': build_precision_matrix(
                num_weights=num_weights,
                precision=build_precision_two_complement_fixed_point(
                    num_bits=num_bits,
                    point_position=point_position
                )
            ).tolist()
        },
        output_file='precision_matrix.json'
    )


def get_problem_matrix() -> None:
    precision = load_dict('precision_matrix.json')['precision']
    dataset = load_dict('preprocessed_dataset.json')
    precision = np.asarray(precision)
    x = np.asarray(dataset['x'])
    y = np.asarray(dataset['y'])

    save_dict(
        to_save={
            'q': build_Q(
                precision_matrix=precision,
                feature_matrix=x,
                target_matrix=y
            ).tolist()
        },
        output_file='q.json'
    )


def anneal() -> None:
    q = np.asarray(
        load_dict('q.json')['q']
    )

    precision = load_dict('precision_matrix.json')['precision']
    precision = np.asarray(precision)

    array_bqm = dimod.AdjArrayBQM(q, 'BINARY')

    sample_set = dimod.SimulatedAnnealingSampler().sample(array_bqm)

    w_binary = np.asarray(list(sample_set.first.sample.values()))

    w_approx = precision.dot(w_binary)

    save_dict(
        {
            'solution': w_approx
        },
        'solution.json'
    )
