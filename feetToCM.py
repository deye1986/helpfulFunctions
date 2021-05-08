def cm(name, feet=0, inches=0): # keyword arguments (x=0) are positioned after required arguments.
    '''Convert imperial measure to metric(feet & inches --> centimeter).'''
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return name, inches_to_cm + feet_to_cm


# print(cm('Dave', 6, 0)) # only values are passed, kwords not required
# print(cm('Dave2', feet=6,)) # the default value for the argument 'inches' is integer:0 line 1

# transfer design to an Object Oriented Programming paradigm.
# this can be converted to a class and adding the function to the class makes it a 'method'.

class Cm_convert: # define a class and name it with Capital letter like nouns
    def __init__(self, ft, inc): # runs everytime an instance of the class is created
        self.ft = ft # instance variables
        self.inc = inc # ''        ''
        

    def convert(self): # functions inside classes are called methods
        '''Convert imperial measure to metric(feet & inches --> centimeter).''' # docstring - useful data

        self.inc_to_cm = self.inc * 2.54 # logic
        self.ft_to_cm = self.ft * 12 * 2.54
        print(self.inc_to_cm + self.ft_to_cm)

print(dir(Cm_convert)) # notice the new method at the end of the list in the terminal output named 'convert'
dave = Cm_convert(6, 0) # feed the parameters/args to variable dave(which is'self=dave' dave.ft=6, dave.inc=0)
dale = Cm_convert(6, 3) # self is now 'dale' seperating this new instance from the other(s)
dave.convert() # run the method 'convert'. important: notice we 'call' the method with '()'
dale.convert() # we call '()' parenthesis

# as Dale is 3 inches taller than Dave, expected output should reflect this in centimeters.


    

