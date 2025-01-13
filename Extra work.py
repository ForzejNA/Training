def calculate_average_grade(grades, students):
    average_grades = {}

    for i in range(len(grades)):
        student_grade = sum(grades[i]) / len(grades[i])
        average_grades[list(students)[i]] = student_grade

    return average_grades


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average_grades = calculate_average_grade(grades, students)
print(average_grades)

def calculate_average_grade(grades, students)
    for i in range(len(grades))