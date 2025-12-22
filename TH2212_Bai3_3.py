def so(a,b,c):
    M = a
    if b > M:
        M = b
    if c > M:
        M = c
    return M
a,b,c = eval(input("Nhap 3 so a,b,c:"))
numM = so(a,b,c)
print(f"So lon nhat la:{numM}")
def so_min(a,b,c):
    Mi = a
    if b < Mi:
        Mi = b
    if c < Mi:
        Mi = c
    return Mi
numMin = so_min(a,b,c)
print(f"So nho nhat la:{numMin}")