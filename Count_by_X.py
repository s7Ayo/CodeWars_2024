def count_by(x, n):
    maxval = x*n
    finallist=[]
    finallist.append(maxval)
    for i in range(n,0,-x):
        finallist.insert(0, i)
    return(finallist)

def count_by(x, n):
    finallist = []
    for i in range(x, x*n+1, x):  # Start from x, end at x*n, increment by x
        finallist.append(i)
    return finallist
