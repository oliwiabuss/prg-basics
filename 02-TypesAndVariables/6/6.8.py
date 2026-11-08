first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)  
last_letter_code = ord(last)
number_of_letters = last_letter_code - first_letter_code - 1
print(f'Between {first} and {last} is letters {number_of_letters}')
