import os

liste = []
j = 0
bulundu = False

adres = input("Dosyanın konumu: ")#Kullanıcıdan dosyanın oluşturulacağı dizin isteniyor
dosya = input("Dosyanın adı:    ")#Dosya adı isteniyor.

if len(adres) < 1:
    adres = os.getcwd()#Dizin adı girilmemişse halihazırda OS_ustunde_oy... adlı python dosyamızın bulunduğu dizinin adını alır
else:    
    os.chdir(adres)#Dizin adı girilmişse terminalde cd DİZİN_ADI yazıp enterlamanın karşılığı olan işlem

dosyalar = os.listdir(adres)#Dizindeki dosyaların ve klasörlerin listesini alır.

if dosya in dosyalar:
    bulundu = True # Dosyamız bu dizinde varsa bulundu'nun değeri True olur, yoksa False kalır

if bulundu: #Bulundu True ise dosyanın içeriğini değiştirmeye başlarız.
    with open(dosya,"r+") as dosya2:
        for i in dosya2.readlines():
            liste.append(i)
        if len(liste) > 0:
            j = 1 + int(liste[len(liste) - 1])
        print(j,file=dosya2,flush=False)
        liste.append(j)
else: #Bulundu False ise girdiğimiz dosya adındaki bir dosyayı oluşturur. Uzantının bir önemi yok. Sonuçta metin belgesi oluşturur
    with open(dosya,"w") as dosya2:
        print(os.getcwd())
        print("Dosya Bulma hatası")
print(*liste) #En sonda da dosyanın içeriğini ekrana bastırır.
