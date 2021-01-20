

def binary_search(data, target_value, upper, lower=0, dimensionality=False, recursive=False):
    """
    Recursive search function which assumes the input of a sorted list.

    Returns true if the target value is found within the defined search parameters of the list.

    The search parameters are defined by the variables 'upper' and 'lower' which are used as index references for the list.

    Checks the dimensionality of the input data and only accepts 1d lists.

    :param data: A 1D list
    :param target_value: the value we are trying to find in our array
    :param upper: the upper index value of our search parameters
    :param lower: the lower index value of our search parameters
    :param dimensionality: boolean value to keep track of list dimensionality in recursion
    :param recursive: boolean value to indicate the search is in a state of recursion
    :return:
    """
    if recursive == False:
        if isinstance(data[0], list) == False:
            dimensionality = True
            recursive = True

    if dimensionality == True:
        print('1.1')
        if upper < lower:
            print('1.1.1')
            return False
        else:
            print('1.2')
            mid = (upper + lower) // 2
            print(mid)
            print(data[mid])
            if target_value == data[mid]:
                print('1.2.1')
                return True
            elif target_value > data[mid]:
                print('1.2.2')
                return binary_search(data, target_value, upper, mid+1, dimensionality, recursive)
            else:
                print('1.2.3')
                return binary_search(data, target_value, mid-1, lower, dimensionality, recursive)
    else:
        print('2.1')
        return False
