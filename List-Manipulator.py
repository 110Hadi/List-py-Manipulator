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



def add_item(list_name, item, priority):
    '''
    Adds items to a specified list.

    Adds item to the list list_name at a given priority.

    Parameters::

    list_name(str): Name of the list to which an item is to be added.
    item(str): The name of item which is to be added to the list.
    priority(int): The position in the list where an item is added.

    Raises:
    ValueError: If priority is less than 1.
    KeyError: If the name of list does not already exists.
    '''

    
    if priority < 1:
        raise ValueError('A Positive Number Is Required')

    if not list_name in my_lists:
        raise KeyError('List of name "', list_name, '" does not exist.')
    else:
        if priority >= len(my_lists[list_name]):
            item = f'{len(my_lists[list_name]) + 1} {item}'
            my_lists[list_name].append(item)

        else:
            item = f'{priority} {item}'
            my_lists[list_name].insert(priority - 1, item)

            for items in range(priority, len(my_lists[list_name])):
                current_item = my_lists[list_name][items]
                index = current_item.find(' ')
                old_position = current_item[:index]
                new_position = int(old_position) + 1
                current_item = f'{new_position}{current_item[index:]}'
                my_lists[list_name][items] = current_item
