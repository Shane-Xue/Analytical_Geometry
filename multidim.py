#multidementional version of basicly the same stuff

def Point():
    def __init__(self,coords):
        """coords is a list"""
        self.coords=coords
    
    def __eq__(self,other):
        return (self.coords=other.coords)
    
    def __ne__(self,other)
        return !(self==other)
    
    
