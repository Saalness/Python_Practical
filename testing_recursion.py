V = 4
INF = 9999
k = 0
j = 0
global i 
i = 0
dist = 0



"""def floydWarshall(graph):
    
    return function_j(dist)"""

def function_j(dist):
    global j
    global i
    if j>=V:
        print("j is ", j)
        i += 1
        j = 0
        return function_i(dist)
        
    if j in range(V):
 
        print(dist)
        j += 1
        return function_j(dist)

def function_i(dist):
    global i
    global k
    if i>=V:
        k += 1
        i = 0
        return function_k(dist)
    if i in range(V):
        print("i is ", i)
        return function_j(dist)
        
def function_k(dist):
    global k
    if k>=V:
        return print(dist)
    if k in range(V):
        return function_i(dist)            


function_j(dist)

"""floydWarshall(graph)"""
