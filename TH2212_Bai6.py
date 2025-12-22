n = int(input("Nhap so luong bai hat:"))
ds = []
for i in range(n):
    bai_hat = input("Nhap bai hat yeu thich cua ban:")
    ds.append(bai_hat)
print(f"{n} bai hat yeu thich cua ban la:{ds}")