n = int(input("Nhap so phan tu n:"))
x = 0
y = 1
S = 0
tong = 0
for i in range(n):
    print(S,end =" ")
    tong += S
    x = y
    y = S
    S = x + y
    # print(S,end =" ")
print(f"\nTong cua {n} so Fibonaci la:{tong} ")
