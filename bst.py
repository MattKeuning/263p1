# This is a placeholder

# Class for an individual node in the tree.
# Stores data and various recursive functions
class BST_Node:
  def __init__(self, key):
    self.key = key
    self.left_node = None
    self.right_node = None

  # Prints the subtree in a pretty, indented format
  def print_indent(self, tabs = 0, prefix = ''):
    print('  ' * tabs, end = '')
    print('[' + prefix + ']', end = '')
    print(str(self.key))
    if self.left_node is not None:
      self.left_node.print_indent(tabs + 1, prefix + 'L')
    if self.right_node is not None:
      self.right_node.print_indent(tabs + 1, prefix + 'R')

  # Recursively insert a node with the given key
  def insert(self, key):
    if key < self.key:
      if self.left_node is None:
        self.left_node = BST_Node(key)
      else:
        self.left_node.insert(key)
    else:
      if self.right_node is None:
        self.right_node = BST_Node(key)
      else:
        self.right_node.insert(key)

  # Traverse in standard sorted order
  def traverse_in_order(self):
    if self.left_node is not None:
      self.left_node.traverse_in_order()
    # print this node's value
    print(self.key, end = ' ')
    if self.right_node is not None:
      self.right_node.traverse_in_order()

  # Traverse in a recursive parent, left, right order
  def traverse_pre_order(self):
    # print this node's value
    print(self.key, end = ' ')
    if self.left_node is not None:
      self.left_node.traverse_pre_order()
    if self.right_node is not None:
      self.right_node.traverse_pre_order()

  # Traverse in a recursive left, right, parent order
  def traverse_post_order(self):
    if self.left_node is not None:
      self.left_node.traverse_post_order()
    if self.right_node is not None:
      self.right_node.traverse_post_order()
    # print this node's value
    print(self.key, end = ' ')

# Class for an entire binary search tree
# Mainly operates via recursive functions on the root node
class BST:
  def __init__(self):
    self.root = None

  def get_maximum(self):
    if not self.root:
        return
    else:
        return max(self.root.left_node, self.root.right_node)


  # Insert a node with the given key into the tree
  def insert(self, key):
    if self.root is None:
      self.root = BST_Node(key)
    else:
      self.root.insert(key)

  # Print the entire tree in an informative, indent-based way
  def print_indent(self):
    if self.root is None:
      print('Tree is empty!')
    else:
      self.root.print_indent()

  # Print all keys in the tree in a sorted order
  def traverse_in_order(self):
    print('In order traversal: ', end = '')
    if self.root is not None:
      self.root.traverse_in_order()
    print('') # Add a newline

  # Print all keys in the tree in a parent, left, right order
  def traverse_pre_order(self):
    print('Pre order traversal: ', end = '')
    if self.root is not None:
      self.root.traverse_pre_order()
    print('') # Add a newline

  # Print all keys in the tree in a left, right, parent order
  def traverse_post_order(self):
    print('Post order traversal: ', end = '')
    if self.root is not None:
      self.root.traverse_post_order()
    print('') # Add a newline


# The code below this if statement can be used to test your code locally
#   Anything inside the if will not be executed by the autograder
if __name__ == '__main__':
  bst = BST()
  print("Hello")
