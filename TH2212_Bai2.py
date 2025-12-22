import math
while True:
    a = int(input("Nhap canh a cua tam giac:"))
    b = int(input("Nhap canh b cua tam giac:"))
    c = int(input("Nhap canh c cua tam giac:"))
    if (a + b > c) and (a + c > b) and (c + b > a) :
        chu_vi = a + b +c
        p = chu_vi / 2
        dien_tich = math.sqrt(p * (p -a) * (p - b) * (p - c))
        break
    else:
        print("Nhap lai")
print(f"Dien tich tam giac la:{dien_tich}")
print(f"Chu vi tam giac la:{chu_vi}")