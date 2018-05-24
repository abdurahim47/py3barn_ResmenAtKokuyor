import os

def yol_degis(yol):
    return r"".join(yol)

def change_path(path):
    return r"".join(path)

menu = """
1. For English
2. Türkçe için
"""
secim = ""
choice = ""

while True:
    try:
        dil = int(input(menu))
    except ValueError as e:
        print("Yanlış Değer")
        print(e)
    if dil == 1:
        choice = "en"
        break
    elif dil == 2:
        secim = "tr"
        break
    else:
        continue
if secim == "tr":
    yol = input("İçindekileri değiştirmek istediğiniz klasörün tam adresini girin: ")
    silinecek = input("Silmek istediğiniz ek: ")
    eklenecek = input("Silinenin yerine gelecek olan yazı: ")
    yol2 = yol_degis(yol)
    if len(yol2) > 0:
        os.chdir(yol2)
    else:
        yol2 = os.getcwd()
    dosyalar = os.listdir(path=yol2)
    print("Çalışılan klasör: ",os.getcwd())
    yeni_adlar = dosyalar.copy()

    for i in range(len(yeni_adlar)):
        yeni_adlar[i] = yeni_adlar[i].replace(silinecek,eklenecek)

    for i in range(len(dosyalar)):
        os.replace(dosyalar[i],yeni_adlar[i])

    print("işlem başarılı...")

elif choice == "en":
    path = input("Full path for directory to change inside it: ")
    will_delete = input(r"What you want to delete from folder's or file's name: ")
    will_replace = input("Will replace text: ")
    path2 = change_path(path)
    if len(path2) > 0:
        os.chdir(path2)
    else:
        path2 = os.getcwd()
    files_folders = os.listdir(path=path2)
    print("Current Working Directory: ",os.getcwd())
    new_names = files_folders.copy()

    for i in range(len(new_names)):
        new_names[i] = new_names[i].replace(will_delete, will_replace)

    for i in range(len(files_folders)):
        os.replace(files_folders[i],new_names[i])

    print("Done...")
