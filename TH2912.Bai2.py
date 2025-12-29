import math
def tong(x,n):
  ket_qua = 0
  for i in range(n):
    ket_qua = math.sqrt(x + ket_qua)
  return ket_qua
n = int(input("Nhap n:"))
x = float(input("Nhap x:"))
while n < 0 and x < 0:
    n = int(input("Nhap lai n:"))
    x = float(input("Nhap lai x:"))
print(tong(x,n))