# fibonacci function - classic computer programmers problem

# for fibonacci.
def forfibon():
    n = int(input('fibonacci >>>'))
    a =-1
    b = 1
    print('fib series is ==')
    for i in range(1, n+1):
        c = a + b
        print (c, end=' ')
        a = b
        b = c
    print()
    
# while fibonacci. 

def fibonacci(n): # define the function and name it so you remember what it does 5 years from now
    '''Fibonacci sequence up to the n'th number''' # get used to writing docstrings
    a, b = 0, 1 # set up the logic for first 2 values in the fibonacci sequence
    while a < n: # implements a counter in to the logic
        print(a, end=' ') # uses one line in the terminal rather than multiple
        a, b = b, a+b # fibonaccis logic, with embedded counter for the while loop
    print() # resets the new line 
    
# fibonacci(3000) # run fibonacci function up to the n'th number which we have decide is 3000
fibonacci(100)