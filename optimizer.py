# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 21:09:53 2026

@author: sabin
"""

from shuffleSorter import shuffleSorter

def optimizer(YOG, KIDS):
    yogEx = {"berry" : 120, "minecraft" : 310, "blueberry" : 200}


    kidsEx = {"experiments" : 40, "science" : 31, "plants" : 20, "animals" : 25}

    #initial run
    resultInit = shuffleSorter(yogEx, kidsEx)
    
    smallestLeftovers = resultInit[1]
    optimalSort=resultInit[0]


    i=0

    while i<1000:
        result = shuffleSorter(yogEx, kidsEx)
        if result[1]<smallestLeftovers:
            optimalSort=result[0]
            smallestLeftovers = result[1]
        else:
            pass
        i+=1
    
    return optimalSort

'''optimizer minimizing leftovers, need to do one maximizing days for each camp so they are as equal as possible'''