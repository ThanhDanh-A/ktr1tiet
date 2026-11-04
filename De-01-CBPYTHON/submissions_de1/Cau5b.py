# Cau 5b: Loc ten hoc sinh co diem dat muc toi thieu

score = {"An": 8, "Binh": 6, "Cuong": 9, "Dung": 5, "Hoa": 8}


def get_high_scores(d, min_score):
    """Tra ve danh sach ten co diem lon hon hoac bang min_score."""
    danh_sach_dat = []

    for ten, diem in d.items():
        if diem >= min_score:
            danh_sach_dat.append(ten)

    return danh_sach_dat


print(get_high_scores(score, 8))
