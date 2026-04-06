student_records = {
    "students": {
        "student_001": {
            "name": "John",
            "age": 19,
            "major": "Computer Science",
            "grades": [85, 92, 78]
        },
        "student_002": {
            "name": "Sarah",
            "age": 20,
            "major": "Biology",
            "grades": [90, 88, 95]
        },
    }
}

student_records["students"]["student_003"] = {
    "name": "Mike",
    "age": 18,
    "major": "Math",
    "grades": [82, 79, 91]
}

student_records["students"]["student_001"]["age"] = 20

for student_id, student in student_records["students"].items():
    print(f"Student ID: {student_id}, Name: {student['name']}, "
          f"Age: {student['age']}, Major: {student['major']}, ",
          f"Grades: {student['grades']}")