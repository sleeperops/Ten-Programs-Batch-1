input_a = input('Input the first number: ')
input_b = input('Input the second number: ')
try:
    input_a = int(input_a)
    input_b = int(input_b)
except:
    print('>>Not numbers')
# ==============================================

def quotient_ab(a, b):
    if a == 0 or b == 0:
        return 'Undefined'
    else:
        return a / b

print(f'Answer: {quotient_ab(input_a, input_b)}')
