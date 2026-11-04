tests = {
    # Câu 1a: Kiểm tra số chẵn/lẻ
    "Cau1a": [
        {"input": "4\n", "expected": ["chan"]},
        {"input": "7\n", "expected": ["le"]},
        {"input": "0\n", "expected": ["chan"]},
        {"input": "-3\n", "expected": ["le"]}
    ],

    # Câu 1b: Nhập tên và tuổi, in theo mẫu
    "Cau1b": [
        {"input": "An\n20\n", "expected": "Xin chào An, bạn 20 tuổi."},
        {"input": "Long\n18\n", "expected": "Xin chào Long, bạn 18 tuổi."},
        {"input": "Hà\n22\n", "expected": "Xin chào Hà, bạn 22 tuổi."}
    ],

    # Câu 2a: Tính tổng các số chẵn trong đoạn
    "Cau2a": [
        {"input": "2\n10\n", "expected": ["30"]},
        {"input": "5\n11\n", "expected": ["24"]},
        {"input": "3\n3\n", "expected": ["0"]},
        {"input": "4\n4\n", "expected": ["4"]},
        {"input": "-2\n2\n", "expected": ["0"]}
    ],

    # Câu 2b: Đếm chữ số trong đoạn chuỗi
    "Cau2b": [
        {"input": "abc12345\n1\n8\n", "expected": ["5"]},
        {"input": "a1b2c3d4e5\n2\n9\n", "expected": ["4"]},
        {"input": "python3.9\n7\n9\n", "expected": ["2"]},
        {"input": "abcdef\n1\n6\n", "expected": ["0"]},
        {"input": "a2b\n2\n2\n", "expected": ["1"]}
    ],

    "Cau3a": [
        {"input": "", "expected": ["['apple', 'banana']"]}
    ],

    "Cau3b": [
        {
            "input": "",
            "expected": [
                "[100, 'apple', 3.14, 'banana', 200, None, 'orange']",
                "[100, 'apple', 'banana', 200, None, 'orange']",
                "['orange', None, 200, 'banana', 'apple', 100]"
            ]
        }
    ],

    "Cau4a": [
        {"input": "", "expected": ["apple", "cherry", "coc"]}
    ],

    "Cau4b": [
        {"input": "", "expected": ["(1, 2, 3, 4)", "(1, 2, 1, 2, 1, 2)"]}
    ],

    "Cau5a": [
        {"input": "", "expected": ["{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}"]}
    ],

    "Cau5b": [
        {"input": "", "expected": ["['An', 'Cuong', 'Hoa']"]}
    ]
}
