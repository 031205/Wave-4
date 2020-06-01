def reverseLookup(dictionary, search_value):
    keys_list = [key for key, value in dictionary.items() if value == search_value]
    return keys_list