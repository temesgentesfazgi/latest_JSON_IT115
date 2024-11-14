# Imported JSON library to work with JSON data formats
import json

# Defining a dictionary
data1 = {

    'name': 'nathan',
    'age': 100,
    'city': 'Seattle',
    'interests': ['soccer', 'videogame'],
    'is_student': True

}

# Write the data on a new file as JSON file
with open('data1.json', 'w') as json_file:
    #Dump the data dictionary into the json file
    json.dump(data1,json_file,indent=4)

print("Data has been written to data1.json")

#Read the JSON file
with open('data1.json', 'r') as json_file:

    loaded_data = json.load(json_file)

print("successfully able to read data1.json")
print(loaded_data)

#Altering content of the JSON dictionary
loaded_data['age'] = 10
loaded_data['interests'].append('silly')

# loaded_data['interests'].remove('videogame')

# ReSave the altered JSON file
with open('data2.json', 'w') as json_file:
    #Dump the data dictionary into the json file
    json.dump(loaded_data,json_file,indent=4)

print("Data has been re-written to data1.json")