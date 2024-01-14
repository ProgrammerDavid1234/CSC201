def calculate_cgpa():
    total_credit_units = 0
    total_grade_points = 0

    num_semesters = int(input("Enter the number of semesters: "))

    for semester in range(1, num_semesters + 1):
        print(f"\nSemester {semester}:")
        num_courses = int(input("Enter the number of courses: "))

        for course in range(1, num_courses + 1):
            grade = input(f"Enter the grade for Course {course} (A, B, C, D, E, F): ").upper()
            credit_unit = int(input(f"Enter the credit unit for Course {course}: "))

            if grade == 'A':
                grade_points = 5.0
            elif grade == 'B':
                grade_points = 4.0
            elif grade == 'C':
                grade_points = 3.0
            elif grade == 'D':
                grade_points = 2.0
            elif grade == 'E':
                grade_points = 1.0
            elif grade == 'F':
                grade_points = 0.0
            else:
                print("Invalid grade entered. Please enter A, B, C, D, E, or F.")
                


            total_grade_points += grade_points * credit_unit
            total_credit_units += credit_unit

    



calculate_cgpa()
