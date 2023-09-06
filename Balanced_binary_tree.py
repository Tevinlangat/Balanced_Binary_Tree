class Solution:
    def isBalanced(self, root) -> bool:
        # Initialize a boolean variable 'balanced' to True.
        self.balanced = True
        
        def dfs(root):
            # Base case: If the current node is None, return a height of 0.
            if not root:
                return 0
            
            # Recursively calculate the heights of the left and right subtrees.
            left = dfs(root.left)
            right = dfs(root.right)

            # Check if the difference in heights exceeds 1, indicating imbalance.
            if abs(left - right) > 1:
                # If an imbalance is found, set 'balanced' to False.
                self.balanced = False

            # Return the height of the current subtree.
            return max(left, right) + 1
        
        # Start the DFS traversal from the root of the tree.
        dfs(root)
        
        # Return the final value of 'balanced', which indicates whether the tree is balanced.
        return self.balanced

# Creating the blue print of the binary tree
class TreeNode:
    def __init__(self, value) :
        self.value = value;
        self.right = None
        self.left = None

# Creating the algorithm of the binary tree
class Binary_Tree:
    def __init__(self): # initiate the root of the binary tree
        self.root = None

    def insert(self,value):
        if self.root is None:
            self.root = TreeNode(value)
        else: self.insert_by_check(self.root, value)
        
    def insert_by_check(self,node,value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else: self.insert_by_check(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else: self.insert_by_check(node.right,value)

    def traverse_tree(self):
        def traverse(node):
            if node:
                traverse(node.left)
                print(node.value, end='')
                traverse(node.right)
            
            traverse(self.root)
            print()



tree = Binary_Tree()
tree.insert(4)
tree.insert(2)
tree.insert(5)
tree.insert(3)
tree.insert(6)

tree.traverse_tree()
