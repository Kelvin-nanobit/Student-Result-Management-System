def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"

student_name = input("Enter student name: ")
score = int(input("Enter student score: "))

grade = calculate_grade(score)

print("Student Name:", student_name)
print("Score:", score)
print("Grade:", grade)
