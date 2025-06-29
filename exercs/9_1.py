class Restaurant():
    """Modelando um restaurante"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    

    def describe_restaurant(self):
        """Descreve o restaurante"""
        print(f'Hello, we are {self.restaurant_name}'\
                f' and our cuisine type is {self.cuisine_type}.')
        
    
    def open_restaurant(self):
        """Informa que o restaurante está aberto"""
        print(f'Our restaurant {self.restaurant_name} is open.')


    def set_number_served(self, number_served):
        """Define um número de pessoas atendidas"""
        if number_served >= 0:
            self.number_served = number_served
        else:
            print('Number served cannot be negative.')


    def increment_number_served(self, served):
        """Incrementa o número de pessoas servidas"""
        self.number_served += served
        

restaurant = Restaurant('pizza hut', 'pizzeria')

print(f'The name of my restaurant is {restaurant.restaurant_name}.')
print(f'The cuisine type of my restaurant is {restaurant.cuisine_type}')
print()
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f'Number served: {restaurant.number_served}')
print()
restaurant.set_number_served(10)
print(f'Update number served: {restaurant.number_served}')

restaurant.increment_number_served(7)
print(f'Total number served: {restaurant.number_served}')

