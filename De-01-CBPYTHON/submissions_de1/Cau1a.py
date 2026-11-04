# Cau 1a: Kiem tra so chan hay so le

x = float(input("Nhap x: "))

# So chan/le chi ap dung cho so nguyen.
if x.is_integer() and int(x) % 2 == 0:
    print("Chan")
else:
    print("Le")
