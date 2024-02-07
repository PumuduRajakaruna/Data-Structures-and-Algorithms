class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def bfs(self):
        queue = [self]  # add the root to the queue 
        elements = []
    
        if queue is None:
            return
       
        while len(queue) > 0:
            
            current_node = queue.pop(0)
            elements.append(current_node.data) 
            
            if current_node.left:
                queue.append(current_node.left)
                
            if current_node.right:
                queue.append(current_node.right)
        
        return elements
            
                        
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for number in elements:
        root.add_child(number)

    return root

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7]
    numbers_trees = build_tree(numbers)
    print(numbers_trees.bfs())
    # print(numbers_trees.in_order_traversal())
    # print(numbers_trees.pre_order_traversal())
    # print(numbers_trees.post_order_traversal())
    # print(numbers_trees.search(4))
