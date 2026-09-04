# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:03:55 2021

@author: matvi
"""
num=([1,1])
tot=0

i=1
while num[i]<4000000:
    num.append(num[i]+num[i-1])
    i+=1
    
for n in num[:-1]:
    if n%2==0:
        tot=tot+n

print(tot)