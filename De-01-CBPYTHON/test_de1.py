"""Du lieu kiem thu cho De so 01 - CBPYTHON.

Cac noi dung bai tap duoc doi chieu voi PDF De so 01 - CBPYTHON.
Cac input/expected duoi day duoc dua theo file test_de1.py trong goi tai lieu.
"""

tests = {
    # Cau 1a: Nhap so thuc x va kiem tra chan/le.
    "Cau1a": [
        {"input": "4\n", "expected": ["chan"]},
        {"input": "7\n", "expected": ["le"]},
        {"input": "0\n", "expected": ["chan"]},
        {"input": "-3\n", "expected": ["le"]},
    ],

    # Cau 1b: Nhap ten, tuoi va in loi chao theo mau.
    "Cau1b": [
        {"input": "An\n20\n", "expected": "Xin chào An, bạn 20 tuổi."},
        {"input": "Long\n18\n", "expected": "Xin chào Long, bạn 18 tuổi."},
        {"input": "Hà\n22\n", "expected": "Xin chào Hà, bạn 22 tuổi."},
    ],

    # Cau 2a: Tinh tong cac so chan trong doan [x, y].
    "Cau2a": [
        {"input": "2\n10\n", "expected": ["30"]},
        {"input": "5\n11\n", "expected": ["24"]},
        {"input": "3\n3\n", "expected": ["0"]},
        {"input": "4\n4\n", "expected": ["4"]},
        {"input": "-2\n2\n", "expected": ["0"]},
    ],

    # Cau 2b: Dem chu so trong chuoi tai cac vi tri x den y (tinh tu 1).
    "Cau2b": [
        {"input": "abc12345\n1\n8\n", "expected": ["5"]},
        {"input": "a1b2c3d4e5\n2\n9\n", "expected": ["4"]},
        {"input": "python3.9\n7\n9\n", "expected": ["2"]},
        {"input": "abcdef\n1\n6\n", "expected": ["0"]},
        {"input": "a2b\n2\n2\n", "expected": ["1"]},
    ],

    # Cau 3a: Tao list moi chi gom cac phan tu kieu str.
    "Cau3a": [
        {"input": "", "expected": ["['apple', 'banana']"]},
    ],

    # Cau 3b: Them orange, xoa 3.14, sau do dao nguoc list.
    "Cau3b": [
        {
            "input": "",
            "expected": [
                "[100, 'apple', 3.14, 'banana', 200, None, 'orange']",
                "[100, 'apple', 'banana', 200, None, 'orange']",
                "['orange', None, 200, 'banana', 'apple', 100]",
            ],
        },
    ],

    # Cau 4a: In phan tu dau, thu ba va cuoi cung cua tuple.
    "Cau4a": [
        {"input": "", "expected": ["apple", "cherry", "coc"]},
    ],

    # Cau 4b: Noi hai tuple va lap lai tuple t1 ba lan.
    "Cau4b": [
        {"input": "", "expected": ["(1, 2, 3, 4)", "(1, 2, 1, 2, 1, 2)"]},
    ],

    # Cau 5a: Dem tan suat xuat hien cua moi ky tu trong 'hello world'.
    "Cau5a": [
        {
            "input": "",
            "expected": ["{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}"],
        },
    ],

    # Cau 5b: Lay ten hoc sinh co diem >= 8.
    "Cau5b": [
        {"input": "", "expected": ["['An', 'Cuong', 'Hoa']"]},
    ],
}
