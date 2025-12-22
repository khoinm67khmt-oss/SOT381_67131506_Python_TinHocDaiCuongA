while True:
    w = float(input("Nhap canh w:"))
    h = float(input("Nhap canh h:"))
    if (w >= 0.0 and w < 100.0) and (h >= 100.0):
        chu_vi = (w + h) * 2
        dien_tich = w * h
        break
    else:
        print("Nhap lai")
print(f"Dien tich HCN la:{dien_tich:.2f}") 
print(f"Chu vi HCN la:{chu_vi:.2f}")




