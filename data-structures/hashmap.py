# Creating a hashmap
my_hashmap = {}

# Adding key-value pairs to the hashmap
my_hashmap['key1'] = 'value1'
my_hashmap['key2'] = 'value2'
my_hashmap['key3'] = 'value3'

# Accessing values using keys
print("Value for key 'key1':", my_hashmap['key1'])
print("Value for key 'key2':", my_hashmap['key2'])

# Checking if a key is present in the hashmap
if 'key3' in my_hashmap:
    print("'key3' is present in the hashmap")

# Removing a key-value pair from the hashmap
removed_value = my_hashmap.pop('key2')
print("Removed value for key 'key2':", removed_value)

# Iterating through keys and values in the hashmap
print("Iterating through keys and values:")
for key, value in my_hashmap.items():
    print(f"Key: {key}, Value: {value}")
