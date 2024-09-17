students = [
    {
        "name": "Ahmet",
        "number": 101,
        "lessons": {"Matematik": 90, "Fizik": 85}
    },
    
]


def add_student(name,number):
    student={
        "name":name,
        "number":number,
        "lessons":{}
    }
    students.append(student)

add_student("Mehmet",103)
print(students)

def add_lesson_to_student(number,lesson_name,grade):
     for student in students:
         if student["number"] == number:
              student["lessons"] [lesson_name] = grade
              break

add_lesson_to_student(103, "Matematik", 95)
add_lesson_to_student(103, "Fizik", 88)          

print(students)


def calculate_average(number):
    for student in students:
        if student["number"] == number:
            lessons = student["lessons"]          
            if lessons:
             total=sum(lessons.values())
             average = total / len(lessons)
             return average  
            else:
                return 0 

average = calculate_average(103)
print(f"Mehmet'in not ortalaması: {average}")    

def lessons_average(lesson_name):
    total = 0  
    count = 0
    for student in students:
        if  lesson_name in student["lessons"]:
             total += student["lessons"][lesson_name]
             count += 1
    
    if count > 0:
        average = total / count
        return average
    else:
        return None  # Eğer kimse bu dersi almıyorsa, None döndür
    
averages = lessons_average("Matematik")
print(f"Matematik dersinin not ortalaması: {averages}")       

   
              