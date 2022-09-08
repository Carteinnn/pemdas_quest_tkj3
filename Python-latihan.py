# Program Dinamis

print("\n1. Luas Segitiga")
alas = int(input("masukan nilai alas: "))
tinggi = int(input("masukan nilai tinggi: "))    
luas_s =  alas * tinggi / 2
print("Nilai Luas segitiga adalah", luas_s)    

print("\n2.Luas persegi")
sisi = int(input("masukan nilai sisi: "))
luas_P = sisi * sisi
print("luas persegi adalah", luas_P)

print("\n3. Luas Jajargenjang")
alas = int(input("masukan nilai alas: "))
tinggi = int(input("masukan nilai tinggi: "))    
luas_j =  alas * tinggi
print("Nilai Luas jajargenjang adalah", luas_j)

print("\n4. Luas Lingkaran")
phi = 22/7
r1 = int(input("masukan nilai r1: "))
r2 = int(input("masukan nilai r2: "))
luas_l =  phi * r1 * r2 
print("Nilai Luas lingkaran adalah", luas_l)

print("\n5. Luas Persegi Panjang")
p = int(input("masukan nilai panjang: "))
l = int(input("masukan nilai luas: "))
luas_p = p * l
print("Nilai Luas Persegi panjang adalah", luas_p)

print("\n6. Luas Trapesium")
a = int(input("masukan nilai a: "))
b = int(input("masukan nilai b: "))
t = int(input("masukan nilai tinggi: "))
luas_t = 1/2 * (a + b) * t
print("Nilai Luas Trapesium adalah", luas_t) 


