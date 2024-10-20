def FindLeaders(N: list) -> list:
    L = []
    Len = len(N)
    
    # Start with the last element as the initial leader
    max_from_right = N[-1]
    L.append(max_from_right)
    
    # Traverse the list from right to left
    for i in range(Len-2, -1, -1):
        if N[i] >= max_from_right:
            max_from_right = N[i]
            L.append(N[i])
    
    # Reverse to maintain the order of leaders from left to right
    return L[::-1]

print(FindLeaders([16, 17, 4, 3, 5, 2]))
