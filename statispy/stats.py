from statispy import statispyError as sE
import math
import random
import pandas as pd
def __init__():
    pass
    
def validate(data, col = None, weight = None):
    if not isinstance(data, pd.DataFrame):
        raise sE.UnsupportedDataFormatError(type(data))
    
    colList = data.columns
    if col != None:
        if col not in colList:
            raise sE.MissingColumnError(col, colList)
        
#        print(data[col].isnull().any())
        
        if data[col].isnull().any():
            raise sE.ContainsNaNValueError(col)
        
        if data[col].dtypes == 'object':
            raise sE.InconsistentDataTypeError(col)

        if not data[col].dtypes == 'int64' and not data[col].dtypes == 'float64':
            raise sE.UnsupportedDataFormatError(data[col].dtypes)
    if weight != None:
        if weight not in colList:
            raise sE.MissingColumnError(col, colList)
        
#        print(data[weight].isnull().any())
        
        if data[weight].isnull().any():
            raise sE.ContainsNaNValueError(weight)
        
        if data[weight].dtypes == 'object':
            raise sE.InconsistentDataTypeError(weight)

        if not data[weight].dtypes == 'int64' and not data[weight].dtypes == 'float64':
            raise sE.UnsupportedDataFormatError(data[weight].dtypes)
        if not data[weight].dtypes == 'int64' and not data[weight].dtypes == 'float64':
            raise sE.UnsupportedDataFormatError(data[weight].dtypes)

def mean(data, col, weight = None):
    
    validate(data, col, weight)

    _sum = 0
    
    if weight == None:
        _sum = sum(data[col])
        return _sum/len(data[col])
    else:
        for i in data.index:
            _sum += data[col].iloc[i]*data[weight].iloc[i]
        return _sum/sum(data[weight])

def RMS(data, col):
    validate(data, col)
    
    sum_sq = 0
    for i in data.index:
        sum_sq += data[col].iloc[i]**2
    mean_sq = sum_sq/len(data[col])
    return math.sqrt(mean_sq)
    
def variance(data, col):
    # if isinstance(X, list):
    validate(data, col)
    _mean = mean(data, col)
    _sum = 0
    for i in data.index:
        _sum += (data[col].iloc[i] - _mean)**2
    return _sum/len(data[col])

def SD(data, col):
    # if isinstance(X, list):
    validate(data, col)
    return math.sqrt(variance(data, col))
