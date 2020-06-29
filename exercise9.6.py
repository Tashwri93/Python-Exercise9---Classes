class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
      long_name =  "This restaurant is called " + self.restaurant_name + " This type of cuisine is " + self.cuisine_type
      return long_name.title()
    
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")


class IceCreamStand(Restaurant):
    
      def __init__(self,restaurant_name,cuisine_type):
          super().__init__(restaurant_name,cuisine_type)
          self.flavours = []

      def ice_cream_flavour(self):
          print("\nThe ice-cream flavours we have are: ")
          for flavours in self.flavours:
              print(flavours.title())


ice_cream_restaurant = IceCreamStand('creams', 'dessert')
ice_cream_restaurant.flavours = ['vanilla','strawberry','banana','chocolate']

print(ice_cream_restaurant.describe_restaurant())
ice_cream_restaurant.ice_cream_flavour()
    
