def find_smallest(arr, start_index):
    if start_index >= len(arr):
        return None, None
    
    smallest = arr[start_index]
    
    index = start_index
    
    for i in range(start_index, len(arr)):
        if arr[i] < smallest:
            index = i
            smallest = arr[i]
    return smallest, index

def selection_sort(arr):
    for i in range(len(arr)):
        smallest, smallest_index = find_smallest(arr, i)
        if smallest and smallest_index:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

print(selection_sort([5,3,6,2,10]))
print(selection_sort(["banana","orange","apple"]))