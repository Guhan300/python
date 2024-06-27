import json
from difflib import get_close_matches

json_file=json.load(open("data1.json"))

value=input("Enter the value: ")
def get_data(value):
    value=value.lower()
    if value in json_file:
        return json_file[value]
    elif len(get_close_matches(value,json_file.keys()))>0:
        choice= input("Did you mean %s :if yes press Y or if No press N:" %get_close_matches(value,json_file.keys()) [0] )
        if choice =="y" or "Y":
            return json_file[get_close_matches(value,json_file.keys()) [0]]
        elif choice=="n" or "N":
            return "data is not exist" 
        else:
            return "you press wrong key try again!"
    else:
        return "data is not exist!"




result=(get_data(value))
if type(result)==list:
    for i in result:
        print(i)
else:
    print(result)



   