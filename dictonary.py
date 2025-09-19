student_grades = {}
off = False
while not off:
    name = input('Enter student name: ')
    grade = input('Enter student grade: ')
    student_grades[name] = grade
    print('Student added successfully!')
    print(student_grades)
    x = input('Do you want to add another student?(Y/N)').lower()
    if x == 'y':
        pass
    else:
        off = True