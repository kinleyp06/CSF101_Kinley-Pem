class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))
    
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
    
    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    # Additional exercises
    def find_middle(self):
        if not self.head:
            return None
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def has_cycle(self):
        if not self.head:
            return False
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    
    def remove_duplicates(self):
        if not self.head:
            return
        
        seen = set()
        current = self.head
        prev = None
        
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next
    
    def merge_sorted_lists(self, other_list):
        dummy = Node(0)
        current = dummy
        list1 = self.head
        list2 = other_list.head
        
        while list1 and list2:
            if list1.data <= list2.data:
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
        
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

# LeetCode Problem 1: Reverse Linked List
def reverseList(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev

# LeetCode Problem 2: Merge Two Sorted Lists
def mergeTwoLists(list1, list2):
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

# LeetCode Problem 3: Remove Nth Node From End of List
def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    
    for _ in range(n):
        fast = fast.next
    
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next
    
    return dummy.next

# ListNode class for LeetCode problems
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create linked list from list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test the implementations
if __name__ == "__main__":
    print("Testing LinkedList implementation:")
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.display()
    
    print("\nTesting reverse method:")
    ll.reverse()
    ll.display()
    
    print("\nTesting find_middle method:")
    print("Middle element:", ll.find_middle())
    
    print("\nTesting has_cycle method:")
    print("Has cycle:", ll.has_cycle())
    
    print("\nTesting remove_duplicates method:")
    ll_with_duplicates = LinkedList()
    ll_with_duplicates.append(1)
    ll_with_duplicates.append(2)
    ll_with_duplicates.append(2)
    ll_with_duplicates.append(3)
    ll_with_duplicates.append(4)
    ll_with_duplicates.append(4)
    ll_with_duplicates.append(4)
    ll_with_duplicates.append(5)
    print("Before removing duplicates:")
    ll_with_duplicates.display()
    ll_with_duplicates.remove_duplicates()
    print("After removing duplicates:")
    ll_with_duplicates.display()
    
    print("\nTesting merge_sorted_lists method:")
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)
    
    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)
    
    print("List 1:")
    list1.display()
    print("List 2:")
    list2.display()
    
    merged = list1.merge_sorted_lists(list2)
    print("Merged list:")
    merged.display()
    
    print("\nTesting LeetCode problems:")
    
    # Test Reverse Linked List
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverseList(head)
    print("Reverse Linked List:", linked_list_to_list(reversed_head))
    
    # Test Merge Two Sorted Lists
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = mergeTwoLists(list1, list2)
    print("Merge Two Sorted Lists:", linked_list_to_list(merged))
    
    # Test Remove Nth Node From End of List
    head = create_linked_list([1, 2, 3, 4, 5])
    result = removeNthFromEnd(head, 2)
    print("Remove Nth Node From End of List:", linked_list_to_list(result))