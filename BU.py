a = 0
def ad():
    global a
    a += 1
def m():
    global a
    a -= 1
def q():
    print(a)
def num():
    global a
    a=int(input("number:"))
while True:
    i = input(">>")
    if "+" in i:
        ad()
    if "-" in i:
        m()
    if "'" in i:
        q()
    if "№" in i:
        num()
    if a >= 128:
        a = 0
