# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 21:09:53 2026

@author: sabin
"""

from shuffleSorter import shuffleSorter

def optimizer(YOG, KIDS):

    #initial run
    resultInit = shuffleSorter(YOG, KIDS)
    
    smallestLeftovers = resultInit[1]
    optimalSort=resultInit[0]


    i=0

    while i<1000:
        result = shuffleSorter(YOG, KIDS)
        if result[1]<smallestLeftovers:
            optimalSort=result[0]
            smallestLeftovers = result[1]
        else:
            pass
        i+=1
        
    result = [optimalSort, smallestLeftovers]
    
    return result

'''optimizer minimizing leftovers, need to do one maximizing days for each camp so they are as equal as possible'''