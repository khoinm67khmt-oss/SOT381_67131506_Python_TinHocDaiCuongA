n = int(input("Nhap so luong phan tu n:"))
L = 0
Z = 0
for i in range(1,n+1):
    L += i
for i in range(2,n + 1,2):
    Z += i
if Z == 0:
    print("Khong the tinh")
else:
    S = L / Z
    print(f"Tong S = {S}")
   