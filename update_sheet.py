import requests
import keys
from datetime import datetime

#this module is responsible for updating the google spreadsheet using sheety API

END_POINT =  keys.sheety_post_endpoint

bearer_headers = {"Authorization": f"Bearer {keys.sheety_token}"
}


def update_sheet(exercise, duration, calories):
    """
    inputs(string): exercise, duration, calories
    
    """
    current_date = datetime.now().strftime("%d/%m/%Y")
    current_time = datetime.now().strftime("%X")
    

    
    payload = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories,
        }
    }
    
    
    response = requests.post(url=END_POINT,json=payload, headers=bearer_headers)
    
    if response.status_code == 200:
        print("Data updated successfully.")
    else:
        print("An error occurred while updating the data.")
        print("Response Status Code:", response.status_code)
        print("Response Content:", response.content)