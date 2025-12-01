# Practical 8: Stacks and Queues - Reflection

## **Documentation**

### **Main Concepts Applied**

#### **1. Stack Implementation:**
* **LIFO (Last-In-First-Out) Principle:** The most recently added element is the first to be removed, implemented using Python's list where `append()` adds to the end and `pop()` removes from the end.
* **Core Operations:** 
  - `push(item)`: Adds an element to the top of the stack
  - `pop()`: Removes and returns the top element
  - `peek()`: Returns the top element without removing it
  - `is_empty()`: Checks if the stack is empty
  - `size()`: Returns the number of elements

#### **2. Queue Implementation:**
* **FIFO (First-In-First-Out) Principle:** The first added element is the first to be removed, implemented using `append()` to add to the end and `pop(0)` to remove from the front.
* **Core Operations:**
  - `enqueue(item)`: Adds an element to the back of the queue
  - `dequeue()`: Removes and returns the front element
  - `front()`: Returns the front element without removing it
  - `is_empty()`: Checks if the queue is empty
  - `size()`: Returns the number of elements

#### **3. LeetCode Problems Solved:**

**Problem 1: Implement Stack using Queues**
```python
class MyStack:
    def __init__(self):
        self.queue = []
    
    def push(self, x: int) -> None:
        # Add new element to queue
        self.queue.append(x)
        # Rotate all previous elements to maintain stack order
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
    
    def pop(self) -> int:
        return self.queue.pop(0) if self.queue else -1
    
    def top(self) -> int:
        return self.queue[0] if self.queue else -1
    
    def empty(self) -> bool:
        return len(self.queue) == 0
```

**Problem 2: Valid Parentheses**
```python
def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():  # Opening bracket
            stack.append(char)
        elif char in mapping.keys():  # Closing bracket
            if not stack or stack.pop() != mapping[char]:
                return False
        else:  # Invalid character
            return False
    
    return len(stack) == 0
```

## **Reflection**

### **What I Learned**

#### **1. Understanding Abstract Data Types (ADTs):**
- Stacks and queues are abstract data types defined by their behavior, not their implementation
- The same ADT can be implemented using different underlying data structures (lists, linked lists, arrays)
- This separation of interface and implementation is crucial in software design

#### **2. Time Complexity Insights:**
- Stack operations (`push`, `pop`, `peek`) are O(1) when implemented with lists
- Queue's `dequeue()` operation using `pop(0)` is O(n) due to shifting elements
- Learned that collections.deque provides O(1) operations for both ends:
```python
from collections import deque

class OptimizedQueue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)  # O(1)
    
    def dequeue(self):
        return self.items.popleft()  # O(1)
```

#### **3. Real-world Applications:**
- **Stack Applications:**
  - Function call management (call stack)
  - Undo/Redo functionality in editors
  - Expression evaluation (postfix notation)
  - Back/Forward navigation in browsers

- **Queue Applications:**
  - Task scheduling in operating systems
  - Print spooling
  - Message queues in distributed systems
  - Breadth-First Search (BFS) in graphs

#### **4. Algorithm Design Patterns:**
- **Stack for Parentheses Matching:** The ability to match opening and closing symbols using LIFO behavior
- **Queue Rotation Technique:** Implementing stack operations using queue rotation (push(x) -> O(n), pop() -> O(1))
- **Alternative Approach:** Could also implement with two queues for different trade-offs

### **Challenges Faced and Solutions**

#### **Challenge 1: Understanding the "Stack using Queues" Problem**
**Problem:** Initially confused about how to implement LIFO behavior using only FIFO queues.

**Solution Breakdown:**
1. **Single Queue Approach:** Each push operation requires rotating all existing elements
```python
def push(self, x):
    self.queue.append(x)
    # Rotate to make new element at front
    for _ in range(len(self.queue) - 1):
        self.queue.append(self.queue.pop(0))
```
2. **Two Queue Approach:** Alternative implementation with better push/pop trade-offs
```python
class MyStackTwoQueues:
    def __init__(self):
        self.main_queue = []
        self.temp_queue = []
    
    def push(self, x):
        self.temp_queue.append(x)
        # Move all elements from main to temp
        while self.main_queue:
            self.temp_queue.append(self.main_queue.pop(0))
        # Swap queues
        self.main_queue, self.temp_queue = self.temp_queue, []
```

