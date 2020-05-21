from statispy import statispyError as sE
import math
import random
import pandas as pd

def __init__():
    pass
    
def validate(data, size, method = 'random'):
    if not isinstance(data, pd.DataFrame):
        raise sE.UnsupportedDataFormatError(type(data))
    if size > len(data) or size <= 0:
        raise sE.InvalidSampleSize(size)
    known_methods = ['random', 'systematic']
    if method not in known_methods:
        raise sE.UnknownSamplingMethodError(method)


def basic_sample(data, size, method = 'random'):
    validate(data, size)
    sample = pd.DataFrame(columns = data.columns)
    if method == 'random':
        sample_index = random.sample(list(data.index), size)
        for i in sample_index:
            sample = sample.append( data.iloc[i])
    if method == 'systematic':
        set_size = int(math.ceil(len(data)/size))
        for i in range(0,size):
            sample = sample.append( data.iloc[i*set_size])
    return sample