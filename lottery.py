from random import choice
# win_letters = []
numbers_symbols = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e')

# for i in range (4):
#     win_letters.append(choice(numbers_symbols))
    
# print ("The winner is ticket:", ' '.join([str(i) for i in win_letters]))
my_ticket = '1234'
i=0
win_ticket = str()
while my_ticket != win_ticket:
    win_ticket = str()
    for _ in range (4):
        win_ticket += choice(numbers_symbols)
    i += 1
    print (win_ticket)
    if i >= 1000000:
        print ('to many tries')
        break
print (f'Number of tryes: {i}')


