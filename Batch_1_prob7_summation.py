def summate():
    total = 0
    counter = 10  # countdown, for auxillary purposes
    for _ in range(10):
        number = int(input(f'Input a number ({counter}): '))
        total += number
        counter -= 1
    print(f'The sum of all the numbers is: {total}')
    
summate()