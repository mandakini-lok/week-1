
# Student Grade Calculator
# Week 2 - Python Basics

# Function to calculate grade
def calculate_grade(marks):

    if marks >= 90:
        return "A", "Excellent! Keep it up!"

    elif marks >= 80:
        return "B", "Very Good! Keep it up!"

    elif marks >= 70:
        return "C", "Good Job! Keep practicing!"

    elif marks >= 60:
        return "D", "You can do better!"

    else:
        return "F", "Don't Give Up! Try Again!"


# Get student name
student_name = input("Enter student name: ")

# Validate marks using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("Invalid marks! Enter marks between 0 and 100.")

    except ValueError:
        print("Please enter numbers only!")

# Calculate grade
grade, message = calculate_grade(marks)

# Display result
print("\n========== STUDENT RESULT ==========")
print("Student Name:", student_name.upper())
print("Marks:", str(marks) + "/100")
print("Grade:", grade)
print("Message:", message)
print("====================================")
