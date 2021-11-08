import json
import os
import pickle


def read_json(file_name_txt):
    with open(file_name_txt) as json_file:
        json_to_dictionary = json.load(json_file)
        dictionary_to_object = json.dumps(json_to_dictionary)
        return dictionary_to_object


def read_all_json_files(file_name_txt):
    full_path = os.path.abspath(file_name_txt)
    listed_directory = os.listdir(full_path)
    jason_as_list = []
    for file in listed_directory:
        json_file = full_path
        json_as_list = read_json(json_file)
        json_as_list.append(json_as_list)
    return json_as_list


def write_pickle(file_name_txt, some_data):
    jason_as_list = read_all_json_files(file_name_txt)
    with open('some_data.pickle', 'wb') as pickle_file:  # found in docs.python.org
        pickle.dumps(jason_as_list, pickle_file)  # takes an object as a parameter and returns a string representation


def load_pickle(some_data):
    with open('some_data.pickle', 'rb') as pickle_file:  # reads resulting pickled data
        data = pickle.load(pickle_file)  # found in docs.python.org
    return data


print(load_pickle())
