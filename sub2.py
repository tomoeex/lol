# ฟังก์ชันแรก: เพิ่มสองตัวเลข
def add_num(a, b):
    """
    ฟังก์ชันนี้รับสองอาร์กิวเมนต์ a และ b และคืนผลรวมของทั้งสอง
    """
    result = a + b
    return result

# ฟังก์ชันที่สอง: คูณสองตัวเลข
def mu_num(x, y):
    """
    ฟังก์ชันนี้รับสองอาร์กิวเมนต์ x และ y และคืนผลคูณของทั้งสอง
    """
    result = x - y
    return result

# ใช้ฟังก์ชัน add_numbers เพื่อบวก 5 กับ 3 และพิมพ์ผลลัพธ์
s = add_num(5, 3)
print("ผลบวก: ", s)

# ใช้ฟังก์ชัน multiply_numbers เพื่อคูณ 4 กับ 6 และพิมพ์ผลลัพธ์
multiply_result = mu_num(4, 6)
print("ผลลบ: ", s)