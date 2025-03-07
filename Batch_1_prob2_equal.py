input_a = input('Input the first number: ')
input_b = input('Input the second number: ')
try:
    input_a = int(input_a)
    input_b = int(input_b)
except:
    print('>>Not numbers')
# ==============================================

def compare_ab(a, b):
    if a == b:
        return 'Equal'
    else:
        return 'Not Equal'

print(f'Answer: {compare_ab(input_a, input_b)}')
