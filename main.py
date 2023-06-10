from get_exercise_data import get_exercise_data
from update_sheet import update_sheet

exercise_list = get_exercise_data()['exercises']

#run the update function for as many items in the list
for exercise_dict in exercise_list:
    exercise = exercise_dict['user_input']
    duration = exercise_dict['duration_min']
    calories = exercise_dict['nf_calories']
    update_sheet(exercise=exercise,duration=duration,calories=calories)
        
    
