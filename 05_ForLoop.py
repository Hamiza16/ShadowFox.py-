#BEGINNER LEVEL TASK 1-[5TH FOR LOOP]

# 1. Using a for loop, simulate rolling a sixsided die multiple times(at least 20 times).
import random

num_rolls = 30

count_6 = 0
count_1 = 0
two_6s_in_a_row = 0

previous_roll = 0

for _ in range(num_rolls):
    roll = random.randint(1, 6)
    
    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            two_6s_in_a_row += 1
    elif roll == 1:
        count_1 += 1

    previous_roll = roll  

print("Total rolls:", num_rolls)
print("Number of times 6 was rolled:", count_6)
print("Number of times 1 was rolled:", count_1)
print("Number of times two 6s occurred in a row:", two_6s_in_a_row)
#----------------------------------------------------------------------------------------------------------------------#

# 2. Imagine you are doing a workout routine, and you have to complete 100 jumping jacks.
total_jumping_jacks = 100
set_size = 10
completed = 0

while completed < total_jumping_jacks:
    completed += set_size
    print(f"\nYou completed {completed} jumping jacks.")

    # Check if user completed full workout
    if completed >= total_jumping_jacks:
        print("🎉 Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").strip().lower()
    
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"\nYou completed a total of {completed} jumping jacks.")
            break
        else:
            print(f"{total_jumping_jacks - completed} jumping jacks remaining.")
    else:
        print(f"{total_jumping_jacks - completed} jumping jacks remaining.")
        #----------------------------------------------------------------------------------------------------------------#