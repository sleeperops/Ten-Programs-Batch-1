def greater_number(a, b):  # what?
    if a > b:
        return str(a)
    elif a == b:
        return 'Equal'
    else:
        return str(b)


def compare_ab(a, b):
    if a == b:
        return 'Equal'
    else:
        return 'Not Equal'


def sum_ab(a, b):
    return a + b


def product_ab(a, b):
    return a * b


def quotient_ab(a, b):
    if a == 0 or b == 0:
        return 'Undefined'
    else:
        return a / b


def exponent_ab(a, b):
    return a ** b


def summate():
    total = 0
    counter = 10  # countdown, for auxillary purposes
    for _ in range(10):
        number = int(input(f'Input a number ({counter}): '))
        total += number
        counter -= 1
    print(f'Sum of all the numbers is: {total}')


def odd_numbers():
    odd_num_count = 0
    counter = 10  # countdown, for auxillary purposes
    for _ in range(10):  # Asks for a number ------------------------
        number = int(input(f'Input a number ({counter}): '))
        if number % 2 == 1:  # if odd, add 1 to the total amount of odd numbers and continue
            odd_num_count += 1
        counter -= 1  # countdown, for auxillary purposes
    print(f' There are {odd_num_count} odd numbers')


def all_even():
    for num in range(101):
        if num % 2 == 0:
            print(num)
        else:
            continue


def no_zero():
    for num in range(101):
        if num % 10 == 0:
            continue
        else:
            print(num)


# user interacting with program ========================
function_dict = {'Prog 1: Print the greater of 2 numbers': greater_number,
                 'Prog 2: Check if 2 numbers are equal': compare_ab, 'Prog 3: Sum of 2 Numbers:': sum_ab,
                 'Prog 4: Product of 2 Numbers': product_ab,
                 'Prog 5: Quotient of 2 Numbers': quotient_ab, 'Prog 6: First Number raised to the Second': exponent_ab,
                 'Prog 7: Summation of 10 Numbers': summate, 'Prog 8: Odd number counter': odd_numbers,
                 'Prog 9: All even numbers from 0 - 100': all_even,
                 'Program 10: All numbers from 0-100 except those ending in zero': no_zero}
function_list = [greater_number, compare_ab, sum_ab, product_ab, quotient_ab, exponent_ab, summate, odd_numbers,
                 all_even, no_zero]

# main loop =============================================
while True:
    for function in function_dict:  # displays all the function
        print(function)
    # function selection
    print('')
    user_input = input('Pick the number of the program of your choice (// to exit): ')
    if user_input == '//':  # exit program
        break
    try:
        user_input = int(user_input)
    except:
        print('>>Not a number')
        continue
    user_input -= 1  # to deal with 0 base
    if user_input >= 0 and user_input < 6:  # for functions with special parameters
        input_a = input('Input the first number: ')
        input_b = input('Input the second number: ')
        try:
            input_a = int(input_a)
            input_b = int(input_b)
        except:
            print('>>Not numbers')
            continue
        print(f'Answer: {function_list[user_input](input_a, input_b)}')  # calls the function based on user input

    elif user_input > 5 and user_input <= 10:  # for functions with no special parameters
        function_list[user_input]()  # calls the function based on user input

    else:
        print('>>Out of index')

    # exit / continue program
    to_continue = input("Continue? (any key or 'n' to exit): ")
    if to_continue.lower() == 'n':
        break
    else:
        continue

