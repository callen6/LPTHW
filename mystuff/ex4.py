cars = 100
# using 4.0 vs 4 doesn't matter with the variable values in the exercise, 
# but what if the math didn't divide evenly?
space_in_a_car = 4
# space_in_a_car = 4.0
drivers = 37
# drivers = 30
passengers = 93
# passengers = 90
# using floating point numbers does not appear to matter in python
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."