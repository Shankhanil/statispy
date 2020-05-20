from statispy import stats as s
from statispy import statispyError as sE
import pytest,math

class Test_stats:    
    def test_mean(self):
        
        # sample unweighted mean on a list
        sample = list(range(1,6))
        mean = s.mean(sample)
        
        assert mean == 3
        
        # sample weighted mean on a dict
        sample = {
            1: 1,
            2: 2,
            3: 3
        }
        mean = s.mean(sample)
        assert mean == pytest.approx(2.333, abs=1e-3), 'approximate weighted mean is 2.333'
        
        # raise an error if datatype isn't List or dict
        sample = '123'
        with pytest.raises(sE.UnsupportedDataFormatError) :
            s.mean(sample)
    
    def test_RMS(self):
        
        # simple unweighted RMS on list
        sample = list(range(1,6))
        rms = s.RMS(sample)
        
        assert rms == pytest.approx(3.3166, abs=1e-3)

        # raises error on unsupported format
        sample = '123'
        with pytest.raises(sE.UnsupportedDataFormatError):
            s.RMS(sample)
    
    def test_SD(self):
    
        # simple SD
        sample = list(range(1,6))
        sdDev = s.SD(sample)
        
        assert sdDev == pytest.approx(1.4142, abs=1e-3)
        
        # error for unweighted format
        sample = '123'
        with pytest.raises(sE.UnsupportedDataFormatError):
            s.SD(sample)
    

    def test_variance(self):
        sample = list(range(1,6))
        var = s.variance(sample)
        
        assert var == 2
        
        # error for unweighted format
        sample = '123'
        with pytest.raises(sE.UnsupportedDataFormatError):
            s.variance(sample)