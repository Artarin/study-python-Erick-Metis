class Restaraunt():
    'restaraunt class'
    def __init__(self, restaraunt_name, cuisine_type):
        self.restaraunt_name = restaraunt_name
        self.cuisine_type = cuisine_type
    
    def open_restaraunt(self):
        print (f"Restaraunt {self.restaraunt_name} now open")

    def describe_restaraunt(self):
        print (self.restaraunt_name)
        print (self.cuisine_type)

# restaraunt = Restaraunt('MCdonalds', 'fastfood')

# restaraunt.open_restaraunt()
# restaraunt.describe_restaraunt()
class IceCreamStand(Restaraunt):
    def __init__(self, restaraunt_name, cuisine_type):
        super().__init__(restaraunt_name, cuisine_type)
        self.flavors = ['belochka', 'ermoshka', 'korovka iz karenovki']
    
    def listing_icecream(self):
        print (self.flavors)

# IceCreamStand = IceCreamStand('MyRest','Icecream rest')
# IceCreamStand.listing_icecream()
# IceCreamStand.open_restaraunt()

