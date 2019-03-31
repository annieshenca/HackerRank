def fibonacci(n):
    # Write your code here.
    d = dict() # Create a hash table to keep track of records.
    d[0] = 0   # Init 0 and 1
    d[1] = 1
    # Loop n from start to finish.
    # Range start from 2 because 0 and 1 are already included.
    # range(n+1) becasue loop through needs to include the number n.
    for num in range(2, n+1):
        d[num] = d[num-1] + d[num-2]

    # Return the desired fib(n)
    return d[n]

n = int(input())
print(fibonacci(n))
