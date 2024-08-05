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

    try:
        if list_name in my_lists:
            raise KeyError(f'List of name "{list_name}" already exists')
        else:
            my_lists[list_name] = []

    except KeyError as error:
        print(f'''KeyError: Cannot create list.
Details: {error}''')



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

    try:
        if priority < 1:
            raise ValueError('A Positive Number Is Required')
    except ValueError as error:
        print(f'ValueError: {error}')

    try:
        if not list_name in my_lists:
            raise KeyError(f'List of name "{list_name}" does not exist.')
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
                    
    except KeyError as error:
        print(f'''KeyError: Cannot perform operation.
Details: {error}''')

            

def del_list(list_name):
    '''
    Completely deletes a specified list.

    Parameters:
    list_name(str): The name of the list which is to be deleted.

    Raises:
    KeyError: If the list does not already exists.
    '''    

    try:
        if list_name not in my_lists:
            raise KeyError(f'List of name "{list_name}" does not exist.')
        else:
            my_lists.pop(list_name)
    except KeyError as error:
        print(f'''KeyError: Cannot perform operation.
Details: {error}''')


def remove_item(list_name, item):
    '''
    Removes an item from a specified list.

    Parameters:
    list_name(str): The name of the list from which an item is to be removed.
    item(str): The item which is to be removed from the specified list.

    Raises:
    KeyError: If the list doesnot exists.
    ValueError: If the item in the list does not exists.
    '''


    if list_name not in my_lists:
        raise KeyError(f'List of name {list_name} does not exist.') 

    else:
        try:
            my_lists[list_name].remove(item)
        except ValueError:
            print(f'Item does not exists in {list_name}')
