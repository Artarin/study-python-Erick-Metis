"""reader two files containes naimal names"""

paths = ['animals//cats.txt', 'animals//dogs.txt']
for path in paths:
    # print (f'\nfile {path}:')
    try:
        with open (path, 'r') as f:
            print (f'\nfile {path}:')
            print (f.read())
    except FileNotFoundError:
        # print (f'file {path} not found')
        pass
    