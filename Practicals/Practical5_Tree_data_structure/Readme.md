# Practical 5 Implementing a Binary Search Tree

## **Objective**
In this lab, you will implement a Binary Search Tree (BST) in Python, including methods for insertion, deletion, search, and various traversal operations. This exercise will help you understand tree data structures and practice recursive algorithms.

**Submission Date: November 1st**

## **Prerequisites**
- Basic knowledge of Python syntax
- Understanding of recursive functions
- Familiarity with tree data structures (conceptual understanding)

## **Lab Steps**

### **Step 1: Define the Node Class**
First, let's define a class for the nodes of our BST:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

### **Step 2: Implement the Binary Search Tree Class**
Now, let's create the BST class with a constructor:

```python
class BinarySearchTree:
    def __init__(self):
        self.root = None
```

### **Step 3: Implement the Insertion Method**
Let's implement the insertion method:

```python
class BinarySearchTree:
    # ... (previous code)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

# Test insertion
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)
```

### **Step 4: Implement the Search Method**
Now, let's implement the search method:

```python
class BinarySearchTree:
    # ... (previous code)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

# Test search
print(bst.search(4))  # Should return a Node
print(bst.search(9))  # Should return None
```

### **Step 5: Implement Traversal Methods**
Let's implement in-order, pre-order, and post-order traversals:

```python
class BinarySearchTree:
    # ... (previous code)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

# Test traversals
print("In-order:", bst.inorder_traversal())
print("Pre-order:", bst.preorder_traversal())
print("Post-order:", bst.postorder_traversal())
```

### **Step 6: Implement the Deletion Method**
Finally, let's implement the deletion method:

```python
class BinarySearchTree:
    # ... (previous code)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            node.value = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

# Test deletion
bst.delete(3)
print("After deleting 3:", bst.inorder_traversal())
```