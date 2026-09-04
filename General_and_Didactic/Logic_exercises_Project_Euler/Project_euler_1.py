# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:03:55 2021

@author: matvi
"""
tot=0
num[0]=1
num[1]=1
i=2
while num<4000000:
    num[i]=num[i-1]+num[i-2]
        i+=1
for n in num:
    if n%2==0:
        tot=tot+n

print(pick)