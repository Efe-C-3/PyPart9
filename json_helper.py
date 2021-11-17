import json
import os
import pickle


def read_json(file_name_txt):
    with open(file_name_txt) as json_file:
        json_to_dictionary = json.load(json_file)
        dictionary_to_object = json.dumps(json_to_dictionary)
        return dictionary_to_object


# print(read_json('/Users/cantekinefe/dev/PyPart9/data/super_smash_bros/link.json'))

def read_all_json_files(file_name_txt):
    full_path = os.path.abspath(file_name_txt)
    listed_directory = os.listdir(full_path)
    json_as_list = []
    for file in listed_directory:
        json_file = full_path
        file_read = read_json(json_file)
        json_as_list.append(file_read)
    return json_as_list


# print(os.path.abspath('data/super_smash_bros/link.json'))
# print(read_all_json_files('data/super_smash_bros/link.json'))


def write_pickle(file_name_txt, some_data):
    json_as_list = read_all_json_files(file_name_txt)
    with open('some_data.pickle', 'wb') as pickle_file:  # found in docs.python.org
        pickle.dumps(json_as_list, pickle_file)  # takes an object as a parameter and returns a string representation


# print(write_pickle('link.json', 'super_smash_characters'))


def load_pickle(file_path):
    with open('some_data.pickle', 'rb') as pickle_file:  # reads resulting pickled data
        data = pickle.load(pickle_file)  # found in docs.python.org
    return data

# print(load_pickle(/Users/cantekinefe/dev/PyPart9/data))
