# fibonacci function - classic computer programmers problem explained by dave ikin

def fibonacci(n): # define the function and name it so you remember what it does 5 years from now
    '''Fibonacci sequence up to the n'th number''' # get used to writing docstrings
    a = 0 # set up the start of the logic
    b = 1 # as above ^
    while a < n: # run code below until this statement becomes invalid which occurs when a becomes more than n
        a = b # this is a counter, the loop stops when the condition is met
        b = a + b # fibonacci's logic
        print(a, end=' ') # end: print() method- value defaults to newline, ' ' keeps output on one line
    print() # this resets the value passed to the 'end' method back to \n (newline), terminal says 'fanks'

fibonacci(3000) # type the name of the function and the argument in the () lets do it! (enthusiasm)