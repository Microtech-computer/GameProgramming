# ==========================================
# STUDENT MANAGEMENT SYSTEM
# Author: Emmanuel Ajoo
# ==========================================

students = [
    {"id": 101, "name": "Alice John", "score": 85},
    {"id": 102, "name": "Emmanuel Ajoo", "score": 92},
    {"id": 103, "name": "James Gudu", "score": 48},
    {"id": 104, "name": "Bob Smith", "score": 76},
    {"id": 105, "name": "Charlie Brown", "score": 39},
]


def get_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"


print("=" * 75)
print("{:^75}".format("STUDENT REPORT"))
print("=" * 75)

print(f"{'S/N':<5}{'ID':<8}{'NAME':<25}{'SCORE':<10}{'GRADE':<10}{'STATUS'}")
print("-" * 75)

total_score = 0
passed = 0
failed = 0

for sn, student in enumerate(students, start=1):

    score = student["score"]
    grade = get_grade(score)

    if score >= 50:
        status = "PASS"
        passed += 1
    else:
        status = "FAIL"
        failed += 1

    total_score += score

    print(
        f"{sn:<5}"
        f"{student['id']:<8}"
        f"{student['name'].upper():<25}"
        f"{score:<10}"
        f"{grade:<10}"
        f"{status}"
    )

average = total_score / len(students)

print("-" * 75)
print(f"Total Students : {len(students)}")
print(f"Passed         : {passed}")
print(f"Failed         : {failed}")
print(f"Average Score  : {average:.2f}")
print("=" * 75)