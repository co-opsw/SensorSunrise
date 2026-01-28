import json


def store_json_data(data, filename):
    file_path = f"./data/{filename}.json"

    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=2)

    except Exception as e:
        print(e)
