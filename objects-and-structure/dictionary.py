# Boş sözlük oluşturma
bos_sozluk = {}

# Anahtar-değer çifti ile sözlük oluşturma  key-value
kullanici = {
    "isim": "Ahmet",  
    "yas": 30,
    "meslek": "Mühendis"
}

print(kullanici)
# Kullanıcı bilgilerini içeren sözlük
student_list = {
    "student1":
    {
        "isim": "Ahmet",
        "yas": 30,
        "meslek": "Mühendis",
        "sehir": "İstanbul"
    },
    
    "student2":
    {
        "isim": "Ayşe",
        "yas": 25,
        "meslek": "Doktor",
        "sehir": "Ankara"
    }
}
print
for student in student_list:
    print(student, student_list[student]["isim"],end=", ")
# Tüm bilgilere erişme
student1_info = student_list["student1"]
print(student1_info)

# tek bir özelliğe erişme
student2_age = student_list["student2"]["yas"]
print(student2_age)

student2_age = student_list["student2"]["yas"] = 26



def add_student(isim,yas,meslek,sehir):
    new_student_key = f"student{len(student_list) + 1}"     #bulunan öğrenci sayısına bir ekleyerek yeni öğrenci adını oluşturur
    new_student = {
        "isim": isim,
        "yas": yas,
        "meslek": meslek,
        "sehir": sehir
    }
    
    student_list[new_student_key] = new_student
    print(f"{new_student_key} başarıyla eklendi!")


add_student("Mehmet", 22, "Öğrenci", "İzmir")


for student, student_list in student_list.items():
    print(f"{student}: {student_list}")
    
   
    degisken = 4
degisken*degisken