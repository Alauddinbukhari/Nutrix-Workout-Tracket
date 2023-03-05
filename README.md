
# Nutrix Workout Tracker

This is a Python script that allows users to input their daily workouts and track their progress over time. The script uses the Nutritionix API to identify exercises and calculate caloric expenditure. The data is then stored in a Google Sheet using the Sheety API.
## Getting Started

Before using this script, you will need to obtain API keys for the Nutritionix and Sheety APIs. Once you have these keys, you can set them as environment variables using the following commands:
```
os.environ[NUTRIX_APP_ID]=your_nutrix_app_id
os.environ[NUTRIX_API_KEY]=your_nutrix_api_key
os.environ[SHEETY_API_KEY]=your_sheety_api_key

```
Make sure to replace "your_nutrix_app_id", "your_nutrix_api_key", and "your_sheety_api_key" with your actual API keys.

## Usage
To use the script, simply run the nutrix_workout_tracker.py file in a Python environment. The script will prompt you to enter the exercises you did in plain text. For example, you could enter something like:
```
ran 3 miles and did 50 sit-ups
```

The script will then use the Nutritionix API to identify the exercises and calculate the caloric expenditure. The data will be stored in a Google Sheet using the Sheety API. You can view the Google Sheet at the following URL:

Python
```
https://docs.google.com/spreadsheets/d/your_spreadsheet_id/edit#gid=0
```
Make sure to replace "your_spreadsheet_id" with the actual ID of your Google Sheet.

## Contributing
If you find any bugs or issues with this script, please feel free to open a GitHub issue. Pull requests are also welcome if you would like to contribute to the project.




