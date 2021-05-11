# convert pounds to metric kilograms in float data type. dave ikin
# 14 pounds in a stone
# one pound == 0.453592 kilograms

def lb_to_kg(stones=0.0, pounds=0.0):
    '''Converts stones to kilograms, enter stones at first prompt, pounds at second prompt'''
    stones = input("Enter Stones, enter pounds after. ")
    pounds = input("Now enter pounds: ")
    pounds = float(pounds)
    stones = float(stones)

    convertstones = (14.0 * 0.453592) * stones
    convertpounds = pounds * 0.453592

    result = convertstones + convertpounds

    print(result,"KG")

lb_to_kg()
