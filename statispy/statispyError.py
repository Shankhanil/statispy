class UnsupportedDataFormatError(Exception):
    def __init__(self, datatype):
        self.datatype = datatype
    def __str__(self): 
<<<<<<< HEAD
        return(repr(self.datatype))
        
class MissingColumnError(Exception):
    def __init__(self, col, colList):
        self.col = col
        self.colList = colList
=======
        return(repr(self.datatype))
>>>>>>> 3a1699eccffd5772589d7f44f7c51fbfc75d5181
