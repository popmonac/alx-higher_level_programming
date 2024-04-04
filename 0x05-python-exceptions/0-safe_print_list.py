#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    no_of_printed_element = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            no_of_printed_element += 1
    except IndexError:
        pass
    except TypeError:
        pass
    finally:
        print()
    return (no_of_printed_element)
