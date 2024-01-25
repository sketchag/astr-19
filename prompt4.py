class MyFavoriteAnimal:
	def __init__(squirrel):
		squirrel.length_arm = 3.218
		squirrel.length_leg = 4.478
		squirrel.eye_number = 2
		squirrel.tail = True
		squirrel.furry = True
	

	def PrintMyFavorite(squirrel):
		print(f"My favorite animal is squirrel")
		print(f"Length of arms: {squirrel.length_arm}")
		print(f"Length of legs: {squirrel.length_leg}")
		print(f"Number of eyes: {squirrel.eye_number}")
		print(f"Does it has a tail?: {squirrel.tail}")
		print(f"Is it furry?: {squirrel.furry}")


if __name__ == "__main__":
    a = MyFavoriteAnimal()
    a.PrintMyFavorite()
