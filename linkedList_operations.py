from linkedList import LinkedList

new_list = LinkedList()
node_data = [76,34,52,96]

for data in node_data:
    new_list.insert_at_head(data)
    new_list.print_list()
    
print("search for 34")
node = new_list.search(34)
if node:
    print(node.data)
else:
    print(node)

print("search for -1")
node = new_list.search(-1)
if node:
    print(node.data)
else:
    print(node)
    
new_list.delete(96)
print("list after deleting the head: ")
new_list.print_list()

new_list.insert_at_head(96)

new_list.delete(34)
print("list after deleting node 34")
new_list.print_list()

new_list.selection_sort()
print("sorted list")
new_list.print_list()