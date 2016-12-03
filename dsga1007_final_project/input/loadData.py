'''
Created on Dec 3, 2016

@author: muriel820
'''
import pandas as pd
import numpy as np

class loadData:
    '''
    classdocs
    '''


    def __init__(self, basicDataFileName, largeCleanedDataFileName):
        '''
        Constructor
        '''
        self.basicData = pd.read_csv(basicDataFileName)
        self.largeData = pd.read_csv(largeCleanedDataFileName)
    
    def getCityNames(self, data):
        self.