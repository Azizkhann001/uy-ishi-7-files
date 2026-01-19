soz=input("soz kiriting:").lower()
with open("input2.txt",encoding="utf-8") as f:
    matn=f.read().lower()
    if matn.find(soz)!=-1:
        print("Siz kiritgan soz faylda bor")
    else:
        print("Siz kiritgan soz faylda yoq!")
