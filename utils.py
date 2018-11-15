
from os import listdir
from os.path import isfile, join
import json


def load_datasets(path='datasets/'):
    """Load all dataset in memory.

    This function load all tweets datasets from 'datasets' folder to a
    dictionary where the key is name of file.

    Args:
        arg1 (string): Path used to find the datasets.
    Returns:
        dict: different datasets in path like dictionary.

    Examples:
        >>> datasets = load_datasets()
        >>> datasets['theinterngroup']
        [tweet_1, tweet_2, tweet_3, ... , tweet_n]
    """
    path = 'datasets/'
    files = [f for f in listdir(path) if isfile(join(path, f))]

    datasets = {}
    for file in files:
        with open("datasets/%s" % file) as f:
            datasets[file[:-5]] = json.load(f)
    return datasets
