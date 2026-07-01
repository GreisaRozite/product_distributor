# -*- coding: utf-8 -*-
"""
"""

from optimizer import optimizer

K = {"Eksperimenti_Centrs_1" : 48, "Zinātne_SEB_1" :  42, "Radošums_Āg_1" : 23, "Pētnieki_Centrs_2" : 36, "Gardumi_Āg_2" : 17 , "Pavāri_Centrs_3" : 40, "Eksperimenti_Āg_3" : 27}
Y = {"Strawberry" : 42*4, "Forest fruit" : 54*4, "Strawberry banana" : 60*4, "Natural" : 30*4 }

x = ArithmeticErroroptimal_distribution = optimizer(Y, K) 

distr = x[0]


cases=len(distr)



for i in range(cases): #handle each week seperately
    case=distr[i]
    name=case[0]
    dictionary=case[1]
    print(f"The camp week {name} has:")
    for b in dictionary:
        if dictionary[b] != 0:
            if dictionary[b] == 1: 
                print(f"\t{dictionary[b]} day of {b} flavour")
            else:
                print(f"\t{dictionary[b]} days of {b} flavour")
        else:
            pass
    print(" ")
            
            





