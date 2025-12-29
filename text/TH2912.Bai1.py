n = int(input("Nhap diem mon toan:"))
m = int(input("Nhap diem mon ly:"))
p = int(input("Nhap diem mon hoa:"))
tong = n + m + p
print("Tong diem 3 mon la:", tong)
if tong >= 15:
    print("Ban da do")
else:
    print("Ban da truot")