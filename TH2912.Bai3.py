n = int(input("Nhap diem n:"))
x = int(input("Nhap diem x:"))
tong = 0
for i in range(1, n + 1):
    tong += x**i/(i+1)
print("Tong la:", tong + 1)                                             