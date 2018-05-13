while True:
    print('Enter the shape you want between a circle, rectangle and triangle')
    user_input = input()

    if len(user_input) > 0 and user_input.isalpha():
        if user_input.lower() == 'circle':
            radius = eval(input('Enter the radius here\t'))
            area = radius * (22 / 7)
            print('Area: %.2f' % area)

        elif user_input.lower() == 'rectangle':
            length = eval(input('Enter your length here:\t'))
            width = eval(input('Enter the width here:\t'))
            area = length * width
            print('Area: %.2f' % area)

        elif user_input.lower() == 'triangle':
            base = eval(input('Enter the base here:\t'))
            height = eval(input('Enter the height here:\t'))
            area = height * base * 0.5
            print('Area: %.2f' % area)
        else:
            print('Shape not available!..Choose from the list above')

    else:
        print('Invalid! Try again!')

