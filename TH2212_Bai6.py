n = int(input("Nhap so luong bai hat:"))
ds = []
for i in range(n):
    bai_hat = input(f"Nhap bai hat yeu thich thu {i} cua ban:")
    ds.append(bai_hat)
#-------------------------------------------------------------
for i in range(n):
    ten = ds[i]
    TEN = ten.upper()
    print(f"Bai {i}:{TEN}")
ds_in_hoa = [bai_hat.upper() for bai_hat in ds]
print(f"{n} bai hat yeu thich cua ban la:", ds_in_hoa)
#-------------------------------------------------------------
print("Cac bai co tu yeu la:")
for i in range(n):
    ten = ds[i].upper()
    if ten.find("YEU")!=-1:
        print(f"Bai {i}:{ten}")
#-------------------------------------------------------------
print("Cac ten bai dai nhat la:")
tenbaidainhat = ds[0]
sotucuabaidainhat = len(tenbaidainhat.split())
vitribai = 0
for i in range(n):
    tenbai = ds[i]
    so_tu = len(tenbai.split())
    if so_tu > sotucuabaidainhat:
        vitribai = i
        tenbaidainhat = tenbai
        sotucuabaidainhat = so_tu
print(f"Bai: {tenbaidainhat} o vi tri {vitribai} co {sotucuabaidainhat} tu")
