#BEGINNER LEVEL TASK 1- [2ND NUMBERS]

# 1. Write a function that takes two arguments, 145 and 'o', and
# uses the format function to return a formatted string. Print the
# result. Try to identify the representation used.


def format_function(num, char):
    return "{0:{1}^10}".format(num, char)

result = format_function(145, 'o')
print("Formatted String:", result)
print("Representation used:", type(result)._name_)
#----------------------------------------------------------------------------#

# 2. In a village, there is a circular pond with a radius of 84 meters.
# Calculate the area of the pond using the formula: Circle Area = π r^2.
# (Use the value 3.14 for π) Bonus Question: If there is exactly
# 1.4 liters of water in a square meter, what is the total amount of
# water in the pond? Print the answer without any decimal point in
# it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
# Water per Square Meter


radius = 84
pi = 3.14
circle_area = pi * radius ** 2
water_per_square_meter = 1.4

total_water = int(circle_area * water_per_square_meter)
print("Total amount of water in the pond:", total_water)
#----------------------------------------------------------------------------#

# 3. If you cross a 490 meter long street in 7 minutes, calculate your
# speed in meters per second. Print the answer without any decimal
# point in it. Hint: Speed = Distance / Time


distance = 490
time = 7 * 60  # 7 minutes converted to seconds
speed = int(distance / time)
print("Speed in meters per second:", speed)
#----------------------------------------------------------------------------#