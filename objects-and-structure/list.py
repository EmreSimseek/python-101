
grade = [80,70,60,90]
my_list = [80,"ahmet",3.25,False,None,grade]

#print(type(my_list))

#print(len(my_list))

#del my_list


#print(my_list[2:])    
#print(my_list[1:3])
#print(my_list[5][0])  

grade.append(40)
grade.insert(1,60)

for i in grade:
    print(i,end=" ") 
my_list.extend(grade)
print(my_list ,end=" ")      

grade.remove(60)

index_two = grade.pop(2)
index_zero= grade.pop 
     