class UnsupportedDataFormatError(Exception):
    def __init__(self, datatype):
        self.datatype = datatype
    def __str__(self): 
        return(repr(self.datatype))