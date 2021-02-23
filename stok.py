import pandas as pd

banner = """
******************************************

ISUZU PARÇA SORGULAMA EKRANINA HOŞGELDİNİZ

******************************************

1) Kod  ile ürün ara
2) İsim ile ürün ara

"""

hoscakalbanner = """
*******************************************

PROGRAMIMIZI KULLANDIĞINIZ İÇİN TEŞEKKÜRLER

*******************************************
"""

def kesisim(l1):
    return list(set(l1))

def kesisim2(l1,l2):
    return list(set(l1)&set(l2))

def kesisim3(l1,l2,l3):
    return list(set(l1)&set(l2)&set(l3))

def kesisim4(l1,l2,l3,l4):
    return list(set(l1)&set(l2)&set(l3)&set(l4))

ques = "Seçiminiz:"
quesans = 0
queskod = "Lütfen Ürün Kodunu Giriniz:"
queskodans = ""
quesisim = "Lütfen Ürün İsmi Giriniz:"
quesisimans = ""
quitask = "Çıkmak İstiyor Musunuz?(y/n):"
quitans = "n"

df = pd.read_csv("isuzu.csv",sep=",")

while 1:
	print(banner,end="")
	quesans = int(input(ques))

	if quesans == 1:
		queskodans = input(queskod)
		print(df[df["Ürün Kodu"].str.contains(queskodans)])
	elif quesans == 2:
		quesisimans = input(quesisim)
		quesisimans = quesisimans.split(",")
		kes = []
		if len(quesisimans) == 1:
			l1 = df[df["Ürün Adı"].str.contains(quesisimans[0])]
			kes = kesisim(l1["Ürün Kodu"])
			print(kes)
		elif len(quesisimans) == 2:
			l1 = df[df["Ürün Adı"].str.contains(quesisimans[0])]
			l2 = df[df["Ürün Adı"].str.contains(quesisimans[1])]
			print(kesisim2(l1["Ürün Kodu"],l2["Ürün Kodu"]))
			kes = kesisim2(l1["Ürün Kodu"],l2["Ürün Kodu"])
		elif len(quesisimans) == 3:
			l1 = df[df["Ürün Adı"].str.contains(quesisimans[0])]
			l2 = df[df["Ürün Adı"].str.contains(quesisimans[1])]
			l3 = df[df["Ürün Adı"].str.contains(quesisimans[2])]
			print(kesisim3(l1["Ürün Kodu"],l2["Ürün Kodu"],l3["Ürün Kodu"]))
			kes = kesisim3(l1["Ürün Kodu"],l2["Ürün Kodu"],l3["Ürün Kodu"])
		elif len(quesisimans) == 4:
			l1 = df[df["Ürün Adı"].str.contains(quesisimans[0])]
			l2 = df[df["Ürün Adı"].str.contains(quesisimans[1])]
			l3 = df[df["Ürün Adı"].str.contains(quesisimans[2])]
			l4 = df[df["Ürün Adı"].str.contains(quesisimans[3])]
			print(kesisim4(l1["Ürün Kodu"],l2["Ürün Kodu"],l3["Ürün Kodu"],l4["Ürün Kodu"]))
			kes = kesisim4(l1["Ürün Kodu"],l2["Ürün Kodu"],l3["Ürün Kodu"],l4["Ürün Kodu"])

		with open(".".join(x for x in quesisimans)+".txt","w",encoding="utf-8") as dosya:
			for x in kes:
				t = df[df["Ürün Kodu"].str.contains(x)]
				t = t.values.tolist()
				t = " ".join(str(x) for x in t)
				dosya.write(t+"\n")
	else:
		continue
	while 1:
		quitans = input(quitask)
		if type(quitans) == str:
			if quitans.lower() == "y" or quitans.lower() == "n":
				if quitans.lower() == "y":
					print(hoscakalbanner)
					exit()
				elif quitans.lower() == "n":
					break
		else:
			continue