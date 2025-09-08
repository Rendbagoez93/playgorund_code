# Student and course data
students = {
    101: "Zelda",
    102: "Link",
    103: "Mario",
    104: "Nero",
    105: "Vergil"
}

courses = {
    "Math": 2,
    "Physics": 2,
    "Chemistry": 1
}

# Enrollment tracking
enrollments = set()
course_roster = {course: set() for course in courses}

# Enroll a student
def enroll(student_id, course_name):
    if student_id not in students:
        print(f"❌ Student ID {student_id} not found.")
        return
    if course_name not in courses:
        print(f"❌ Course '{course_name}' does not exist.")
        return

    entry = (student_id, course_name)

    if entry in enrollments:
        print(f"⚠️ {students[student_id]} is already enrolled in {course_name}.")
    elif len(course_roster[course_name]) >= courses[course_name]:
        print(f"🚫 Course '{course_name}' is full.")
    else:
        enrollments.add(entry)
        course_roster[course_name].add(student_id)
        print(f"✅ {students[student_id]} enrolled in {course_name}.")

# Show all enrollments
def show_enrollments():
    print("\n📋 Enrollments by Course:")
    for course, student_ids in course_roster.items():
        print(f"\n{course} ({len(student_ids)}/{courses[course]}):")
        for sid in student_ids:
            print(f" - {students[sid]} (ID: {sid})")

# Sample usage
enroll(101, "Math")
enroll(102, "Math")
enroll(103, "Math")      # Should be full
enroll(104, "Physics")
enroll(101, "Physics")
enroll(101, "Physics")   # Duplicate
enroll(105, "Chemistry") # Invalid student

show_enrollments()