# Student Grade Calculator

## 1. Project Overview

Student Grade Calculator is a simple Python-based project that calculates students' grades based on their examination marks.

The program accepts the student's name and marks from the user and displays the corresponding grade with an encouraging message.

This project helps beginners understand Python programming concepts such as conditional statements, loops, functions, and error handling.

## 2. Project Objectives

- To calculate student grades automatically.
- To understand if-elif-else statements.
- To practice comparison operators.
- To use functions in Python.
- To implement while loops.
- To validate user input.
- To handle errors using try-except.

## 3. Project Features

- Accepts student name.
- Accepts marks between 0 and 100.
- Calculates grades automatically.
- Displays encouraging messages.
- Checks invalid marks.
- Handles incorrect input.
- Uses functions and loops.

## 4. Grading System

| Marks | Grade | Message |
|---|---|---|
| 90–100 | A | Excellent! Keep it up! |
| 80–89 | B | Very Good! Keep it up! |
| 70–79 | C | Good Job! Keep improving! |
| 60–69 | D | You can do better! |
| 0–59 | F | Don't Give Up! Try Again! |

## 5. Technologies Used

- Programming Language: Python
- Code Editor: Visual Studio Code
- Operating System: Windows
- Concepts: If-else, Loops, Functions, Error Handling

## 6. Project Folder Structure

```text
Student_Grade_Calculator/
│
├── grade_calculator.py
├── README.md
├── test_cases.txt
│
└── screenshots/
    ├── 01_python_code.png
    ├── 02_grade_A.png
    ├── 03_grade_B.png
    ├── 04_grade_C.png
    ├── 05_grade_D.png
    ├── 06_grade_F.png
    ├── 07_invalid_marks.png
    └── 08_error_handling.png
```

## 7. Setup Instructions

Step 1: Install Python on your computer.

Step 2: Install Visual Studio Code.

Step 3: Create a folder named Student_Grade_Calculator.

Step 4: Create a Python file named grade_calculator.py.

Step 5: Copy the Python program into the file.

Step 6: Save the file.

## 8. How to Run the Project

1. Open Visual Studio Code.
2. Open the Student_Grade_Calculator folder.
3. Open the Terminal.
4. Type the following command:

```bash
python grade_calculator.py
```

5. Enter the student name.
6. Enter marks between 0 and 100.
7. View the calculated grade and message.

## 9. Functions Used

### calculate_grade(marks)

This function accepts student marks and returns the grade and an encouraging message.

### Input Function

The input() function accepts the student's name and marks.

### Print Function

The print() function displays the final student result.

## 10. Technical Details

### Conditional Statements

The if-elif-else statements are used to determine the student's grade based on marks.

### While Loop

The while loop repeatedly asks the user to enter marks until valid marks are provided.

### Error Handling

The try-except block handles incorrect inputs such as alphabetic characters instead of numbers.

### Input Validation

The program accepts marks only between 0 and 100.

## 11. Sample Output

```text
Enter student name: Priya
Enter marks (0-100): 85

========== STUDENT RESULT ==========
Student Name: PRIYA
Marks: 85 /100
Grade: B
Message: Very Good! Keep it up!
====================================
```

## 12. Testing Details

The program is tested with different marks and invalid inputs.

- 95 marks – Grade A
- 85 marks – Grade B
- 75 marks – Grade C
- 65 marks – Grade D
- 35 marks – Grade F
- 105 marks – Invalid marks
- -5 marks – Invalid marks
- abc – Invalid input

## 13. Screenshots

The screenshots folder contains program code, grade results, and input validation outputs.

These screenshots demonstrate the working of the project.

## 14. Conclusion

The Student Grade Calculator project helped me understand the basic concepts of Python programming.

I learned how to use conditional statements, comparison operators, loops, functions, and error handling.

This project improved my logical thinking and programming skills. It also helped me understand how Python can be used to solve real-life problems.