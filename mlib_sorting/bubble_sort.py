def bubble_sort(input_list: list, reversed: bool = False) -> list:
    """
        input_list: list of number (`int`, `float`, ...)
        reversed: larger to smaller if `False` (default)
    """
    # copy input_list
    sorted_list = input_list.copy()
    
    # calculate number of elements
    element_number = len(sorted_list)

    # loop all elements 
    for idx1 in range(element_number - 1):
        # for each element, loop from the next elements to the last elements
        for idx2 in range(idx1 + 1, element_number):
            # if the 2nd element is greater than 1st element, swap 2 elements
            if sorted_list[idx2] > sorted_list[idx1]: 
                sorted_list[idx1], sorted_list[idx2] = sorted_list[idx2], sorted_list[idx1]
    
    # check if reversed (default from larger to smaller)
    if reversed:
        sorted_list = sorted_list[::-1]

    # return sorted list
    return sorted_list


if __name__ == "__main__":
    import random
    input_list = [random.randint(1, 100) for _ in range(10)]
    sorted_list = bubble_sort(input_list)
    reversed_sorted_list = bubble_sort(input_list, reversed = True)
    
    print("### BUBBLE SORT ###")
    print("Input list:", input_list)
    print("Output list (Descending):", sorted_list)
    print("Output list (Ascending):", reversed_sorted_list)