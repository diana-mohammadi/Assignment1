
# Author: Diana Mohammadi
# Assignment: #1

gym_member = "Alex Alliton" #this is a string
preferred_wight_kg=20.5 #this is a float
highest_reps=25 #this is an integer
membership_active=True #this is a boolean

#this is a dictionary with keys of the name of the friends and values of the minutes they spent on doing 3 differen exercises (yoga, running, or weightlifting)
workout_stats = {"Alex":(30,45,60), "John":(25,40,55), "Sara":(20,35,50)} 

keys = list(workout_stats.keys())

for key in keys:
    total_min = 0
    for i in workout_stats[key]:
        total_min += i
    workout_stats[f"{key}_Total"] = total_min 


#this is a 2 dimensional list that contains the minutes spent on each exercise by each friend
workout_list = [list(workout_stats[key]) for key in workout_stats if not key.endswith("_Total")]
      
for i in workout_list:
    print("Minutes spent on Yoga:", i[0]) 
    print("Minutes spent on Running:", i[1],"\n")

for i in workout_list[1:]:
    print("Minutes spent on weightlifting:", i[2],"\n")   

      
        
        