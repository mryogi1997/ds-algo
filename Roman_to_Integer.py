R = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def RToInt(D:int)->int:
    i = 0
    N = len(D)
    result = 0
    while i < N:
        if i + 1 < N:
            if R.get(D[i],-1) >= R.get(D[i+1],-1):
                result = result + R.get(D[i],-1)
            else:
                result = result + R.get(D[i+1],-1) - R.get(D[i],-1)
                i = i + 1
        else:
            result = result + R.get(D[i],-1)
        i = i + 1
    return result
    
print(RToInt('IV'))
