class UnsupportedDataFormatError(Exception):
    def __init__(self, datatype):
        self.datatype = datatype
    def __str__(self): 
        return(repr(self.datatype))
        
class InconsistentDataError(Exception):
    def __init__(self, col):
        self.col = col
    
class MissingColumnError(Exception):
    def __init__(self, col, colList):
        self.col = col
        self.colList = colList
        
class InvalidSampleSize(Exception):
    def __init__(self, size):
        self.size = size
        
class InconsistentDataTypeError(Exception):
    def __init__(self, col):
        self.col = col

class ContainsNaNValueError(Exception):
    def __init__(self, col):
        self.col = col
        
class UnknownSamplingMethodError(Exception):
    def __init__(self, error):
        self.error = error
    