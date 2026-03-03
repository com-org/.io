import json
import os
import sys

def save_user():
    # Ensure arguments (username and password) were passed from the workflow
    if len(sys.argv) < 3:
        print("Error: Missing arguments.")
        return

    username = sys.argv[1]
    password = sys.argv[2]

    file_path = 'data.json'

    # Check if the file exists; if not, initialize an empty list
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                # Ensure the data is a list
                if not isinstance(data, list):
                    data = []
        except (json.JSONDecodeError, ValueError):
            # If file is corrupted or empty, start fresh
            data = []
    else:
        print(f"{file_path} not found. Creating a new one.")
        data = []

    # Append the new user record
    new_entry = {
        "username": username,
        "password": password
    }
    data.append(new_entry)

    # Write back to data.json with clean formatting
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"Successfully saved user: {username}")

if __name__ == "__main__":
    save_user()
