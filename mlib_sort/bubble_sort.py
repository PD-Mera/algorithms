def bubble_sort(input_list: list, reversed: bool = False) -> list:
    sorted_list = input_list.copy()
    element_number = len(sorted_list)
    for idx1 in range(element_number - 1):
        for idx2 in range(idx1 + 1, element_number):
            if sorted_list[idx1] < sorted_list[idx2]:
                sorted_list[idx1], sorted_list[idx2] = sorted_list[idx2], sorted_list[idx1]
    if reversed:
        sorted_list = sorted_list[::-1]
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