# a compact function is on lines 3 to 5, on lines 9 to 31 a larger script which implements further
# logic and steps to help explain the concept of this further. Builtin methods are applied in both.

def sum_string(a, b):
    '''efficient function for adding two strings and converting back to 'str'.'''
    return str(int(a or 0) + int(b or 0))



# return the sum of two integers returning a string.
def sum_str():
    '''Sum 2 integers and convert to string type for output.'''    
    a = input('First? >>>  ')
    b = input('Second? >>>  ')
    if a == '' and b == '':
        print('0') # two empty parameters return Zero 
        return     
    elif a == '':
        a = 0 # one empty parameter will still need a value eg : '0' + '5' = '5'
    elif b =='':
        b = 0
    a = int(a)
    b = int(b)
    sum = a + b
    sum = str(sum)
    print(sum)
    print(type(sum)) # check it has been changed to a string defined as 'str'
    return
    


while True: # start loop
    sum_str() # looped