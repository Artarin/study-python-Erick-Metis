import copy
class SomePeople():
    """describe people"""
    def __init__(self, some_integer):

        self.some_integer = some_integer

Antonns = SomePeople(1)
some_list = [copy.copy(Antonns)]
Antonns.some_integer = 2
print (some_list[0].some_integer)
assert some_list[0].some_integer == 1


