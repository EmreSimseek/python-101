# Küme tanımlama
my_set = {1, 2, 3, 4}
my_set2 = {10, 20, 30, 40,1}
'''
Kümeler içindeki her eleman benzersizdir.
Kümeye eleman ekleyip çıkarabilirsiniz.
Kümeler sıralı değildir, yani elemanlar eklediğiniz sırada saklanmaz.
Kümeler hızlı arama işlemleri için karma (hash) yapısını kullanır.
'''

# Kümeye eleman ekleme
my_set.add(5)
my_set.remove(3)
my_set.discard(0)  # 0 kümede yoksa hata vermez
my_set.union(my_set2)
new_set = my_set.intersection(my_set2)
print("my_set:",my_set)
print("new_Set:",new_set)

# Kümeler arası fark bulma
other_set = {3, 4, 5, 6}
diff_set = my_set.difference(other_set)
print(diff_set)  # Çıktı: {1, 2}



# tuple
# sıralı ve değiştirilemez bir veri yapısıdır. 
# bir kez tanımlandıktan sonra içeriği değiştirilemez.

# Tuple tanımlama
my_tuple = (1, 2, 3, 4,1,5)

# Tuple içindeki bir elemanı sayma
print(my_tuple.count(1))  

# Tuple içindeki elemanın indeksini bulma
print(my_tuple.index(5))  
