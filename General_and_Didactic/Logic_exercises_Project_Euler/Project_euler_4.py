# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:03:55 2021

@author: matvi
"""
num=([1,1])
tot=0

n =range(1,999)
all_all= []
all_molt=[]
for num in n:
    for num2 in n:
        num_molt=num*num2
        num_molt_str=str(num_molt)
        if num_molt_str==num_molt_str[::-1]:
            all_all.append([num_molt,num,num2])
            all_molt.append([num_molt])

print(max(all_molt))