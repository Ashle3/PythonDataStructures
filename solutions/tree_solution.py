#Solution to the problem in the tree lesson

# declare the BST class
class BST:
    # declare the Node class
    class Node:
        
        # this function initializes a new node that we can enter into a tree
        def __init__(self, value):
            
            # initializes the value of the new node
            self.value = value
            # initializes the pointer to the left subtree
            self.left = None
            # initializes the pointer to the right subtree
            self.right = None
    
    # initializes an empty BST
    def __init__(self):
        self.root = None


    def __iter__(self):

        yield from self._traverse_forward(self.root)  # Start at the root

        
    def _traverse_forward(self, node):
        
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)


    def insert(self, new_node):
        # if there isn't a root node, make the value of the new node the root node
        if self.root is None:
            self.root = BST.Node(new_node)
        # if there is a root
        else:
            # call the second __insert function
            self.__insert(new_node, self.root)


    def __insert(self, new_node, current_node):

        if new_node < current_node.value:
            # if the left node is empty
            if current_node.left is None:
                # make the new node the new current_node.left
                current_node.left = BST.Node(new_node)
            else:
            # recursively call the __insert function
                self.__insert(new_node, current_node.left)
        elif new_node == current_node.value:
            pass #move on if the new node is the same as the current node
        else: #if new_node > current_node.value
            #if the right node is empty
            if current_node.right is None:
                # make the new node the new current_node.right
                current_node.right = BST.Node(new_node)
            else:
            # recursively call the __insert function
                self.__insert(new_node, current_node.right)