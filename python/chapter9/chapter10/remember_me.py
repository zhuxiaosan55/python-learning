import json
file_name = 'username.json'
try:
    with open(file_name) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("what's your name")
    with open(file_name, 'w') as f_obj:
        json.dump(username, f_obj)
        print("we will remember when you come back,"+username+'!')
else:
    print("welcome back,"+username+'!')
