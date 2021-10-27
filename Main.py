from math import ceil
def multiply_table(n,k):
    d = 0 ; l = max(ceil(k/n),1)
    if k==1 and n==1:return 1
    for i in range(l,n+1):
        if k%i==0:d+=1
    return d
