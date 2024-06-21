from random import randint
#humpyang game

options = {0: "kulob", 1: "hayang"}
p1 = input("pick 0 kung kulob 1 kung hayang (kulob, hayang): ")
p1 = options[int(p1)]
c1 = options[randint(0, 1)]
c2 = options[randint(0, 1)]

print(f"P1: {p1}")
print(f"c1: {c1}")
print(f"c2: {c2}")


if p1 != c1 and p1 != c2:
    print("p1 ang daog!")
elif c1 != p1 and c1 != c2:
    print("c1 ang daog!")
elif c2 != p1 and c2 != c1: 
    print("c2 ang daog!")
else:
    print("parehas tanan! utro!")
