'''
Created on 17.11.2014

@author: Carsten Schnober
'''
from UserDict import UserDict

class PrefixMap(UserDict):
    '''
    Extends a dict.
    '''
        
    def getPrefixEntries(self, prefix):
        """Return aggregated values of all dictioniary entries that start with the given prefix."""
        result = 0
        for key in self.data:
            if key.startswith(prefix):
                result += self.data[key]
        return result
