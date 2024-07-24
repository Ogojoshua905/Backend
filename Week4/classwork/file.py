import json
import os

class File:
    @staticmethod
    def save_to_file(data, filename):
        if not os.path.exists('store'):
            os.makedirs('store')
        with open(filename, 'w') as file: #with statement makes sure the file is opened and closed properly 
            json.dump(data, file, indent=4) # A function That Converts lists or Dictionaries into json files and dump it in a file
            # indent=4 means the JSON data will be formatted with an indentation of 4 spaces, making it easier to rea
        print(f"Data Saved to {filename}")

    @staticmethod
    def load_from_file(filename):
        try: #Exception Handling
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"file Not Found {filename}")
            return []
        except json.JSONDecodeError:
            print(f"There is An Error decoding the Json file structure at {filename}")
            return []
            

    @staticmethod
    def delete_file(filename):
        if os.path.exists(filename):
            os.remove(filename)
            print(f"{filename} has be deleted")
        else:
            print(f"{filename} does not exist.")
