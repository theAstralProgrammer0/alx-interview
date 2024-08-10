#!/usr/bin/python3

def gen_list(plist):
    i = 0
    newlist = [1]
    
    for i in range(len(plist) - 1):
        newlist.append(plist[i] + plist[i+1])    
    newlist.append(1)
    return newlist


def pascal_recur(n, plist=None, mlist=None):
    if mlist is None:
        mlist = []
    if plist is None:
        plist = [1]

    mlist.append(plist)
    if n == 1:
        return mlist
    else:
        return pascal_recur(n - 1, gen_list(plist), mlist)

def pascal_triangle(n):
    if n <= 0:
        return [] 
    return pascal_recur(n)
