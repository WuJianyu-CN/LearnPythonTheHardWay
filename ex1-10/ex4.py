# assign the numbers of cars
cars = 100
# assign the space per car
space_in_a_car = 4.0
# assign the numbers of drivers
drivers = 30
# assign the numbers of passengers
passengers = 90
# calculate the numbers of cars which are not in use
cars_not_driven = cars - drivers
# calculate the numbers of cars in use
cars_driven = drivers
# calculate the whole spaces of all cars can provide
carpool_capacity = cars_driven * space_in_a_car
# calculate the average numbers of passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
