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
        self.basicData.set_index('Pokemon No.', inplace=True, drop=False)
        self.largeData = pd.read_csv(largeCleanedDataFileName)
    
    def listPokemonNameswithID(self):
        '''return a series of Pokemon names, with pokemonID as index'''
        self.nameList = self.basicData['Name']
        return  self.nameList
    
    def pokemonwideDataframe(self, pokemonId):
        '''return the records of one certain city'''
        pokemonRecords = self.largeData[self.largeData["pokemonId"]==pokemonId]
        return pokemonRecords
    

    def getCityNames(self):
        '''return a numpy ndarray of cities'''
        self.cityList = self.largeData['city'].unique()
        return self.cityList
    
    def citywideDataframe(self, cityName):
        '''return the records of one certain city'''
        citywideRecords = self.largeData[self.largeData["city"]==cityName]
        return citywideRecords
    
    def getContinentNames(self):
        '''return a numpy ndarray of cities'''
        self.continentList = self.largeData['continent'].unique()
        return self.continentList
    
    def continentwideDataframe(self, continent):
        '''return the records of one certain city'''
        continentwideRecords = self.largeData[self.largeData["continent"]==continent]
        return continentwideRecords
    
