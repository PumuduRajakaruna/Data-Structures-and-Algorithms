class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return removed_item
        else:
            print("Queue is empty.")

    def size(self):
        current_node = self.front
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

# Example usage:
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())

print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())

print("Queue size:", queue.size())
