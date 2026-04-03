fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}

fruits.add("grape")
fruits.remove("banana")
fruits.discard("kiwi")

print(fruits)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))