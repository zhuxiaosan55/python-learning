class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        number_served = 0

    def describe_restaurant(self):
        print("my restaurant's name is "+self.restaurant_name.title()+".")
        print("my restaurant's cuisine_type is "+self.cuisine_type.title()+".")
        print("this restaurant served "+str(self.number_served)+" people.")

    def open_restaurant(self):
        print("The restaurant is opening")

    def set_number_served(self, people):
        if people >= self.number_served:
            self.number_served = people
        else:
            print("You can't roll back served people")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['straberry', 'lemon']

    def show_icecream(self):
        print(self.flavors)


my_restaurant = Restaurant("jiaoziwang", "chiness_food")
my_restaurant.number_served = 23
my_restaurant.describe_restaurant()
my_restaurant.set_number_served(50)
my_restaurant.set_number_served(40)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_icecream = IceCreamStand('madanload', 'quike food')
my_icecream.show_icecream()
