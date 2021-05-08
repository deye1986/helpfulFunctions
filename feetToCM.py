def cm(name, feet=0, inches=0): # keyword arguments (x=0) are positioned after non kwargs.
    '''Convert imperial measure to metric(feet & inches --> centimeter).'''
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return name, inches_to_cm + feet_to_cm


print(cm('Dave', 6, 0))