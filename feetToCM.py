def cm(feet=0, inches=0):
    '''Convert imperial measure to metric(feet & inches --> centimeter).'''
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm


print(cm(6, 0))