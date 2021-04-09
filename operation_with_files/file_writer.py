# write one string to file in path
path = 'text_files//guest.txt'
with open (path, 'w') as file_object:
    file_object.write('123\n')

# save user's greeting to file

while True:
    path = 'text_files//guest_book.txt'
    name_user = input('Enter You name or enter to quit: ')
    if len(name_user) == 0:
        break
    greeting = (f"Hello m'r or m's {name_user}")
    print (greeting)
    with open(path, 'a') as file_object:
        file_object.write(greeting+'\n')

#user poll

while True:
    path = 'text_files//user_answers.txt'
    answer = input ('tip, why you like programming or press enter:  ')
    if len(answer) == 0:
        break
    with open(path, 'a') as file_object:
        file_object.write(answer + '\n')

