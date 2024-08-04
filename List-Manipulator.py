##Declaring a Global Dictionary which contains all the lists of a User
my_lists = {}



def create_list(list_name): ##Function which creates a new list with the name of list_name
    '''
    Creates a new list.
    
    Creates a new list with the name list_name and stores it in the dictionary my_lists.Takes 1
    string argument.

    Parameters:

    list_name(str): The name of the new List

    Raises:
    KeyError: If the list name already exists.
    
    '''


    if list_name in my_lists:
        raise KeyError('List of name "', list_name, '" already exists')
    else:
        my_lists[list_name] = []
