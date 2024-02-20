def insertion_sort(input_list: list, reversed: bool = False) -> list:
    sorted_list = input_list.copy()
    element_number = len(sorted_list)
    for idx1 in range(1, element_number):
        key = sorted_list[idx1]
        for idx2 in range(idx1, 0, -1):
            if key > sorted_list[idx2 - 1]:
                sorted_list[idx2 - 1], sorted_list[idx2] = sorted_list[idx2], sorted_list[idx2 - 1]

    if reversed:
        sorted_list = sorted_list[::-1]
    return sorted_list


if __name__ == "__main__":
    import random
    input_list = [random.randint(1, 100) for _ in range(10)]
    sorted_list = insertion_sort(input_list)
    reversed_sorted_list = insertion_sort(input_list, reversed = True)
    
    print("### INSERTION SORT ###")
    print("Input list:", input_list)
    print("Output list (Descending):", sorted_list)
    print("Output list (Ascending):", reversed_sorted_list)