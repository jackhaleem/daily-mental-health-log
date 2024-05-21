import json
from datetime import datetime

# Function to gather user input for daily mental health log
def get_user_input():
    # Get user's name
    name = input("What is your name? ")
    # Get today's date in YYYY-MM-DD format
    date = datetime.today().strftime('%Y-%m-%d')
    # Get user's mood on a scale from 1 to 10
    mood = input("How are you feeling on a scale from 1-10? ")
    # Get three things the user is grateful for
    gratitude = []
    for i in range(3):
        gratitude.append(input(f"Thing {i+1} you are grateful for: "))
    
    # Return a dictionary containing the user's responses
    return {
        "name": name,
        "date": date,
        "mood": mood,
        "gratitude": gratitude
    }

# Function to save user response to a file
def save_response(response):
    try:
        # Open the responses.json file in append mode
        with open('responses.json', 'a') as f:
            # Write the response as a JSON object followed by a newline
            json.dump(response, f)
            f.write('\n')
        print("Response saved successfully.")
    except Exception as e:
        print(f"Error saving response: {e}")

# Function to view past responses from the log file
def view_log():
    try:
        # Open the responses.json file in read mode
        with open('responses.json', 'r') as f:
            # Read each line in the file
            for line in f:
                # Parse the JSON object and print it
                response = json.loads(line.strip())
                print(response)
    except Exception as e:
        print(f"Error reading log: {e}")

# Main function to display the menu and handle user choices
def main():
    print("Program started...")  # Indicate that the program has started
    while True:
        # Display menu options
        print("1. Record today's responses")
        print("2. View past responses")
        print("3. Exit")
        # Get user's choice
        choice = input("Choose an option: ")
        # Handle the user's choice
        if choice == '1':
            response =
