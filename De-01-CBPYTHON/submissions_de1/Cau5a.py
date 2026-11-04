# Cau 5a: Dem tan suat xuat hien cua tung ky tu

def count_freq(s):
    """Tra ve dictionary dem so lan xuat hien cua moi ky tu trong s."""
    tan_suat = {}

    for ky_tu in s:
        if ky_tu in tan_suat:
            tan_suat[ky_tu] += 1
        else:
            tan_suat[ky_tu] = 1

    return tan_suat


ket_qua = count_freq("hello world")
print(ket_qua)
