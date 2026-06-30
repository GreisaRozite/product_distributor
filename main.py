# -*- coding: utf-8 -*-
"""
"""

from optimizer import optimizer

K = {"Eksperimenti_Centrs_1" : 48, "Zinātne_SEB_1" :  42, "Radošums_Āg_1" : 23, "Pētnieki_Centrs_2" : 36, "Gardumi_Āg_2" : 17 , "Pavāri_Centrs_3" : 40, "Eksperimenti_Āg_3" : 27}
Y = {"Strawberry" : 42*4, "Forest fruit" : 54*4, "Strawberry banana" : 60*4, "Natural" : 30*4 }

optimal_distribution = optimizer(Y, K) 






