# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:03:55 2021

@author: matvi
"""

n_pot=[]
n_list=[]
save=[]
n=1
boh=10
while n<=boh:
    n_pot.append((n-1)**3)
    n_pot_str=str(n_pot[n])
    n_list.append(n_pot_str)
    n+=1


n=1
flag=0
for n in range(1,boh):
  perm=0
  save.clear()
  
  for i in range(n,boh):
     if perm<5:
        if (len(n_pot_str[i]) != len(n_pot_str[n])):
            pass
        elif n_pot_str[i]==n_pot_str[n]:
            pass
        elif sorted(n_pot_str[i])==sorted(n_pot_str[n]):
            perm=perm+1
            save.append(n_pot_str[i])
     else:
        flag=1
        result=save
        break
  if flag==1:
    break
  else:
    pass


print(result)