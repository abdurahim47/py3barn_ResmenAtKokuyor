import requests
import os
import urllib.request as request

file_path = input("URL of your document(such as: https://images.app.goo.gl/ck8KKUQCsFojC4bH8): ")
saved = input("Pathname for your new doc: ")
filename = input("What will your doc name be: ")

if len(saved) < 1:
    os.chdir(os.getcwd())
else:
    os.chdir(saved)

extensions = ["jpg","png","deb","pdf","zip","epub","exe"]

file1 = file_path.split("/")
ext = file1[-1].split(".")

if len(filename) <= 3 or (ext and ext not in extensions):
    filename = file1[-1]

print("Starting Download...")
filex = requests.get(file_path,stream=True)
if filex.status_code == 200:
    print("Size of File: ",filex.headers.get('content-length',0))
else:
    print("Couldn't Download..")

try:
    print("Downloading..")
    request.urlretrieve(file_path,filename)
    print("Downloaded!")
except:
    print("Didn't download")
