import requests
from dotenv.main import load_dotenv
from datetime import datetime
import os


load_dotenv()
app_id = os.environ["APP_ID"]
app_key = os.environ["APP_KEY"]
GENDER = "female"
WEIGHT_KG = 50
HEIGHT_CM = 162
AGE = 23

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/7c6b742fb38c0b79b8913452912f2814/workoutTracking/workouts"

headers = {
    "x-app-id": app_id,
    "x-app-KEY": app_key,
}
text_input = input("Tell me which exercises you did: ")

parameters = {
 "query": text_input,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": "Bearer hjgvdznhvcnb"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)
