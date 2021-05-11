# convert farenheit to celcius and output result to the terminal. dave ikin

def far2cel():
    '''Convert farenheit to celcius in terminal'''
    
    fahrenheit = int(input("Enter a temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5.0/9.0

    print ("Temperature:", fahrenheit, "Fahrenheit = ", celsius, "degrees celcius")

far2cel()