# **Documentation**

### **The main concepts I applied**
1. ***Clarity and Readability:*** The pseudocode and flowchart descriptions are written in simple, clear English. The steps are logical and easy to follow, even for someone new to programming.

2. ***Precision:*** The instructions are unambiguous. For example, the formula for Fahrenheit conversion is written exactly as (celsius * 9/5) + 32, leaving no room for misinterpretation.

3. ***Abstraction:*** We focused on the logic (e.g., "check if a number is even") rather than the implementation details of a specific language (e.g., if(number % 2 == 0) vs if(number & 1 == 0)).

### **Pseudocode Conventions:**

- **Keywords:** Used uppercase keywords like START, END, READ, PRINT, IF, ELSE, ENDIF, AND to make control structures stand out.

- **Indentation:** Used indentation (e.g., inside the IF block) to visually represent the structure and nesting of the code.

### **Flowchart Symbols:** *Correctly applied the standard symbols:*

- Oval for Start/End terminals.

- Parallelogram for all Input (READ) and Output (PRINT) operations.

- Rectangle for Processes (calculations and assignments).

- Diamond for Decision points (conditional checks like IF statements).

### **Basic Structures:**

- ***Sequence:*** Problems 1 and 4 are pure sequences of steps.

- ***Selection*** (Conditionals): Problems 2 and 3 used IF, ELSE IF, and ELSE structures to handle different conditions and branches in the logic. This was represented by Diamond symbols in the flowcharts.

- ***Input/Output:*** Consistently used READ for getting data and PRINT for displaying results, following the pseudocode principles.

- ***Assignment:*** Used the = operator for assignment in processes (e.g., area = length * width).

# **Reflection**

### **What I Learned**
- I was reminded that coding is not the first step in solving a problem; design is. Pseudocode and flowcharts force you to think through the entire logic, handle all edge cases (like which number is largest if two are equal), and create a blueprint. This saves immense time and effort later during implementation and debugging.

-  This was the most significant learning reinforcement. I practiced abstracting a problem from its English description (e.g., "find the largest number") into a precise, step-by-step procedure using logical constructs (sequence, selection) without worrying about semicolons, syntax, or language-specific functions.

- Writing good pseudocode requires careful choice of words. The difference between "check if the number is even" and IF number % 2 == 0 is the difference between an idea and an executable step. I learned to be ruthlessly precise in defining conditions and operations.

- Flowcharts provide a powerful visual metaphor for program flow. Drawing them (even mentally) makes the flow of control—especially the branching paths of IF statements—intuitively clear. It's a universal language that can be understood by technical and non-technical people alike.

- Using the standard symbols (Oval, Diamond, Rectangle, Parallelogram) and conventions (arrows for flow, yes/no labels) ensures that anyone can read and understand the chart. This practice promotes clear communication, which is a critical skill in software development.

## **Challenges Faced and How I Overcame Them**

### ***Challenge 1:*** Choosing the Right Level of Detail
- Initially, I wondered how much detail to include in the pseudocode. Should I explicitly READ each variable on a separate line? Should I define the formula for Fahrenheit as (9/5) or 1.8?

- How I Overcame It: I referred back to the principles in the notes: Clarity and Precision. I chose the version that was most clear and left no room for ambiguity. Using 9/5 is more semantically clear as it matches the standard formula we learn in science, even if 1.8 is computationally identical. For reading inputs, using two READ statements is perfectly clear, but a single READ length, width is also precise and more concise.

### ***Challenge 2:*** Designing the Efficient Conditional Logic
- For the "largest of three numbers" problem, the simplest solution can be inefficient. A naive approach might check every possible pair-wise comparison (e.g., is A>B, is A>C, is B>A, etc.), which is redundant.

- How I Overcame It: I applied logical reasoning to optimize the flowchart and pseudocode. The chosen solution uses a more efficient logic:

  First, check if the first number is the largest.

  If not, the problem is instantly reduced to finding the larger of the remaining two numbers.
  This approach requires fewer comparisons on average. This challenge taught me to not just make the logic work, but to think about making it efficient even at the design stage.

### ***Challenge 3:*** Representing Decisions in a Linear Format
- Describing a multi-branch diamond decision (from the flowchart) in text-based pseudocode can be tricky. Making the ELSE IF structure in the pseudocode visually match the branching of the flowchart was a small but important challenge.

- How I Overcame It: I strictly followed the indentation convention from the provided notes. The clean alignment of IF, ELSE IF, ELSE, and ENDIF creates a visual hierarchy that perfectly mirrors the branches of the flowchart diamond, making the text just as readable.


### ***Challenge 4:*** Tool-Based Flowchart Creation (Hypothetical)
- If I were to use Draw.io or Excalidraw for the first time, a common challenge is navigating the interface—finding the right symbols, connecting them neatly with arrows, and formatting text.

- How I Would Overcome It: I would start by watching a short introductory tutorial for the chosen tool. Most of these platforms have a searchable library of shapes. I would use the text tool inside each shape for labels and the connector tool (usually an arrow icon) to link them. The key is to use the tool's alignment and grid features to keep the flowchart looking clean and professional.

### **Conclusion**
This exercise was a successful practice in foundational software engineering skills. It strengthened my ability to deconstruct problems, design logical solutions, and communicate those solutions effectively using standard, universal methods like pseudocode and flowcharts. The challenges were primarily about thoughtful design and attention to detail, which are muscles every programmer needs to continuously exercise.


