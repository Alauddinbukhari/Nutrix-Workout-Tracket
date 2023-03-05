import requests
import datetime
import os

# Get the Nutrix app details from environment variables
NUTRIX_APP_ID = os.environ.get("NUTRIX_APP_ID")
NUTRIX_API_KEY = os.environ.get("NUTRIX_API_KEY")

# Get today's date and time
todays_date = datetime.datetime.now().strftime("%Y/%m/%d")
todays_exact_time = datetime.datetime.now().strftime("%I.%M.%S")

# Endpoint to get exercise data from Nutrix API
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Set the authorization token for Nutrix API requests
TOKEN = "Bearer require"

# Get input for exercises performed
plain_text = input("Tell me which exercises you did: ")

# Set headers and parameters for Nutrix API request
header_nutix = {
    "x-app-id": NUTRIX_APP_ID,
    "x-app-key": NUTRIX_API_KEY,
    "Authorization": TOKEN  # Authorization token required for Nutrix API
}
parameters_nutrix = {
    "query": plain_text
}

# Send post request to Nutrix API to get exercise data
response = requests.post(headers=header_nutix, json=parameters_nutrix, url=EXERCISE_ENDPOINT)

# Extract exercise data from response
exercise_names = [item["name"] for item in response.json()["exercises"] if "name" in item]
caloric_lose = [item["nf_calories"] for item in response.json()["exercises"] if "name" in item]
duration_of_exercise = [item["duration_min"] for item in response.json()["exercises"] if "duration_min" in item]

# Print exercise data
print(exercise_names)
print(caloric_lose)
print(duration_of_exercise)

# Set authorization token for Sheety API requests
sheety_token = "Bearer require"
sheety_header = {
    "Authorization": sheety_token
}

# Send data for each exercise performed to Sheety API
for i in range(len(exercise_names)):
    data = {
        "workout": {
            "date": datetime.datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.datetime.now().strftime("%I.%M.%S"),
            "exercise": exercise_names[i].title(),
            "duration": duration_of_exercise[i],
            "calories": caloric_lose[i]
        }
    }

    # Send post request to Sheety API to add data to workout sheet
    send_data = requests.post("Sheety api",
                              headers=sheety_header, json=data)
    print(send_data.text)
