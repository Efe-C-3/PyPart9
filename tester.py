import json

person_as_json = '{"name": "bob", "age": 18}'
person_as_dict = json.loads(person_as_json)
type(person_as_dict) --> dict

person_as_dictionary = {'name': 'bob', 'age': 18}
person_as_json_format = json.dumps(person_as_dictionary)
type(person_as_json_format) --> str

animal_as_list = ['dog', 'cat', 'mouse']
animal_as_json = json.dumps((animal_as_list))
type(animal_as_json) --> str

numbers_as_json = '[1, 2, 3, 4]'
numbers_as_list = json.loads(numbers_as_json)
type(numbers_as_list) --> list


#Arrays Example:
{
    "serviceHistory": [
        "serviceType: "Oil change",
        "serviceDate": "Jun 23 1968",
    ],
}

json.loads() #converts to dictionary
             #converts to list
json.dumps() #converts from dictionary to json as str
             #converts from list to json as str


{
    "key1": "value1",
    "key2": "value",
}

{
    "carId": "AZU-3005",
    "carMake": "Chevy",
    "carModel1": "Camaro",
}

{
    "modelYear": 1967,
    "acceleration060": 6.3,
}

{
    "isForSale": false,
    "isAntique": true,
}

{
    "serviceHistory": null,
}
