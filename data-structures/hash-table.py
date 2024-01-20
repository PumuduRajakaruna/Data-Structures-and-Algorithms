class Node:
    def __init__(self, key,value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        h=0
        for char in key:
            h = h + ord(char)
        return h%100

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    # If key already exists, update the value
                    current.value = value
                    return
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        # Key not found
        return None
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        previous = None
        while current:
            if current.key == key and previous is not None:
                previous.next = current.next
                return
            elif current.key == key and previous is None:
                self.table[index] = current.next
                return
            else:
                previous = current
                current = current.next
    def display(self):
        for i in range(self.size):
            print(f"Index {i}: ", end="")
            current = self.table[i]
            while current:
                print(f"({current.key}, {current.value})", end=" -> ")
                current = current.next
            print("None")

# Example usage:
hash_table = HashTable()

hash_table.insert("apple", "A fruit")
hash_table.insert("banana", "Yellow fruit")
hash_table.insert("orange", "Orange fruit")
hash_table.insert("grape", "Small fruit")
hash_table.insert("leppa", "Not a real fruit but collides with 'apple'")  # Collision with "apple"


hash_table.display()

print("Value for key 'banana':", hash_table.get("banana"))
print("Value for key 'apple':", hash_table.get("apple"))
print("Value for key 'orange':", hash_table.get("orange"))
print("Value for key 'grape':", hash_table.get("grape"))

hash_table.delete("banana")
print("\nAfter removing key 'banana':")
hash_table.display()