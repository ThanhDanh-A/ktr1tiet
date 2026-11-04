# CAU 1 (2.0 diem): Nhap so nguyen duong n trong doan [1; 1500].
# Dem so chu so le cua n va tinh S = 1/2 + 1/4 + ... + 1/(2n).


def DemChuSoLe(n):
    dem = 0
    while n != 0:
        tam = n % 10
        if tam % 2 != 0:
            dem += 1
        n //= 10
    return dem


def S(n):
    tong = 0
    for i in range(1, n + 1):
        tong += 1 / (2 * i)
    return tong


n = int(input("Nhập giá trị 1<=n<=1500: "))
while n < 1 or n > 1500:
    n = int(input("Nhập lại giá trị 1<=n<=1500: "))

print("Số lượng chữ số lẻ là: ", DemChuSoLe(n))
print("S = ", S(n))
