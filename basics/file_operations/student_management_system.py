student_list= []
index = 0

def add_student():
    name=str(input("Enter student name:"))
    age =int(input("Enter student age:"))
    grade=int(input("Enter student grade:"))
    student_list.append([name, age, grade])

def write_to_txt():
    global index
    
    with open("student.txt", "a") as file:  # with kullanımı dosya işlemlerini daha güvenli yapar
            file.write(f"{student_list[index][0]},{student_list[index][1]},{student_list[index][2]}\n")
    
    index+=1

def print_student_list():
    file = open("student.txt", "r")
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # Satır sonundaki boşlukları (yeni satır karakteri) kaldırırız.
    file.close()

def update_student_grade(name,grade):
    found = False
    updated_students=[]
    
    with open("student.txt","r") as file:
        lines = file.readlines()
    
    for line in lines: 
        student_data= line.strip().split(",")
        if student_data[0] == name:
            student_data[2] = str(grade)   
            found = True
        updated_students.append(student_data)
    
    
    with open("student.txt","w") as file:
        for student in updated_students:
            file.write(f"{student[0]},{student[1]},{student[2]}\n")
    if found:                   
        print(f"{name}'s grade has been updated to {grade}.")
    else:
        print(f"Student named {name} not found.")
 
def main():  
    
    
    while True:
        choice = int(input("1-Add Student\n2-Update Student Grade\n3-List of Student\n4-Delete Student\n0-For exit program\nEnter your choice:"))
        match choice:
            case 1:
                add_student() #Student added student_list
                write_to_txt()
            case 2:
                name = input("Enter student name:")
                grade =input(f"Enter new grade for {name}:")
                update_student_grade(name,grade)     
                   
            case 3:
                print("------------------\nStudent List:")
                print_student_list()
                print("------------------")
            case 4:
                return 0
            case 0:
                return False        
                        
    
       
       
           
if __name__ == "__main__":
    main()  