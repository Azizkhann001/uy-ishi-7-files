with open("input4.txt",encoding="utf-8") as f:
    sonlar=f.read().split()

yegindi=sum(map(int,sonlar))
ortacha=yegindi/len(sonlar)

print(round(ortacha))