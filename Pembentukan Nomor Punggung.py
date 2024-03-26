#!/usr/bin/env python
# coding: utf-8

# In[7]:


# input nomor punggung
nomor_punggung = int(input("Masukkan nomor punggung: "))

# hasil posisi
posisi = ""

# pengecekan
if nomor_punggung % 2 == 0:
    if nomor_punggung >= 50 and nomor_punggung <= 100:
        posisi = "Capten Team"
    else:
        posisi = "Target Attacker"
elif nomor_punggung % 2 != 0:
    if nomor_punggung % 3 == 0 or nomor_punggung % 5 == 0:
        posisi = "Keeper"
    elif nomor_punggung > 90:
        posisi = "Playmaker"
    else:
        posisi = "Defender"
else:
    posisi = "Posisi tidak diketahui"

# output
if posisi != "Posisi tidak diketahui":
    print(f"Pemain dengan nomor punggung {nomor_punggung} adalah seorang {posisi}")
else:
    print("Nomor punggung tidak valid atau tidak sesuai dengan aturan")

