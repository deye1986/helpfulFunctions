# fibonacci function - classic computer programmers problem explained by dave ikin

def fibonacci(n): # define the function and name it so you remember what it does 5 years from now
    '''Fibonacci sequence up to the n'th number''' # get used to writing docstrings
    a, b = 0, 1 # set up the logic for first 2 values in the fibonacci sequence
    while a < n: # implements a counter in to the logic
        print(a, end=' ') # uses one line in the terminal rather than multiple
        a, b = b, a+b # fibonaccis logic, with embedded counter for the while loop
    print() # resets the new line 
    
fibonacci(3000) # run fibonacci function up to the n'th number which we have decide is 3000