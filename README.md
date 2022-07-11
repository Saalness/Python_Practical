# Python_Practical
Floyd Warshall Recursive Algorithm


This program takes a matrix and checks for the shortest path between each pair of vertices

j  is the smallest loop that is called the most
 
i  is the middle loop that is called second most

k  is the biggest loop that is called the least (4 times in this case)

since V is 4 in this example

in the base case of each recursive function, the function will stop calling itself, it will reset to zero and increment the next variable.

the second if statement in each function is when the variable is in range of 4 (aka less than 4) and the function will call itself after executing that part of code. In j it compares the lengths of the edges (the important part of the code, which remains unchanged).

How the program works:

graph and dist are  initialised at the bottom, then function_j is called. It calls itself 4 times then calls i which calls j 4 times then i calls k which calls i 4 times. Once that is done k calls the print function.


*note: The variables are defined inside as global to avoid errors