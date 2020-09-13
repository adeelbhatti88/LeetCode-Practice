class Node:
    def init (self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        #inserting data into tree
        #first checking if the root is empty if it is, we insert the data into it.
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)


    def _insert(self, data, cur_node):
        #if the data is smaller then the current root node
        if data < cur_node.data:
            #if there is no root value
            if cur_node.left is None:
                #we set the value
                cur_node.left = Node(data)
                #else we move through the left part of the tree recursivley
            else:
                #we recursivley call this function because the data is smaller then the root
                #so it needs to be placed in the left part of the BST
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else
                self.insert(data, cur_node.right)
        else:
            print("value is already present in tree.")


    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            #if the function rerturned something, then it's true and this will return True
            if is_found:
                return True
            #if no value is found, return false.
            else:
                return None

    def _find(self, data, cur_node):
        #if the data is bigger then the current node data and the node has a right child
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data,cur_node.left)
        if data == cur_node.data:
            return True





