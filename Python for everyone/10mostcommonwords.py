# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:06:29 2019

@author: Dat Nguyen
"""

name = input ('please enter file name: ')
fh = open (name)

mydict = dict ()
mylist = list ()

for line in fh:
    words = line.split()
    for word in words:
        mydict [word] = mydict.get(word, 0) + 1

for k,v in mydict.items ():
    newtupe = (v,k)
    mylist.append(newtupe)

mylist = sorted(mylist, reverse = True )    
for k,v in mylist [:10]:
    print (v,k)
    