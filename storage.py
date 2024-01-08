import csv
import json

def save_to_csv(data, filename):
    """
    Saves data to a CSV file.

    :param data: Data to be saved. Should be a list of dictionaries.
    :param filename: Name of the file to save the data.
    """
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    except IOError as e:
        print(f"Error saving data to {filename}: {e}")

def save_to_json(data, filename):
    """
    Saves data to a JSON file.

    :param data: Data to be saved.
    :param filename: Name of the file to save the data.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error saving data to {filename}: {e}")

def save_to_text(data, filename):
    """
    Saves data to a text file.

    :param data: Data to be saved.
    :param filename: Name of the file to save the data.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for item in data:
                file.write(str(item) + '\n')
    except IOError as e:
        print(f"Error saving data to {filename}: {e}")
