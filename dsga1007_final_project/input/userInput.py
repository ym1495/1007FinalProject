import pandas as pd
import numpy as np
import sys

from LoadData import *


class UserChoice:

    """
    This class contains all process that asking user input of choosing cuisine category, cuisine, neighborhood category,
    and neighborhood.
    User could go back or exit follow the instruction.
    """
    def __init__(self):
        self.user_decision = {'Cuisine_Category': None, 'Cuisine': None,
                              'Neighborhood_Category': None, 'Neighborhood': None}
        self.cuisine = Cuisine()
        self.nbhd = Neighborhood()

    def select_pokemon(self):
        while True:
            choice = raw_input('\nHow would like to CHOOSE a cuisine category?\n'
                               'You can type \'back\' to go back.\n'
                               'A. African\n'
                               'B. EastAsian\n'
                               'C. SouthAsian\n'
                               'D. LatinAmerican\n'
                               'E. NorthAmerican\n'
                               'F. European\n'
                               'G. MiddleEastern\n'
                               'H. Cafes\n'
                               'I. Bars\n'
                               'J. Vegan\n'
                               'K. OtherBusiness\n'
                               '---->')
            choice = choice.lower().rstrip().lstrip()
            if choice == 'quit':
                return 'quit'
            elif choice == 'back':
                return 'back'
            elif choice in ['a','b','c','d','e','f','g','h','i','j','k']:
                self.user_decision['Cuisine_Category'] = self.cuisine.cuisine_category[choice]
                return 'selected'
            else:
                print 'Invalid Input. Please enter again.\n'
    
    
