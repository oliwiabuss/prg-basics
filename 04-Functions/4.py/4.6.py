def day_name(day_number):
    result = ''
    if day_number == 1:
        result = 'poniedzialek'
    elif day_number == 2:
        result = "wtorek"
    elif day_number == 3:
        result = "sroda"
    elif day_number == 4:
        result = 'czwartek'
    elif day_number == 5:
        result = 'piatek'
    elif day_number == 6:
        result = "sobota"
    elif day_number == 7:
        result = "niedziela"
    elif day_number >7:
        print = "nie istnieje"
        
    return result

# Function usage
print('The name of day 9 in the week is', day_name(9))
print('The name of day 3 in the week is', day_name(3))
print('The name of day 7 in the week is', day_name(7))