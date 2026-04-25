def exercise_1_basics():

    course = "CMP 269"
    students = 30

    print(f"The course {course} has {students} students.")


def exercise_2_collections():

    colors = ["red", "blue", "green", "yellow", "purple"]

    # Add a 6th color
    colors.append("orange")

    student = {
        "name": "Abdule",
        "gpa": 3.8
    }

    print("Colors:", colors)
    print("Student Info:", student)


def exercise_3_logic():

    numbers = [1, 2, 3, 4, 5, 6]
    evens = []

    for num in numbers:
        if num % 2 == 0:
            evens.append(num)

    print("Even numbers:", evens)


if __name__ == "__main__":
    print("--- Exercise 1 ---")
    exercise_1_basics()
    print("\n--- Exercise 2 ---")
    exercise_2_collections()
    print("\n--- Exercise 3 ---")
    exercise_3_logic()