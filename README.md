
## Workout Tracker

This is a simple workout tracker script built using Python and several APIs. The script allows users to input the exercises they did, and then uses the Nutritionix API to get information about those exercises (such as the number of calories burned). It then logs that information to a Google Sheet using the Sheety API.
### Installation

To use this script, you'll need to install several dependencies:

1. Install the "requests" module by running "pip install requests"
2. Install the "dotenv" module by running "pip install python-dotenv"

You'll also need to set up API keys for both the Nutritionix and Sheety APIs. Follow the instructions on their respective websites to get your API keys.

Once you have your API keys, create a .env file in the root directory of the project, and add the following lines:

```
APP_ID=[your Nutritionix app ID]
APP_KEY=[your Nutritionix app key]
BEARER_TOKEN=[your Sheety bearer token]
```

### Usage

To use the script, simply run "python main.py" in your terminal. You'll be prompted to enter the exercises you did (e.g. "ran 3 miles" or "lifted weights for 30 minutes"). The script will then use the Nutritionix API to get information about those exercises, and log that information to a Google Sheet using the Sheety API.

