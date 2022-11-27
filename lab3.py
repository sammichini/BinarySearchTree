#  TODO: Add docstrings, tests, and other reqs

class Node(object):
    """
    Attributes:
    --------------
    parent: node
    left: node
    right: node
    data: int or float
    """

    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    """
    Attributes
    --------------
    root : node


    Methods
    --------------
    print()
        Prints nodes in order
    insert(data)
        inserts node such that BST property is maintained
    min()
        Return the min node's data or None on empty tree
    max()
        Return the max node's data or None on empty tree
    contains()
        uses private method .__find_node to return True if found, False otherwise
    __iter__
        returns nodes in order for iteration
    inorder()
        uses .__traverse, a generator, to return inorder traversal of nodes
    postorder()
        return postorder traversal of nodes
    preorder()
        return preorder traversal of nodes
    find_successor(data)
        finds the node with minimum value which is greater than input data -or- left child of node's parent
    delete(data)
        goes through the tree and deletes node with given data, maintains BST property with .__transplant(node1, node2)

    """
    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)


    def __print(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)
            

    def insert(self, data):
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is None, calling n.data will cause an error
        # Algorithm from CLRS
        if type(data) is not int and type(data) is not float:
            raise TypeError("Please only insert numbers.")

        y = None
        x = self.root
        node = Node(data)
        while x:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

    def min(self):
        # Returns the minimum value held in the tree
        # Returns None if the tree is empty
        if self.root is None:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node.data




    def max(self):
        # Returns the maximum value held in the tree
        # Returns None if the tree is empty
        if self.root is None:
            return None
        node = self.root
        while node.right:

            node = node.right
        return node.data

    def __find_node(self, data):
        # returns the node with that particular data value else returns None
        if self.root is None:
            return None
        node = self.root
        while node and data != node.data:
            if data < node.data:
                node = node.left
            else:
                node = node.right
        return node

    def contains(self, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        node = self.__find_node(data)
        if node:
            return True
        return False


    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop

        # iterate thru tree defaults to inorder trav

        return self.inorder()



    def inorder(self):
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        # helper method implemented using generators
        # all the traversals can be implemented using a single method

        # recursive generator
        if curr_node:
            if traversal_type == self.PREORDER:
                yield curr_node.data
                yield from self.__traverse(curr_node.left, self.PREORDER)
                yield from self.__traverse(curr_node.right, self.PREORDER)

            elif traversal_type == self.INORDER:
                yield from self.__traverse(curr_node.left, self.INORDER)
                yield curr_node.data
                yield from self.__traverse(curr_node.right, self.INORDER)

            elif traversal_type == self.POSTORDER:
                yield from self.__traverse(curr_node.left, self.POSTORDER)
                yield from self.__traverse(curr_node.right, self.POSTORDER)
                yield curr_node.data

        #Yield data of the correct node/s


    def find_successor(self, data):
        # Find the successor node
        # If the value specified by find_successor does NOT exist in the tree, then raise a KeyError
        # helper method to implement the delete method but may be called on its own
        # If the right subtree of the node is nonempty,then the successor is just 
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty, then go up the tree until a node that is
        # the left child of its parent is encountered. The parent of the found node will be the
        # successor to the initial node.
        # Note: Make sure to handle the case where the parent is None
    
    	# Return object of successor if found else return None
        if self.contains(data) is False:
            raise KeyError("Key Error: Node does not exist!")
        node = self.__find_node(data)
        tree = Tree()
        tree.root = node.right
        if tree.root:
            min = tree.min()
            min_node = self.__find_node(min)
            return min_node
        else:
            y = node.parent
            while y and node == y.right:
                node = y
                y = y.parent
            return y


    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does NOT exist in the tree, then don't change the tree and raise a KeyError
        # If you find the node and ...
        #  a) The node has no children, just set its parent's pointer to None.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Note: Make sure to handle the case where the parent is None
        # Algorithm from CLRS
        if self.contains(data) is False:
            raise KeyError("Key Error: Node does not exist!")
        node = self.__find_node(data)

        if node.left is None:
            self.__transplant(node, node.right)

        elif node.right is None:
            self.__transplant(node, node.left)
        else:
            tree = Tree()
            tree.root = node.right
            min = tree.min()
            y = self.__find_node(min)


            if y != node.right:
                self.__transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.__transplant(node, y)
            y.left = node.left
            y.left.parent = y


    def __transplant(self, u, v):
        """"""
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent
