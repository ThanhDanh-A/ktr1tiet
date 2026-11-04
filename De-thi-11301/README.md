# De thi Lap trinh Python - Ma de 11301

Bo loi giai cho PDF mon Lap trinh Python (229152), ma de 11301. De gom 5 cau, moi cau 2 diem.

## Tu cham bang dau tich va dau X trong VS Code

1. Cai Python 3.9 tro len va extension Python cua Microsoft trong VS Code.
2. Mo VS Code > File > Open Folder > chon thu muc De-thi-11301 (thu muc co autograde_11301.py).
3. Nhan Ctrl + Shift + P > Python: Select Interpreter > chon ban Python da cai.
4. Nhan Ctrl + Shift + B.
5. Xem ket qua trong Terminal: moi tieu chi co ✅ neu dat, ❌ neu chua dat, diem du kien va ghi chu cach sua.

Lenh Terminal tuong duong: python autograde_11301.py

Bo tu cham tu tim thu muc co du Cau1.py den Cau5.py. Em co the doi ten HOTEN_MSSV thanh ho ten va MSSV truoc khi cham; khong can sua duong dan.

## Chay rieng tung cau

Trong VS Code nhan Ctrl + Shift + P > Tasks: Run Task > chon Chay Cau 1 den Chay Cau 5. Cac task nay cung tu tim thu muc bai lam sau khi em doi ten.

Hoac mo file trong thu muc bai lam va chon Run Python File.

## Kiem tra bo cham

Chay cac bai test tu dong cua bo cham:

python -m unittest -v test_autograde_11301.py

## Cau truc nop bai theo yeu cau PDF

De yeu cau thu muc HOTEN_MSSV chua dung 5 file .py:

HOTEN_MSSV/
  Cau1.py
  Cau2.py
  Cau3.py
  Cau4.py
  Cau5.py

Doi ten HOTEN_MSSV thanh ho ten va MSSV that cua em truoc khi nop.

## Bo cham danh gia dieu gi?

Cau 1a - kiem tra n trong [1;1500]: 0.50
Cau 1b - ham dem chu so le: 0.75
Cau 1c - ham tinh S: 0.75
Cau 2a - dem chu hoa: 0.75
Cau 2b - kiem tra chuoi doi xung: 0.50
Cau 2c - tinh tong chu so: 0.75
Cau 3a - nhap list den khi gap 0: 0.75
Cau 3b - tong so duong chan: 0.75
Cau 3c - dem so lan xuat hien cua k: 0.50
Cau 4a - nhap va luu thong tin sach: 1.50
Cau 4b - xoa sach theo ma: 0.50
Cau 5a - lop DienThoai va thuoc tinh/phuong thuc: 1.00
Cau 5b - tao hai doi tuong va hien thi thong tin: 1.00

Tong: 10.00 diem.

Luu y: Day la bo tu kiem tra tham khao duoc viet theo de va dap an/rubric trong PDF, khong phai chuong trinh cham chinh thuc cua giang vien. Bo cham dung mot so bo du lieu thu, co the khong bao phu moi truong hop ma giang vien su dung. Khong can cai thu vien ben ngoai bang pip.
