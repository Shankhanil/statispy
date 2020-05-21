from statispy import sample as s
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

class Test_sample:
    def test_validate(self):
        # invalid data
        with pytest.raises(sE.UnsupportedDataFormatError):
            s.validate(invalid_data_2, 3)
        
        # invalid size
        with pytest.raises(sE.InvalidSampleSize):
            s.validate(valid_data, len(valid_data) + 1)
            
        with pytest.raises(sE.InvalidSampleSize):
            s.validate(valid_data, 0)
            
        # invalid method
        with pytest.raises(sE.UnknownSamplingMethodError):
            s.validate(valid_data, len(valid_data)-1, method = 'some-unknown-method')
    
    def test_basic_sample(self):
        sample = s.basic_sample(big_data, size = 4)
        assert len(sample) == 4
        
        for i in list(sample.index):
            if (big_data.loc[i] != sample.loc[i]).all():
                assert False
        assert True
        
        sample = s.basic_sample(big_data, method = 'systematic' , size = 4)
        assert len(sample) == 4
        
        sample_index = list(sample.index)
        assert sample_index == [0,3,6,9]