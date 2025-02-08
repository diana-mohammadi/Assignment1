"""
Author: Diana Mohammadi
Assignment: 1
"""
gym_member = "Alex Alliton" #this is a string
preferred_wight_kg=20.5 #this is a float
highest_reps=25 #this is an integer
membership_active=True #this is a boolean

#this is a dictionary with keys of the name of the friends and values of the minutes they spent on doing 3 differen exercises (yoga, running, and weightlifting)
workout_stats = {"Alex":(30,45,60), "John":(25,40,55), "Sara":(20,35,50)} 

#create a lost of keys to iteragte through them instead of the dictionary
keys = list(workout_stats.keys())

for key in keys:
    total_min = 0
    for i in workout_stats[key]:
        total_min += i
    workout_stats[f"{key}_Total"] = total_min 


#this is a 2 dimensional list that contains the minutes spent on each exercise by each friend
workout_list = [list(workout_stats[key]) for key in workout_stats if not key.endswith("_Total")]
    
# the minutes spent on Yoga and Running for each friend
for i in range(len(workout_list)):
    print(f"\n{keys[i]}:")
    print("Minutes spent on Yoga:", workout_list[i][0]) 
    print("Minutes spent on Running:", workout_list[i][1],"\n")
print("----------------------------------")
# the minutes spent on weightlifting for the last two friends
for i in range(1, len(workout_list)):
    print(f"{keys[i]}:")
    print("Minutes spent on weightlifting:", workout_list[i][2],"\n")   
print("----------------------------------\n")
for key in workout_stats:
    if key.endswith("_Total") and (workout_stats[key] >= 120):
        name = key.replace("_Total", "")
        print(f"Great job staying active, {name}!\n")
        
print("----------------------------------\n")
nameInput = input("Enter the name of the friend: ")
if nameInput in workout_stats:
    print(f"minutes spent on yoga: {workout_stats[nameInput][0]}\n minutes spent on running: {workout_stats[nameInput][1]}\n minutes spent on weightlifting: {workout_stats[nameInput][2]}\n total minutes spent: {workout_stats[nameInput+'_Total']}")
else:
    print(f"\nFriend {nameInput} not found in the records.")


#this is highest and lowest minutes spent on workingout
total_values={key:value for key, value in workout_stats.items() if key.endswith("_Total")}
max_value = max(total_values.values())
min_value = min(total_values.values())

for key, value in total_values.items():
    if value == max_value:
        print(f"\n{key} spent the most time working out with {value} minutes.")
    elif value == min_value:
        print(f"\n{key} spent the least time working out with {value} minutes.")

        
        