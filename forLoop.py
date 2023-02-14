# -*- coding: utf-8 -*-

sehirler = ["Ankara","İstanbul","İzmir"] 

# print(sehirler[0])
# print(sehirler[1])
# print(sehirler[2])

for sehir in sehirler:
    if sehir != "Ankara": 
       print(sehir + " için kod : " + sehir[0:3])
    print("******")
#sehir bir takma isimdir.Döngüyü oluşturup printlemek için.
# != farklıysa anlamına gelir.
#continue o duruma denk gelen şeyi yazdırma demek.Döngünün o anki loopunu iptal ediyor.
#break şart ne ise ona denk geldiğinde döngüyü durdurmak

#%% For range

for x in range(100):
    print(x+1)
    
for x in range(1,10,2):
    print(x)
    
#2 sayısı sayıların aralarındaki değer aralığı kaçar kaçar gittiğini gösteriyor.