 #BEGINNER LEVEL TASK 1- [3RD LIST]

# Creating list named as justice_league with different superheroes.
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
#--------------------------------------------------------------------------------------------------------------------------#

# 1. Calculate the number of members in the Justice League.
number_of_members = len(justice_league)
print("Number of members in Justice League:", number_of_members)
#--------------------------------------------------------------------------------------------------------------------------#

# 2. Batman recruited Batgirl and Nightwing as new members as new members.
# Add them to your list.
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)
#--------------------------------------------------------------------------------------------------------------------------#

# 3. Wonder Woman is now the leader of the Justice League. Move her to the 
# beginning of the list (as a new leader).
justice_league.remove("Wonder Woman") 
justice_league.insert(0, "Wonder Woman") #0 index for 1st member of list
print(justice_league)
#--------------------------------------------------------------------------------------------------------------------------#

# 4. Aquaman and Flash are having conflicts, and you need to separate them.
# Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash.
justice_league.remove("Green Lantern")
justice_league.insert(4, "Green Lantern") #4th index just after flash and before Aquaman
print(justice_league)
#------------------------------------------------------------------------------------------------------------------------#

# 5. The Justice League faced a crisis, and Superman decided to assemble a
#  new team. Replace the existing list with the following new members: 
# "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow".
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(justice_league)
#-----------------------------------------------------------------------------------------------------------------------#

# 6. Sort the Justice League alphabetically.The hero at the 0th index will
#  become the new leader.
justice_league.sort()
new_leader = justice_league[0]
print(justice_league)
print("New leader of the Justice League at 0th index:", new_leader) #New leader: Cyborg
#-----------------------------------------------------------------------------------------------------------------------#