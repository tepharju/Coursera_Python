grade1 = 100.0
grade2 = 90.0

total = 0
grade_count = 0

if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
else:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)
