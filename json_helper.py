import json
import os
import pickle

""" Define a function called read_json. Given a string representing a 
    file path to a json file, this function should open said file 
    and convert its contens into a json object. The json object should be returned."""


def read_json(file_name_txt):
    with open(file_name_txt) as json_file:
        json_to_dictionary = json.load(json_file)
        dictionary_to_object = json.dumps(json_to_dictionary)
        return dictionary_to_object


# print(read_json('/Users/cantekinefe/dev/PyPart9/data/super_smash_bros/link.json'))

""" Define a function called read_all_json_files. Given a string representing a 
    path to a directory, this function should read all of the json files 
    and return a list containing all of the json objects."""


def read_all_json_files(file_path):
    listed_directory = os.listdir(file_path)
    json_as_list = []
    for file_name in listed_directory:
        json_file_path = os.path.join(file_path, file_name)
        file_read = read_json(json_file_path)
        json_as_list.append(file_read)
    return json_as_list


# print(read_all_json_files('data/super_smash_bros'))

""" Define a function called write_pickle. This function should take a file path 
    and some data. Given these parameters, the function should write the contents 
    of the json files to a file called super_smash_characters.pickle."""


def write_pickle(file_name_txt, data):
    json_as_list = read_json(file_name_txt)
    with open(data, 'wb') as pickle_file:
        pickle.dumps(json_as_list, pickle_file)


# write_pickle('/Users/cantekinefe/dev/PyPart9/data/super_smash_bros/link.json', 'super_smash_characters.pickle')


def load_pickle(pickle_file_path):
    with open(pickle_file_path, 'rb') as pickle_file:  # reads resulting pickled data
        data = pickle.load(pickle_file)
    return data


# print(load_pickle('/Users/cantekinefe/dev/PyPart9/super_smash_characters.pickle'))
