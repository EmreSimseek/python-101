# Write

file = open("example.txt","w")   #dosya yolu , mod
file.write("Hello, Word")
file.close

file = open("example.txt", "a")
file.write("\nThis line is include new text.")
# Open

file = open("example.txt","r")
content = file.read()

print(content)

file.close()

#line by line
file = open("example.txt", "r")

# Dosyanın tüm satırlarını bir liste olarak döndürür.
lines = file.readlines()

for line in lines:
    print(line.strip())  # Satır sonundaki boşlukları (yeni satır karakteri) kaldırırız.

file.close()
#use with block
with open("example.txt", "r") as file:
    content = file.read()
    print(content)