### **Main Concepts Applied**

**1. Recursive Implementation:**
*   **Recursion:** The function solves the problem by calling itself with smaller inputs (`n-1` and `n-2`).
*   **Base Case:** The fundamental building blocks of the sequence that terminate the recursion (`if n == 0: return 0; if n == 1: return 1`).
*   **Call Stack Management:** Each recursive call adds a new frame to the call stack, which is unwound once the base cases are reached and return their values.

**2. Iterative Implementation:**
*   **Iteration (Looping):** A `for` loop is used to build the solution sequentially from the base cases up to the desired result.
*   **State Management:** Two variables (`a` and `b`) are used to track the previous two Fibonacci numbers, and their state is updated in each iteration of the loop to compute the next number.
*   **Algorithmic Efficiency:** This approach uses a linear process (O(n) time complexity), which is significantly more efficient for this problem than the naive recursive method.

