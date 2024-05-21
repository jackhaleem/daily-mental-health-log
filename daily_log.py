import json
from datetime import datetime

def get_user_input():
    name = input("What is your name? ")
    date = datetime.today().strftime('%Y-%m-%d')
    mood = input("How are you feeling on a scale from 1-10? ")
    gratitude = []
    for i in range(3):
        gratitude.append(input(f"Thing {i+1} you are grateful for: "))
    
    return {
        "name": name,
        "date": date,
        "mood": mood,
        "gratitude": gratitude
    }

def save_response(response):
    try:
        with open('responses.json', 'a') as f:
            json.dump(response, f)
            f.write('\n')
        print("Response saved successfully.")
    except Exception as e:
        print(f"Error saving response: {e}")

def view_log():
    try:
        with open('responses.json', 'r') as f:
            for line in f:
                response = json.loads(line.strip())
                print(response)
    except Exception as e:
        print(f"Error reading log: {e}")

def main():
    while True:
        print("1. Record today's responses")
        print("2. View past responses")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            response = get_user_input()
            save_response(response)
        elif choice == '2':
            view_log()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
