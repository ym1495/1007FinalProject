'''
Created on Dec 3, 2016

@author: muriel820
'''
import numpy as np
import pandas as pd
from input.loadData import *

class basicFunctions():
    '''
    More info about pokemons in certain places, with pokemon go data
    '''
    def __init__(self, str):
        '''
        Constructor
        '''
        str = 'want more info?'
    
    def listPokemonIdsAppeared(self,dataframe):
        pokemonIdList = dataframe['pokemonId'].unique()
        return pokemonIdList
    
    def getCityNames(self,dataframe):
        '''return a numpy ndarray of cities'''
        cityList = dataframe['city'].unique()
        return cityList
    
    def getContinentNames(self,dataframe):
        '''return a numpy ndarray of continents'''
        continentList = dataframe['continent'].unique()
        return continentList
    
    def pokemonwideDataframe(self, dataframe, pokemonId):
        '''return the records of one certain pokemon'''
        pokemonRecords = dataframe[dataframe["pokemonId"]==pokemonId]
        return pokemonRecords
   
    def citywideDataframe(self, dataframe, cityName):
        '''return the records of one certain city'''
        citywideRecords = dataframe[dataframe["city"]==cityName]
        return citywideRecords
    def continentwideDataframe(self, dataframe, continent):
        '''return the records of one certain city'''
        continentwideRecords = dataframe[dataframe["continent"]==continent]
        return continentwideRecords
    def hasItAppearedIn(self, pokemonId, place):
        if place in {'the world', 'global','globally','globaly','around the world'}:
            return (pokemonId in dataframe['pokemonId'].unique())
        elif place in dataframe['pokemonId'].unique()