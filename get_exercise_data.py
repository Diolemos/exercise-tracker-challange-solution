#this function is responsible for talking to nutritionix API
import keys
import requests

API_KEY = keys.nutritionix
APP_ID = keys.nutritionix_app_id

def get_exercise_data():
    

    #1. Using the Nutritionix "Natural Language for Exercise" API Documentation, figure out how to print the exercise stats for plain text input.



    END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

    exercise_text = input("Tell me which exercises you did: ")

    params = {
        "query": exercise_text,
        "gender": "male",
        "weight_kg": 113,
        "height_cm": 177.00,
        "age": "32",

    }

    headers = {"x-app-id": APP_ID,
            "x-app-key": API_KEY,
            "x-remote-user-id": "0",
            "Content-Type": "application/json"}

    response = requests.post(url=END_POINT, json=params, headers=headers)

    return response.json()
    
    #return something

