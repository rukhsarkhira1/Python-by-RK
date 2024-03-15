# Creating sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# add(element)
set1.add(4)
print(set1)  # Output: {1, 2, 3, 4}

# clear()
set1.clear()
print(set1)  # Output: set()

# copy()
set1 = {1, 2, 3}
set_copy = set1.copy()
print(set_copy)  # Output: {1, 2, 3}

# difference(set)
diff_set = set1.difference(set2)
print(diff_set)  # Output: {1, 2}

# difference_update(set)
set1.difference_update(set2)
print(set1)  # Output: {1, 2}

# discard(element)
set1.discard(1)
print(set1)  # Output: {2}

# intersection(set)
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {}

# intersection_update(set)
set1 = {1, 2, 3}
set1.intersection_update(set2)
print(set1)  # Output: {3}

# isdisjoint(set)
print(set1.isdisjoint(set2))  # Output: False

# issubset(set)
print(set1.issubset(set2))  # Output: True

# issuperset(set)
print(set1.issuperset({3}))  # Output: True

# pop()
popped_element = set1.pop()
print(popped_element)  # Output: 3

# remove(element)
set1.remove(2)
print(set1)  # Output: set()

# symmetric_difference(set)
sym_diff_set = {1, 2, 3}.symmetric_difference({3, 4, 5})
print(sym_diff_set)  # Output: {1, 2, 4, 5}

# symmetric_difference_update(set)
set1 = {1, 2, 3}
set1.symmetric_difference_update({3, 4, 5})
print(set1)  # Output: {1, 2, 4, 5}

# union(set)
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# update(set)
set1.update({5, 6, 7})
print(set1)  # Output: {1, 2, 3, 5, 6, 7}
