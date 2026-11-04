# Cau 2a: Tinh tong cac so chan trong doan [x, y]

x = int(input("Nhap x: "))
y = int(input("Nhap y: "))

tong = 0
for so in range(x, y + 1):
    if so % 2 == 0:
        tong += so

print(tong)
