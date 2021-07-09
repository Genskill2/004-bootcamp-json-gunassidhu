# Add the functions in this file
import json
from math import sqrt

def load_journal(file_name):
    f = open(file_name)
    j = json.load(f)
    f.close()
    return j
    # pass

def compute_phi(file_name, event):
    j = load_journal(file_name)
    n11 = 0
    n00 = 0
    n10 = 0
    n01 = 0
    n1x = 0
    n0x = 0
    nx1 = 0 
    nx0 = 0
    
    for i in j:
        a = event in i["events"]
        b = i["squirrel"]
        if(a == True and b == True):
            n11+=1
        elif(a == False and b == False):
            n00+=1
        elif(a == True and b == False):
            n10+=1
        elif(a == False and b == True):
            n01+=1
        
        if(a == True):
            n1x+=1
        elif(a == False):
            n0x+=1
        if(b == True):
            nx1+=1
        elif(b == False):
            nx0+=1
    phi = (n11 * n00 - n10 * n01) / sqrt(n1x * n0x * nx1 * nx0)

    return phi
    # pass

def compute_correlations(file_name):
    j = load_journal(file_name)
    dic = {}
    for i in j:
        for k in i["events"]:
            if(k not in dic.items()):
                dic[k] = compute_phi(file_name,k)
    return dic
    # pass

def diagnose(file_name):
    dic = compute_correlations(file_name)
    maxevent = ""
    minevent = ""
    mini = 5
    maxi = -5
    for i in dic.keys():
        if(dic[i] > maxi):
            maxevent = i
            maxi = dic[i]
        if(dic[i] < mini):
            minevent = i
            mini = dic[i]
    # pass
    return maxevent,minevent
