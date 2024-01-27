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

    def dfs(self, visited):
        
        if visited is None:
            visited = []
        stack = [self]
        
        while stack:
            current_node = stack.pop()
            visited.append(current_node.data)
            
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
        return visited
            
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for number in elements:
        root.add_child(number)

    return root

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7]
    numbers_trees = build_tree(numbers)
    print(numbers_trees.dfs([]))
    