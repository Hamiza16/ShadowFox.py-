#BEGINNERS LEVEL TASK 1 - [2ND NUMBERS]

# 1. Write a function that takes two arguments, 145 and 'o', and uses the format function to
#  return a formatted string.Print the result. Try to identify the representation used.

def formatfunc(num , letter) :  
    return format(num,letter)   

print(formatfunc(145,'o')) # Displaying the final result 

#----------------------------------------------------------------------------------------------------------------------------------#

# 2.  In a village, there is a circular pond with a radius of 84 meters. 
# Calculate the area of the pond using the formula: Circle Area = π r^2. (Use the value 3.14 for π) 
# Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total
# amount of water in the pond?Print the answer without any decimal point in it. Hint: Circle
# Area = π r^2 Water in the pond = Pond Area Water per Square Meter 

pond_radius = 84        
pi = 3.14            

pond_area = int((pi * pond_radius * pond_radius))    
total_water = int((pond_area * 1.4))                   

print(f"The total pond area is {pond_area} and the total water in the pond is {total_water} liters") 

#----------------------------------------------------------------------------------------------------------------------------#

# 3. If you cross a 490 meter long street in 7 minutes, calculate your speed in meters per second. 
#    Print the answer without any decimal point in it. Hint: Speed = Distance / Time

distance = 490      # Storing the Given Distance
time = 7            # Storing the Given Time

speed = int((distance / time))      # Caculating the speed [speed = distance / time ]

print(f"The Speed is {speed}")

#-----------------------------------------------------------------------------------------------------------------------------#