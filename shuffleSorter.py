# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 20:54:06 2026

@author: sabin
"""
import random
  
def shuffle_dict(D):
    P=[]
    for i in D:
        P.append(i)
    random.shuffle(P)
    D2={}
    for i in P:
        D2[i]=D[i]
    return D2

def shuffleSorter(YOG, KIDS):
    result = []
    for i in KIDS:
        partial = []
        partial.append(i)
        result.append(partial)
        
    # result = [[exp], [sc], [pl], [an]]

    for i in range(len(result)):
        result[i].append({})


    # result = [[exp, {}], [sc, {}], [pl, {}], [an, {}]]
        
    totalYOG=0;

    for i in YOG:
        totalYOG+=YOG[i]

    

    biggestNR=0
    for i in KIDS:
        biggestNR=max(biggestNR, KIDS[i])
        
    YOGLeft=YOG.copy() 
    '''cause of bug! needs to be YOGLeft = YOG.copy() not YOGLeft = YOG .... need to explore why though'''

    for i in YOG: 
        partial={}
        number=YOG[i]
        while number > biggestNR: # keeps looping until cant anymore
            KIDS2 = shuffle_dict(KIDS)
            for j in KIDS2: # loops over each camp in succesion for maximum variation of flavours in each 
                partial[j]=0 # initialize zero days of i yoghurt per j camp
                if number-KIDS2[j]>=0: #120-40    i = berry  j = experiments
                    partial[j]+=1
                    number=number-KIDS2[j]
                else:
                    pass
        ## i = yoghurt type
        ## partial = {camp : nr of days of this yoghurt it can have}
        for k in range(len(result)): ## i[0] = camp = exp
            amounts=result[k][1]
            camp = result[k][0]
            if camp in partial: 
                amounts[i]=partial[camp]
                result[k][1] = amounts
        YOGLeft[i]=number
       

    # result = [[exp, {}], [sc, {}], [pl, {}], [an, {}]]

    # for 0 1 2 3
    # amounts = {}
    # camp = exp
    # if exp in partial
    # amounts[i]=partial[camp]
    #
        
    totalLeft=0
    for i in YOGLeft:
        totalLeft+=YOGLeft[i]
        
        
    realResult=[result, totalLeft]
    return realResult
    
    
'''possible bug - can only run once, changes og YOG values when minusing. no effect when called as function with different inputs each time'''
'''FIXED!'''
