groceries = ["milk", "eggs", "bread", "butter"]
print(f"{groceries}\n")

groceries.append("cheese")
print(f"Append cheese: {groceries}")

groceries.insert(1, "orange juice")
print(f"Insert orange juice at index 1: {groceries}")

groceries.remove("bread")
print(f"Remove bread: {groceries}")

popped = groceries.pop()
print(f"Pop: {popped}")

groceries.sort()
print(f"Sort: {groceries}")

groceries.reverse()
print(f"Reverse: {groceries}")

print(f"Length: {len(groceries)}")
print(f"Contains milk: {'milk' in groceries}")
print(f"Concatenate with ham: {groceries + ['ham']}")
print(f"Repeat twice: {groceries * 2}")