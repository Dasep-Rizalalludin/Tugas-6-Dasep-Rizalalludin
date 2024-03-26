#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Menentukan ganjil genap
nilai = int(input('Isikan Nilai :'))
sisa_bagi = nilai % 2
if sisa_bagi==0:
    print(f'{nilai} adalah bilangan genap')
else:
    print(f'{nilai} adalah bilangan ganjil')
print('program selesai')


# In[25]:


#0 - 49 => E
#50 - 59 => D
#60 - 69 => C
#70 - 84 => B
#85 - 100 => A
nilai_program = int(input('Isikan Nilai Pemrograman'))
if nilai_program < 0 or nilai_program > 100:
    print("Nilai anda salah")
else:
    if nilai_program < 50:
        print("E")
    elif nilai_program <60:
        print("D")
    elif nilai_program <70:
        print ("C")
    elif nilai_program <80:
        print("B")
    elif nilai_program <=100:
        print("A")
    else:
        print("Input anda salah")


# In[29]:


username = input ('Isikan username')
password = input ('Isika Password')

#jika username salah => Username anda salah
#jika password salah => password anda salah
#jika keduanya salah => Username dan Password anda salah
#jika keduanya benar => Selamat datang (username)
#username: admin
#passsword: admin

if username == 'admin':
    if password == 'admin':
        print (f'selamat datang {username}')
    else:
        print(f'password anda salah')

else:
    if password == 'admin':
        print("Username anda salah")
    else:
        print("Username dan password anda salah")
    


# In[61]:


nama = input("Masukan nama :")
umur = int(input ("Masukan umur :"))
alamat = input("Masukan alamat :")
tabungan = int(input ("Masukan tabungan :"))

pangkat = ''
if umur > 40 :
        if alamat == 'new york' or alamat =='nevada' or alamat=='hevana':
            if tabungan > 100:
                pangkat = 'Don'
if umur >25 and umur <= 40:
        if alamat == 'new jersey' or alamat =='manhatan' or alamat=='hevana':
            if tabungan > 0 and tabungan <=2 :
                pangkat = 'Underboss'
if umur > 18 and umur <= 24 :
        if alamat == 'callifornia' or alamat =='detroit' or alamat=='hevana':
            if tabungan > 10:
                pangkat = 'capo'
                
if pangkat !='':
    print (f'{nama} kemungkinan seorang anggota mafia dengan pangkat {pangkat}')
else:
    print(f'{nama} tidak mencurigakan')
    


# In[ ]:




