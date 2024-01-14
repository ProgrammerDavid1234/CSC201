def get_grade_points(grade):
    grade_points = {'A': 5.0, 'B': 4.0, 'C': 3.0, 'D': 2.0, 'E': 1.0, 'F': 0.0}
    return grade_points.get(grade.upper(), 0.0)

def calculate_gpa(credits, grade_points):
    total_credits = sum(credits)
    weighted_grade_points = sum(credit * gp for credit, gp in zip(credits, grade_points))
    gpa = weighted_grade_points / total_credits
    return gpa

def calculate_cgpa(cumulative_credits, cumulative_grade_points):
    total_cumulative_credits = sum(cumulative_credits)
    weighted_cumulative_grade_points = sum(credit * gp for credit, gp in zip(cumulative_credits, cumulative_grade_points))
    cgpa = weighted_cumulative_grade_points / total_cumulative_credits
    return cgpa

def get_user_input_course():
    credit = float(input("Enter credit unit for the course: "))
    grade = input("Enter grade for the course (e.g., A, B, C, D, E, F): ")
    return credit, grade

def main():
    num_semesters = int(input("Enter the number of semesters: "))
    cumulative_credits = []
    cumulative_grade_points = []

    for semester in range(num_semesters):
        print(f"\nSemester {semester + 1}:")
        num_courses = int(input("Enter the number of courses for this semester: "))
        credits = []
        grades = []

        for i in range(num_courses):
            credit, grade = get_user_input_course()
            credits.append(credit)
            grades.append(get_grade_points(grade))

        gpa = calculate_gpa(credits, grades)

        cumulative_credits.extend(credits)
        cumulative_grade_points.extend([gpa] * num_courses)

        print(f"\nGPA for Semester {semester + 1}: {gpa:.2f}")

    cgpa = calculate_cgpa(cumulative_credits, cumulative_grade_points)
    print(f"\nOverall CGPA: {cgpa:.2f}")

if __name__ == "__main__":
    main()
