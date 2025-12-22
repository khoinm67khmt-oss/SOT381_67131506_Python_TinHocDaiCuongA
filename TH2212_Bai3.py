ds =[]
for i in range(3):
    so = float(input("Nhap so:"))
    ds.append(so)
lon_nhat = max(ds)
nho_nhat = min(ds)
print(f"Danh sach vua nhap la:{ds}")
print(f"So lon nhat trong danh sach la:{lon_nhat}")
print(f"So lon nhat trong danh sach la:{nho_nhat}")

