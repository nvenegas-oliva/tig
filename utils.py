
from os import listdir
from os.path import isfile, join
import json


def load_datasets():
    path = 'datasets/'
    files = [f for f in listdir(path) if isfile(join(path, f))]

    datasets = {}
    for file in files:
        with open("datasets/%s" % file) as f:
            datasets[file[:-5]] = json.load(f)
    return datasets
