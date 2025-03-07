input_a = input('Input the first number: ')
input_b = input('Input the second number: ')
try:
    input_a = int(input_a)
    input_b = int(input_b)
except:
    print('>>Not numbers')
# ==============================================

def exponent_ab(a, b):
    return a ** b

print(f'Answer: {exponent_ab(input_a, input_b)}')
