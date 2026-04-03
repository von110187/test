students = []
subjects = []
names = []

for _ in range(5):
    while True:
        try:
            name    = input("\nName: ")
            subject = input("Subject: ")
            grade   = int(input("Grade: "))
        except ValueError:
            print("Please enter a valid grade")
        else:
            break

    students.append((name, subject, grade))

print("\nAll Students:")
for i in students:
    print(f"Name: {i[0]}, Subject: {i[1]}, Grade: {i[2]}")
    subjects.append(i[1])
    names.append(i[0])

print("\nUnique Subjects:")
for i in set(subjects):
    print(i)

print("\nUnique Students:")
for i in set(names):
    print(i)