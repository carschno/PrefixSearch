'''
Created on 17.11.2014

@author: Carsten Schnober
'''
from UserDict import UserDict
import re


class PrefixDict(UserDict):
    '''
    Extends a dict to aggregate methods matching certain conditions.
    '''
        
    def getPrefixEntries(self, prefix):
        """Return aggregated values of all dictioniary entries that start with the given prefix."""
        result = 0
        for key in self.data:
            if key.startswith(prefix):
                result += self.data[key]
        return result
    
    def getRegexEntries(self, pattern):
        regex = re.compile(pattern)
        result = 0
        for key in self.data:
            if regex.match(key):
                result += self.data[key]
        return result
