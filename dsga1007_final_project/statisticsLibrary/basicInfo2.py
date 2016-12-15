'''
Created on Dec 3, 2016

@author: muriel820
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
from collections import Counter
import collections
from input.loadData import *
from

class basicFunctions():
    '''
    More info about pokemons in certain places, with pokemon go data
    '''
    def __init__(self, pokemonSeries, cityList, continentList):
        '''
        Constructor
        '''
        self.pokemonSeries = pokemonSeries
        self.cityList = cityList
        self.continentList = continentList
    
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
        pokemonRecords = dataframe.loc[dataframe["pokemonId"]==pokemonId]
        return pokemonRecords
   
    def citywideDataframe(self, dataframe, cityName):
        '''return the records of one certain city'''
        citywideRecords = dataframe.loc[dataframe['city'] == cityName]
        return citywideRecords    
    
    def hasItAppearedGlobally(self, dataframe, pokemonId):
            return (pokemonId in dataframe['pokemonId'].unique())
        
    def city_ID_freq(self, dataframe, city_input):
        ''''
        input:
            city name(str)
        return:
            the frequence of all pokemon appear in this city(Series), with pokemonId as index
        '''
        data = self.citywideDataframe(dataframe, city_input)
        ID_freq_count = data['pokemonId'].value_counts()
        ID_freq_count.hist()
        plt.savefig('Frequence of pokemons appear in ' + str(city_input))
        return ID_freq_count
    
    def ID_city_freq(self, dataframe, ID_input):
        ''''
        input:
            pokemon ID(int)
        return:
            the frequence of a given pokemon appear in all cities(Series), with city name as index
        '''
        data = self.pokemonwideDataframe(dataframe, ID_input)
        city_freq_count = data['city'].value_counts()
        city_freq_count.hist()
        plt.savefig('Frequence of cities'+ str(ID_input)+'has appeared in. ' )
        return city_freq_count
    
    def appeared_incity(self, dataframe, ID_input, city_input):
        '''
        input:
            pokemonID(int) and city_name(str)
        return:
            **print** if the pokemon appeared in this city
        '''
        data = self.pokemonwideDataframe(dataframe, ID_input)
        city_freq_count = data['city'].value_counts()
        if str(city_input) in city_freq_count.index:
            return (print('Pokemon ' + str(ID_input) + ' has appeared in ' + str(city_input)+ ' before'))
        else:
            return (print('Pokemon ' + str(ID_input) + ' has not appeared in ' + str(city_input)+ ' before'))
    def appeared_time(self, dataframe, ID_input):
        '''
        input: 
            pokemonID(int) 
        return:
            
            pie chart of this pokemon appear in different time priod
            '''
        data = self.pokemonwideDataframe(dataframe,ID_input)
        time_array = np.array(data['appearedTimeOfDay'])
        time_df = pd.DataFrame({'time':time_array})
        time_freq_count = time_df['time'].value_counts()
        
        #pie chart
        labels = 'night', 'morning', 'afternoon'
        pie(time_freq_count, labels =labels ,autopct='%1.1f%%')
        #save figure as png
        plt.savefig('pie chart of pokemon ' + str(ID_input) + ' showing up periods')
        return time_freq_count
    
    def co_occurance (self, dataframe, ID_input):
    '''
    input:
        pokemonID(int)
    return:
        Five pokemonID(list)'''
        data = self.pokemonwideDataframe(dataframe, ID_input)
        freq_list = []
        result = []
        for i in range(1,152):
            col_name = str('cooc_'+str(i))
            freq = sum(data[col_name])
            freq_list.append(freq)
        maxfive = sort(freq_list)[-5:]
        for i in range(1,6):
            a = freq_list.index(maxfive[-i])
            result.append(a)
        return result
    