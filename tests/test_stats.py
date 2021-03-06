from statispy import stats as s
from statispy import statispyError as sE
import pytest
import math
import pandas as pd

valid_data = pd.DataFrame({
    'c1': [0,1,2,3],
    'c2': [1,2,3,4]
})
big_data = pd.DataFrame({
    'c1': list(range(0,10)),
    'c2': list(range(1,11))
})
invalid_data = pd.DataFrame({

    'c1': ['c',1,2,3],
    'c2': [1,2,None,4]
})
invalid_data_2 = [1,2,3,4]

class Test_stats:
    def test_validate(self):
        # invalid data-type
        with pytest.raises(sE.UnsupportedDataFormatError):
            s.validate(invalid_data_2, col = 'c1')
        
        # incosistent data type
        with pytest.raises(sE.InconsistentDataTypeError):
            s.validate(invalid_data, col = 'c1')
        
        # NaN error
        with pytest.raises(sE.ContainsNaNValueError):
            s.validate(invalid_data, weight = 'c2')
        
        # invalid column
        with pytest.raises(sE.MissingColumnError):
            s.validate(valid_data, col = 'c4')
        
        with pytest.raises(sE.MissingColumnError):
            s.validate(valid_data, col = 'c1', weight = 'c8')
    
    def test_mean(self):
        
        # unweighted mean
        _mean = s.mean(valid_data, col = 'c2')
        assert _mean == 2.5

        # weighted mean
        _mean_w = s.mean(valid_data, col = 'c1', weight = 'c2')
        assert _mean_w == 2
        
    
    def test_RMS(self):
    
        rms = s.RMS(valid_data, col = 'c2')
        assert rms == pytest.approx(2.7386, abs=1e-3)

    
    def test_SD(self):
    
        # simple SD
        sdDev = s.SD(valid_data, col = 'c1')
        
        assert sdDev == pytest.approx(1.11803, abs=1e-3)

    def test_variance(self):
        var = s.variance(valid_data, col = 'c2')
        
        assert var == pytest.approx(1.25, abs = 1e-3)
        