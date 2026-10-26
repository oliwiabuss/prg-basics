def oceny(punkty):
    grande = ""
    if punkty >= 18:
        grande = 'excellent'
    elif punkty >= 14:
        grande = "good"
    elif punkty >=10:
        grande = "satisfactory"
    elif punkty <10:
        grande = "fall"

    return grande 

test_result = 18
final_grande = oceny(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grande}')