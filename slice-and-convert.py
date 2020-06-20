"""
@author : hackedubuntu (on twitter)
This little script serves to change special character of HTML.
Especially, <, >, ?, & characters will change to &lt; , &gt; ,
&quot; , &amp; .
"""

file = input("Enter filename: ")

try:
	with open(file, "r+", encoding="utf8") as f:
		file2 = "a" + file
		with open(file2, "w", encoding="utf8") as fd:
			for x in f.readlines():
				x = x.strip("\n")
				x = [*x]
				for i in range(len(x) -1):
					if x[i] == "<":
						x[i] = "&lt;"
					elif x[i] == ">":
						x[i] = "&gt;"
					elif x[i] == "?":
						x[i] = "&quot;"
					elif x[i] == "&":
						x[i] = "&amp;"
				x.append("\n")
				x = "".join(t for t in x)
				fd.write(x)
			print("File had changed!!")
		print("Mission Completed!!")
except Exception as e:
	print(e)
