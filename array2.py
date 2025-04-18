# add
add = []
add.append("hai")

# copy
copy = add.copy()

# remove
copy.remove("hai")

# Insert
copy.insert(len(copy), "hello")

# extend
copy.extend(["world", "python"])

# count
print(copy.count("hello"))

# sort aq-z, 1-10
print(copy.sort())

# reverse
print(copy.reverse())

# index
print(copy.index("hello"))

print(copy)