#### **Challenge 2: Edge Cases in Parentheses Validation**
**Problem:** Initially missed several edge cases:
- Empty string should return True
- Strings with only opening brackets
- Strings with only closing brackets
- Nested valid parentheses

**Solution:** Systematic test cases:
```python
test_cases = [
    ("()", True),           # Simple case
    ("()[]{}", True),       # Multiple types
    ("(]", False),          # Mismatched types
    ("([)]", False),        # Wrong nesting order
    ("{[]}", True),         # Nested valid
    ("", True),             # Empty string
    ("(", False),           # Only opening
    (")", False),           # Only closing
]
```

#### **Challenge 3: Performance Optimization**
**Problem:** The queue implementation using `pop(0)` has O(n) dequeue operation.

**Solution Alternatives:**
1. **Using collections.deque:** Provides O(1) operations for both ends
2. **Circular Buffer:** Implement with fixed-size array and pointers
3. **Linked List:** Each node points to the next, O(1) enqueue/dequeue

#### **Challenge 4: Debugging Complex Parentheses Patterns**
**Problem:** With complex nested patterns, it was difficult to trace why certain inputs failed.

**Solution:** Added visualization:
```python
def isValid_with_trace(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    print(f"Input: {s}")
    for i, char in enumerate(s):
        if char in mapping.values():
            stack.append(char)
            print(f"Step {i}: Push '{char}' -> Stack: {stack}")
        else:
            if not stack:
                print(f"Step {i}: Empty stack, closing '{char}' -> INVALID")
                return False
            top = stack.pop()
            if top != mapping[char]:
                print(f"Step {i}: Popped '{top}', expected '{mapping[char]}' -> INVALID")
                return False
            print(f"Step {i}: Pop matches '{char}' -> Stack: {stack}")
    
    result = len(stack) == 0
    print(f"Final: Stack {'empty' if result else 'not empty'} -> {result}")
    return result
```

### **Key Insights Gained**

#### **1. Trade-offs in Implementation Choices:**
- Python lists are efficient for stacks but inefficient for queues
- The choice between single queue vs. two queues for stack implementation depends on usage patterns
- Error handling (raising exceptions vs. returning sentinel values) depends on context

#### **2. Problem-Solving Strategies:**
- **Pattern Recognition:** Parentheses matching is a classic stack problem
- **Simulation:** Working through examples step-by-step reveals algorithm logic
- **Optimization:** Understanding when to optimize and what to optimize

#### **3. Testing Methodology:**
```python
# Comprehensive testing approach learned
def test_stack_implementation():
    stack = Stack()
    
    # Test 1: Basic operations
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.peek() == 1
    
    # Test 2: Empty stack handling
    stack.pop()
    try:
        stack.pop()
        assert False, "Should have raised exception"
    except IndexError:
        pass
    
    # Test 3: Size tracking
    for i in range(5):
        stack.push(i)
    assert stack.size() == 5
```

### **Conclusion**

This practical provided deep insights into fundamental data structures that form the backbone of many algorithms and systems. The most valuable lesson was understanding how abstract behaviors (LIFO/FIFO) can be implemented in multiple ways, each with different performance characteristics. The LeetCode problems bridged theoretical knowledge with practical problem-solving, demonstrating how these data structures solve real-world problems like syntax validation.

The experience highlighted the importance of:
1. Choosing the right data structure for the problem
2. Considering edge cases and error conditions
3. Understanding time/space complexity trade-offs
4. Applying systematic debugging and testing approaches

These concepts are foundational for more advanced topics like trees, graphs, and dynamic programming, making this practical essential building block in my computer science education.