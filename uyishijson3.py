with open("input3.txt",encoding="utf-8") as f1 :
    matn=f1.read()

sozlar=matn.split(" ")
yangi=""

for soz in sozlar:
    yangi+=soz.capitalize()+" "

with open("output3.txt","w",encoding="utf-8") as f2 :
    f2.write(yangi.strip())

