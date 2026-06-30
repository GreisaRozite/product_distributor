# -*- coding: utf-8 -*-
"""
Yoghurt distribution for work
"""

import random

#print("how many types of yoghurts?")
#T = int(input());
#YOG={};

#for i in range(T):
#    print("enter type name")
#    name=input()
#    print("enter amount")
#    amount=int(input())
#    YOG[name]=amount
    
YOG = {"berry" : 120, "minecraft" : 310, "blueberry" : 200}

#print("how many different camps?")
#CAMPS = int(input());

#KIDS={};

#for i in range(CAMPS):
#    print("enter camp name")
#    name = input()
#    print(f"how many people in {name} camp?")
#    people = input()
#    KIDS[name]=int(people)
    

KIDS = {"experiments" : 40, "science" : 31, "plants" : 20, "animals" : 25}
    
totalYOG=0;

for i in YOG:
    totalYOG+=YOG[i]

totalKIDS=0
for i in KIDS:
    totalKIDS+=KIDS[i]
    
approx = round(totalYOG/totalKIDS) # approximate_days_of_YOG_per_camp = yog_per_kid (one yoghurt per day)






'''RULE: one location must have only one type of yoghurt at a time'''



result = []
for i in KIDS:
    partial = []
    partial.append(i)
    result.append(partial)
    
# result = [[exp], [sc], [pl], [an]]

for i in range(len(result)):
    result[i].append({})


# result = [[exp, {}], [sc, {}], [pl, {}], [an, {}]]


  
def shuffle_dict(D):
    P=[]
    for i in D:
        P.append(i)
    random.shuffle(P)
    D2={}
    for i in P:
        D2[i]=D[i]
    return D2

biggestNR=0
for i in KIDS:
    biggestNR=max(biggestNR, KIDS[i])
    
YOGLeft=YOG

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
    
print(result)
print(totalLeft)

        
        
'''
    {'sci': 1, 'pl': 1, 'ani': 1, 'exp': 1}
    
    
result = [[exp], [sc], [pl], [an]]


    
    {'exp': 1, 'ani': 0, 'sci': 0, 'pl': 1}
    {'pl': 1, 'exp': 0, 'ani': 1, 'sci': 1}'''
    
        
  
        
            
        
    
    




    

    









