import json

def saver_json(info_to_save, filename):
    "saving  data, get from user to json"
    print (f"\nwrite {info_to_save}, to {filename}")
    with open (filename, 'w') as f:
        json.dump(info_to_save, f)
    print (f"We'l remember you like number, when you come back")

def loader_json(filename):
    "read the json file and return data"
    try:
        with open (filename) as f:
            info_to_load = json.load(f)
    except FileNotFoundError:
        return None
    else:
        print (f"\nread file '{filename}': ")
        return info_to_load
        
def quester(filename):
    "main function "
    like_number = loader_json(filename)
    if like_number:
        print (f"You like number is {like_number}")
    else:
        info_to_save = input ('What is you like number? ')
        saver_json(info_to_save, filename)


filename = 'like_number.json'
quester(filename)


