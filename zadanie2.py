list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]
list_to_sort_2.sort(key=lambda list_element: (list_element[1], list_element[2]))
print(list_to_sort_2)