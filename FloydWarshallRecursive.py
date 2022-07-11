V = 4
INF = 9999
k = 0
j = 0
global i 
i = 0

def function_j(dist):
    global j
    global i
    if j>=V:
        i += 1
        j = 0
        return function_i(dist)
        
    if j in range(V):
 
        dist[i][j] = min(dist[i][j],
                         dist[i][k] + dist[k][j]
                         )
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
        return function_j(dist)
        
def function_k(dist):
    global k
    if k>=V:
        return printSolution(dist)
    if k in range(V):
        return function_i(dist)
        
def printSolution(dist):
    print ("The shortest paths between each pair are shown in the matrix below:")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print ("%7s" % ("INF"),end=" ")
            else:
                print ("%7d\t" % (dist[i][j]),end=' ')
            if j == V-1:
                print ()
                
def check_increments():
    print("j, i, k:",j ,i, k)
    return k

                
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]

dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

function_j(dist)


