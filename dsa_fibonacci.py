

def fibonacci(n, recursive=False):
    """
    Takes a number n as an input for the nth value of a number in the fibonacci sequence and determines Fn the value corresponding to this index.
    :param n: Integer input
    :param recursive: boolean used upon the first run of the function to ensure input is integer.
    :return: Integer
    """
    if recursive == False:
        if isinstance(n, int) == False:
            print("Incorrect input: the input n must be a valid integer equal to or greater than 1")
        elif n <= 0:
            print("Incorrect input: the input n must be a valid integer equal to or greater than 1")
        else:
            if n == 1:
                return 0
            elif n == 2:
                return 1
            else:
                recursive = True
                return fibonacci(n-1)+fibonacci(n-2)
    else:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibonacci(n-1)+fibonacci(n-2)

