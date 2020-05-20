from statispy import statispyError as sE
import math
import random

def __init__():
    pass

def create_sample(X, size, method = 'random'):
    if method == 'random':
        return random.sample(X, size)
    
def mean(X):
    if isinstance(X, list):
        return sum(X)/len(X)
    elif isinstance(X, dict):
        weighted_sum = 0
        for k in X.keys():
            weighted_sum += X[k]*k
        return weighted_sum/sum(X.keys())
    else:
        raise sE.UnsupportedDataFormatError(type(X))

def RMS(X):
    if isinstance(X, list):
        sum_sq = 0
        for xi in X:
            sum_sq += xi**2
        mean_sq = sum_sq/len(X)
        return math.sqrt(mean_sq)
    else:
        raise sE.UnsupportedDataFormatError(type(X))
    
def variance(X):
    if isinstance(X, list):
        _mean = mean(X)
        _sum = 0
        for xi in X:
            _sum += (xi - _mean)**2
        return _sum/len(X)
    else:
        raise sE.UnsupportedDataFormatError(type(X))

def SD(X):
    if isinstance(X, list):
        return math.sqrt(variance(X))
    else:
        raise sE.UnsupportedDataFormatError(type(X))
