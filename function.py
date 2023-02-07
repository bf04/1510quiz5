def is_sorted(user_list):
    """
    Check list of integers.

    A function that checks if a list is sorted or not.

    :param:list
    :precondition: list can either contain integers or be empty
    :postcondition: correctly returns True if list is sorted, False if not sorted
    :return: True if sorted, False if not sorted
    >>> is_sorted([2,4,5,6])
    True
    >>> is_sorted([20,19,18,17,16])
    False
    >>> is_sorted([0,0,0,0,0])
    True
    >>> is_sorted([-1.5,-2.7,-3.9,-4.2,-5.7])
    False
    >>> is_sorted([6.3, 9.5, 15.6, 20.1])
    True
    """

    if user_list == sorted(user_list):
        return True
    else:
        return False


def main():
    print(is_sorted())


if __name__ == "__main__":
    main()
