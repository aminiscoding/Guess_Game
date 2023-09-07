import random
h = random.randrange(1, 100)
print(f"my guess is: {h}; write r for right, l for lower, h for higher")
ghabl_k = [101]
ghabl_b = [0]

n = input()

while n != "r":
    if n == "l":
        ghabl_k.append(h)
        h = random.randrange(max(ghabl_b), min(ghabl_k))
        print (h)
        n = input()
    if n == "h":
        ghabl_b.append(h)
        h = random.randrange(max(ghabl_b), min(ghabl_k))
        print (h)
        n = input()
if n == "r":
    print("hahaha I did it!!!")