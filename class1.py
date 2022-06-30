class Restaurant: # class name starts with capital letter
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("restaurant_name : ", self.restaurant_name)
		print("cuisine_type : ", self.cuisine_type)

	def open_restaurant(self):
		print("restaurant is open")


class Users:
	def __init__(self, first_name, last_name):
		self.first = first_name
		self.last = last_name

	def describe_user(self):
		""" To describe personal info of user"""
		print("user First Name", self.first)
		print("user Last Name", self.last )

	def greet_user(self):
		print(f"Greetings {self.first} {self.last}")


if __name__ == "__main__":
	restaurant1 = Restaurant("Black Perl", "multi-cuisine")
	#print(restaurant1.restaurant_name, restaurant1.cuisine_type)
	restaurant1.describe_restaurant()
	restaurant1.open_restaurant()
	restaurant2 = Restaurant("Udupi Veg", "south indian")
	restaurant3 = Restaurant("mast kalander", "north indian")
	restaurant2.describe_restaurant()
	restaurant3.describe_restaurant()
	user1 = Users("Devraju", "Achavalla")
	user1.describe_user()
	user1.greet_user()
	user2 = Users("Rahul", "Kumar")
	user2.describe_user()



	