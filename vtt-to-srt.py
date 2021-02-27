from os import listdir,getcwd


liste = listdir(getcwd())

liste = [x for x in liste if x.endswith(".vtt")]

cevrilecek = []

for x in liste:
	with open(x,"r",encoding="utf-8") as file:
		f = [a.strip() for a in file.readlines()]
		for t in range(len(f)):
			if f[t] == "WEBVTT" or f[t] == "":
				del f[t]
		for t in range(1,len(f),2):
			if liste[t].endswith(".") and liste[t] not in cevrilecek[-1]:
				cevrilecek.append((liste[t -1],liste[t]))
			else:
				cevrilecek.append((liste[t -1][:14] + liste[t+1][14:24],liste[t] + " " + liste[t + 2]))

	with open(x[:-3] + "srt","w",encoding="utf-8") as file:
		for x in range(len(cevrilecek)):
			file.wrie((x + 1) + "\n" + cevrilecek[x][0] + "\n" + cevrilecek[x][1])