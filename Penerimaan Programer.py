#!/usr/bin/env python
# coding: utf-8

# In[18]:


#input nilai
nilai_coding = int(input("Masukan nilai coding :"))
nilai_interview = input("Masukan nilai interview (A/B) :")

#hasil nilai_coding
if nilai_coding > 80:
    hasil_coding = "LOLOS"
elif nilai_coding >= 60 or nilai_coding <= 80:
    hasil_coding = "DIPERTIMBANGKAN"
else:
    hasil_coding = "GAGAL"
    
#hasil nilai interview
if nilai_interview == 'A' or nilai_interview == 'B':
    hasil_interview = "LOLOS"
else:
    hasil_interview = "GAGAL"
    
#output
if hasil_coding == "LOLOS" or hasil_coding == "DIPERTIMBANGKAN" and hasil_interview == "LOLOS":
    print("Selamat Kamu Berhasil Menjadi Calon Programmer")
else:
    print("Maaf Kamu Belum Berhasil Menjadi Calon Programmer")

