# โปรแกรมนี้ใช้ฟังก์ชัน c ที่รับ parameter 2 ตัวคือ w และ h
# และใช้ keyword argument เมื่อเรียกใช้งานฟังก์ชัน

def c(w, h):
    """
    ฟังก์ชันนี้คำนวณพื้นที่สี่เหลี่ยมผืนนี้
    """
    area = w * h
    return area

# เรียกใช้ฟังก์ชัน c โดยระบุ w และ h ใช้ keyword argument
result = c(w=10, h=5)
print("พื้นที่สี่เหลี่ยมผืนนี้คือ: ", result)
