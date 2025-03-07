input_a = input('Input the first number: ')
input_b = input('Input the second number: ')
try:
    input_a = int(input_a)
    input_b = int(input_b)
except:
    print('>>Not numbers')
# ==============================================

def greater_number(a, b): 
    if a > b:
        return str(a)
    elif a == b:
        return 'Equal'
    else:
        return str(b)

print(f'Answer: {greater_number(input_a, input_b)}')