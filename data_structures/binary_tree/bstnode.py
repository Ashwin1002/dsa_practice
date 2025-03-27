class BSTNode:
    """
        A class representing a node in a Binary Search Tree (BST).
        The `BSTNode` class provides methods for common operations on a binary search tree,
        including insertion, deletion, traversal, and searching. Each node in the tree contains
        a value (`val`) and pointers to its left and right children (`left` and `right`).
        Attributes:
            val (Any): The value stored in the node. Defaults to None.
            left (BSTNode): Pointer to the left child of the node. Defaults to None.
            right (BSTNode): Pointer to the right child of the node. Defaults to None.
        Methods:
            __init__(val=None):
                Initializes a new instance of the `BSTNode` class with an optional value.
            search_range(lower_bound, upper_bound):
                Searches for all values within a specified range [lower_bound, upper_bound]
                in the binary search tree using in-order traversal.
            exists(val):
                Checks if a value exists in the binary search tree.
            inorder(visited):
                Performs an in-order traversal of the binary search tree and appends
                the values of visited nodes to a provided list.
            postorder(visited):
                Performs a postorder traversal of the binary search tree and appends
                the values of visited nodes to a provided list.
            preorder(visited):
                Performs a preorder traversal of the binary search tree and appends
                the values of visited nodes to a provided list.
            height():
                Calculates the height of the binary search tree or subtree rooted at the current node.
            get_min():
                Finds and returns the minimum value in the binary search tree.
            get_max():
                Finds and returns the maximum value in the binary search tree.
            insert(val):
                Inserts a value into the binary search tree while maintaining the BST property.
            delete(val):
                Deletes a node with the specified value from the binary search tree while
                maintaining the BST property.
    """

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def search_range(self, lower_bound, upper_bound):   
        """
        Searches for all values within the specified range [lower_bound, upper_bound] 
        in the binary search tree (BST) using an in-order traversal.
        Args:
            lower_bound (int): The lower bound of the range (inclusive).
            upper_bound (int): The upper bound of the range (inclusive).
        Returns:
            list: A list of values within the specified range, sorted in ascending order.
        """
        result = []
    
        def inorder_traverse(node):
            if not node:
                return
            
            # Only search left if there's a chance of finding values within the range
            if node.val >= lower_bound and node.left:
                inorder_traverse(node.left)
    
            # Include the current node if its User ID is within the range
            if lower_bound <= node.val <= upper_bound:
                result.append(node.val)  # Append the User object, not BSTNode
    
            # Only search right if there's a chance of finding values within the range
            if node.val <= upper_bound and node.right:
                inorder_traverse(node.right)
    
        inorder_traverse(self)  # Start traversal from the current node
        return result  # Returns a list of User objects

    def exists(self, val):
        """
        Checks if a value exists in the binary tree.

        Args:
            val (Any): The value to search for in the binary tree.

        Returns:
            bool: True if the value exists in the tree, False otherwise.

        Notes:
            - If the tree is empty (root node is None), the method returns False.
            - The method performs a binary search, checking the left or right
              subtree based on the comparison of the value with the current node's value.
        """
        if self.val is None:
            return False  # Tree is empty

        if self.val == val:
            return True  # Value found

        if val < self.val:
            return self.left.exists(val) if self.left else False  # Search left

        return self.right.exists(val) if self.right else False  # Search right

    def inorder(self, visited):
        """
        Perform an in-order traversal of the binary tree.

        In-order traversal visits the left subtree, the current node, and then the right subtree.
        The values of the visited nodes are appended to the provided list.

        Args:
            visited (list): A list to store the values of the nodes in in-order sequence.

        Returns:
            list: The updated list containing the values of the nodes in in-order sequence.
        """
        if self.left:
            self.left.inorder(visited)
        if self.val:
            visited.append(self.val)
        if self.right:
            self.right.inorder(visited)
        return visited

    def postorder(self, visited):
        """
        Perform a postorder traversal of the binary tree.

        In postorder traversal, the nodes are recursively visited in the following order:
        1. Left subtree
        2. Right subtree
        3. Current node

        Args:
            visited (list): A list to store the values of the nodes in the order they are visited.

        Returns:
            list: The updated list containing the values of the nodes in postorder traversal order.
        """
        if self.left:
            self.left.postorder(visited)
        if self.right:
            self.right.postorder(visited)
        if self.val:
            visited.append(self.val)
        return visited

    def preorder(self, visited):
        """
        Perform a preorder traversal of the binary tree.

        In a preorder traversal, the current node is visited first, 
        followed by the left subtree, and then the right subtree.

        Args:
            visited (list): A list to store the values of the visited nodes 
                            in preorder sequence.

        Returns:
            list: The updated list of visited nodes in preorder sequence.
        """
        if self.val is not None:
            visited.append(self.val)  # Visit the current node
            if self.left:
                self.left.preorder(visited)  # Traverse the left subtree
            if self.right:
                self.right.preorder(visited)  # Traverse the right subtree
        return visited
     
    def height(self):
        """
        Calculate the height of the binary tree or subtree rooted at the current node.
        The height of a binary tree is defined as the number of edges on the longest
        path from the current node to a leaf node. An empty tree or node has a height of 0.
        Returns:
            int: The height of the binary tree or subtree. If the current node is None,
            the height is 0. Otherwise, it is 1 plus the maximum of the heights of the
            left and right subtrees.
        """
        if self.val is None:
            return 0  # An empty node or tree has height 0
        
        # Recursively calculate the height of the left and right subtrees
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        
        # The height of the current node is 1 plus the maximum of the heights of its left and right subtrees
        return max(left_height, right_height) + 1
    
    def get_min(self):
        """
        Finds and returns the minimum value in the binary tree.

        This method recursively traverses the left subtree of the binary tree
        to find the smallest value, as the minimum value in a binary search tree
        is always located in the leftmost node.

        Returns:
            The minimum value (self.val) in the binary tree.
        """
        if self.left:
            return self.left.get_min()
        return self.val

    def get_max(self):
        """
        Finds and returns the maximum value in the binary tree.

        This method traverses the right subtree of the binary tree recursively,
        as the maximum value in a binary search tree is located at the rightmost node.
        If there is no right child, the current node's value is returned.

        Returns:
            The maximum value stored in the binary tree.
        """
        if self.right:
            return self.right.get_max()
        return self.val

    def insert(self, val):
        """
        Inserts a value into the binary search tree (BST) while maintaining the BST property.

        Args:
            val (int): The value to be inserted into the tree.

        Behavior:
            - If the current node's value is None, the value is assigned to the current node.
            - If the value already exists in the tree, no action is taken (duplicates are not allowed).
            - If the value is less than the current node's value, it is inserted into the left subtree.
            - If the value is greater than the current node's value, it is inserted into the right subtree.

        Raises:
            None
        """
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
    
    def delete(self, val):
        """
        Deletes a node with the specified value from the binary tree.

        This method removes a node with the given value from the binary tree while
        maintaining the binary search tree property. If the value is not found in
        the tree, the tree remains unchanged.

        Args:
            val (int): The value of the node to be deleted.

        Returns:
            Node: The root of the modified subtree after deletion. If the node to
            be deleted is the root and has no children, returns None.

        Behavior:
            - If the value is less than the current node's value, the method
              recursively calls delete on the left subtree.
            - If the value is greater than the current node's value, the method
              recursively calls delete on the right subtree.
            - If the value matches the current node's value:
                - If the node has no right child, it is replaced by its left child.
                - If the node has no left child, it is replaced by its right child.
                - If the node has both children, it is replaced by the smallest
                  value in its right subtree, and that node is subsequently deleted
                  from the right subtree.
        """
        if not self.val:
            return None

        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self

        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self

        # Node to delete found
        if not self.right:  # No right child, return left child
            return self.left
        if not self.left:  # No left child, return right child
            return self.right

        # Both children exist, find the minimum in the right subtree
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left

        # Replace value with min_larger_node's value
        self.val = min_larger_node.val

        # Delete the min_larger_node from the right subtree
        self.right = self.right.delete(min_larger_node.val)

        return self
