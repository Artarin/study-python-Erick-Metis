path = 'text_files\\learning_python.txt'

print('open all file:')

with open (path) as file_object:
    contens = file_object.read()
print (contens, '\n')


print('open file by lines:')

with open (path) as file_object:
    for line in file_object:
        print (line.rstrip())
print()
print('open file in list:')

with open (path) as file_object:
    lines = file_object.readlines()

for i in range(len(lines)):
#     print (line.rstrip())
    lines[i] = lines[i].replace('python', 'C')
    

# print (''.join([str(i) for i in lines]))

print(''.join(lines))


