import json

def saver_json(info_to_save, filename):
    "saving  info get from user to json"
    print (f"\nwrite {info_to_save}, to {filename}")
    with open (filename, 'w') as f:
        json.dump(info_to_save, f)
    print (f"We'l remember you, when you come back, {info_to_save}")

def loader_json(filename):
    "read the json file and return data"
    try:
        print (f"\nread file '{filename}': ")
        with open (filename) as f:
            info_to_load = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return info_to_load
        



info_to_save = input ('What is you name? ')
filename = 'username.json'
saver_json(info_to_save, filename)
print (loader_json(filename))