with open("input1.txt") as f1:
    sonlar=f1.read().split()

with open("output1.txt","w") as f2:
    for i in sonlar:
        f2.write(chr(int(i)))
 