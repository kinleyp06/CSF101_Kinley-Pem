# Practical 4: Singly Linked List Implementation

## **Objective**
In this lab, you will implement a singly linked list data structure in Python. You'll create basic operations and list manipulation functions, gaining a deeper understanding of linked data structures and their operations.

## **Prerequisites**
- Basic knowledge of Python syntax
- Understanding of classes
- Familiarity with data structures concepts

## **Part 1: Singly Linked List Implementation**

### **Step 1: Define the Node Class**
First, let's create a Node class to represent individual elements in our linked list:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### **Step 2: Create the LinkedList Class**
Now, let's create the LinkedList class with a constructor:

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

### **Step 3: Implement the Append Method**
Let's add a method to append nodes to the end of the list:

```python
class LinkedList:
    # ... (previous code)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Test the append method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
```

### **Step 4: Implement the Display Method**
Now, let's add a method to display the list contents:

```python
class LinkedList:
    # ... (previous code)

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

# Test the display method
ll.display()  # Output: 1 -> 2 -> 3
```

### **Step 5: Implement the Insert Method**
Let's add a method to insert a node at a specific position:

```python
class LinkedList:
    # ... (previous code)

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

# Test the insert method
ll.insert(4, 1)
ll.display()  # Output: 1 -> 4 -> 2 -> 3
```

### **Step 6: Implement the Delete Method**
Now, let's implement a method to delete a node by its value:

```python
class LinkedList:
    # ... (previous code)

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

# Test the delete method
ll.delete(2)
ll.display()  # Output: 1 -> 4 -> 3
```

### **Step 7: Implement the Search Method**
Let's add a method to search for a value in the list:

```python
class LinkedList:
    # ... (previous code)

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

# Test the search method
print(ll.search(4))  # Output: 1
print(ll.search(5))  # Output: -1
```

### **Step 8: Implement the Reverse Method**
Finally, let's add a method to reverse the linked list:

```python
class LinkedList:
    # ... (previous code)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Test the reverse method
ll.reverse()
ll.display()  # Output: 3 -> 4 -> 1
```

## **Part 2: Reverse Linked List**

### **1. Problem Statement**
Given the head of a singly linked list, reverse the list, and return the reversed list.

**Example 1:**
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**
```
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**
```
Input: head = []
Output: []
```

**Constraints:**
- The number of nodes in the list is the range [0, 5000]
- -5000 <= Node.val <= 5000

### **2. Conceptual Understanding**
A linked list is a data structure where each element (node) contains a value and a reference (or link) to the next node in the sequence. Reversing a linked list means changing these links so that each node points to its previous node instead of its next node.

We'll focus on the iterative approach as it's often the most intuitive and efficient:

1. Initialize three pointers: `prev` as None, `current` as the head of the list, and `next` as None
2. Traverse the list:
   - Save the next node
   - Reverse the current node's pointer to point to the previous node
   - Move `prev` and `current` one step forward
3. Return `prev` as the new head of the reversed list

### **3. Python Implementation**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    
    while current is not None:
        next_temp = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev one step
        current = next_temp       # Move current one step
    
    return prev  # prev is the new head of the reversed list
```

## **Part 3: Merge Two Sorted Lists**

### **1. Problem Statement**
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

**Example 1:**
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**
```
Input: list1 = [], list2 = []
Output: []
```

**Example 3:**
```
Input: list1 = [], list2 = [0]
Output: [0]
```

**Constraints:**
- The number of nodes in both lists is in the range [0, 50]
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order

### **2. Conceptual Understanding**
This problem involves working with linked lists, a fundamental data structure in computer science. The task is to combine two already sorted linked lists into a single sorted linked list.

We'll use the in-place merge approach:

1. Create a dummy node as the start of our result list
2. Use a pointer to keep track of where we're inserting nodes
3. Iterate through both lists simultaneously:
   - Compare the current nodes of both lists
   - Append the smaller node to our result list
   - Move forward in the list we took the node from
4. If one list is exhausted, append the remainder of the other list
5. Return the next node after the dummy node (the actual head of our merged list)

### **3. Python Implementation**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    return dummy.next
```

## **Part 4: Remove Nth Node From End of List**

### **1. Problem Statement**
Given the head of a linked list, remove the nth node from the end of the list and return its head.

**Example 1:**
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Example 2:**
```
Input: head = [1], n = 1
Output: []
```

**Example 3:**
```
Input: head = [1,2], n = 1
Output: [1]
```

**Constraints:**
- The number of nodes in the list is sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

### **2. Conceptual Understanding**
This problem involves manipulating a linked list, which is a linear data structure where elements are stored in nodes. Each node contains a data field and a reference (or link) to the next node in the sequence.

We'll use the one-pass algorithm with two pointers:

1. Initialize two pointers, `fast` and `slow`, to the head of the list
2. Move `fast` n nodes ahead
3. If `fast` is null, it means we need to remove the head. Return head.next
4. Move both `fast` and `slow` until `fast` reaches the last node
5. Now, `slow` is just before the node we want to remove
6. Update `slow.next` to skip the next node (effectively removing it)
7. Return the head of the modified list

### **3. Python Implementation**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    
    # Move fast pointer n nodes ahead
    for _ in range(n):
        fast = fast.next
    
    # Move both pointers until fast reaches the end
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    # Remove the nth node
    slow.next = slow.next.next
    
    return dummy.next
```