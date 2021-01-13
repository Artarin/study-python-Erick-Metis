def addition_two_num():
    """ addition two numbers"""
    print ('this program do addition of two numbers\n')
    try:
        first_number = int(input('enter first number:  '))
        second_number = int(input('enter second number:  '))
        answer = first_number + second_number
    except ValueError:
        print ('\nYou must enter Number, not characters!\n')
    else:
        print (answer)


while True:
    addition_two_num()
