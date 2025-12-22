a,b,c = eval(input("Nhap 3 so a,b,c: "))
max_h = a
if b > max_h:
    max_h = b
if c > max_h:
    max_h = c
print(f"So lon nhat trong 3 so a,b,c la:{max_h}")
min_h = a
if b < min_h:
    max_h = b
if c < min_h:
    max_h = c
print(f"So nho nhat trong 3 so a,b,c la:{min_h}")
