# -*- coding: utf-8 -*-
"""
Yoghurt distribution for work


Fakts:
Brīnumeksperimenti - Brīnumzeme Centrs 	29.06.2026 - 03.07.2026 (44 +4) 
A 19 +2
B 25 +2
Brīnumradošums - Brinumzeme Āgenskalns 	29.06.2026 - 03.07.2026 	21 +2
Brīnumzinātne - SEB 	29.06.2026 - 03.07.2026 	(38+4)

Prognoze:
Brīnumpētnieki - Brīnumzeme Centrs 	06.07.2026 - 10.07.2026 	34
Brīnumgardumi - Brinumzeme Āgenskalns 	06.07.2026 - 10.07.2026 	15

Brīnumpavāri - Brīnumzeme Centrs 	13.07.2026 - 17.07.2026 	38
Brīnumeksperimenti - Brinumzeme Āgenskalns 	13.07.2026 - 17.07.2026 	25

"""

print("how many types of yoghurts?")
T = int(input());
YOG={};

for i in range(T):
    print("enter type name")
    name=input()
    print("enter amount")
    amount=int(input())
    YOG[name]=amount
    
'''YOG = {berry : 120, minecraft : 310}'''

print("how many different camps?")
CAMPS = int(input());

KIDS={};

for i in range(CAMPS):
    print("enter camp name")
    name = input()
    print(f"how many people in {name} camp?")
    people = input()
    KIDS[name]=int(people)
    

'''KIDS = {experiments : 40, science : 31}'''
    
totalYOG=0;

for i in YOG:
    totalYOG+=YOG[i]

totalKIDS=0
for i in KIDS:
    totalKIDS+=KIDS[i]
    
approx = round(totalYOG/totalKIDS) # approximate_days_of_YOG_per_camp = yog_per_kid

# A 3               B 2
#         500
# 500/5 = 100
# 250 per camp
    

    









