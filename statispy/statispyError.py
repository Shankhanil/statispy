class UnsupportedDataFormatError(Exception):
    def __init__(self, datatype):
        self.datatype = datatype
    def __str__(self): 
        return(repr(self.datatype))
        
class MissingColumnError(Exception):
    def __init__(self, col, colList):
        self.col = col
        self.colList = colList