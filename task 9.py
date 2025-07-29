student_marks={'Rahul':88,'Anjali':57,'Shashank':68}
student_name=input("Enter your name: ")
if student_name in student_marks:
    result="{}'s mark is {}".format(student_name,student_marks[student_name])
    print(result)
else:
    print("Student doesn't exist")
