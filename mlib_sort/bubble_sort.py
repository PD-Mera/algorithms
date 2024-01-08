def bubble_sort(input_list: list) -> list:
    sorted_list = input_list.copy()
    element_number = len(sorted_list)
    for idx1 in range(element_number - 1):
        for idx2 in range(idx1 + 1, element_number):
            if sorted_list[idx1] < sorted_list[idx2]:
                sorted_list[idx1], sorted_list[idx2] = sorted_list[idx2], sorted_list[idx1]
    return sorted_list

if __name__ == "__main__":
    import random
    input_list = [random.randint(1, 100) for _ in range(10)]
    sorted_list = bubble_sort(input_list)
    print(input_list)
    print(sorted_list)