from random import randint
class Die():
    'base roll cube class'
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

six_edges_cube = Die(6)
ten_edges_cube = Die(10)
twenty_edges_cube = Die(20)
cubes = [six_edges_cube, ten_edges_cube, twenty_edges_cube]
print(' '.join([str(i) for i in cubes]))
for cube in cubes:
    print (f"now rolls {str(cube)} press 'enter' to continue")
    k = input()
    for _ in range (10):
        cube.roll_die()