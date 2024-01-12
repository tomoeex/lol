# โปรแกรมนี้มีฟังก์ชัน c ที่รับ parameter 2 ตัวคือ width และ height
# โดยมี default parameter คือ 1
# และใช้ keyword argument เมื่อเรียกใช้งานฟังก์ชัน

def c(width=10, height=15):
    """
    ฟังก์ชันนี้รับ width และ height เพื่อคำนวณพื้นที่สี่เหลี่ยมผืนนี้
    """
    area = width * height
    return area

# เรียกใช้ฟังก์ชัน cโดยไม่ระบุพารามิเตอร์ใด ๆ
result1 = c()
print("พื้นที่: ", result1)

# เรียกใช้ฟังก์ชัน calculate_area โดยระบุค่า width เป็น 4 และ height เป็น 5
result2 = c(width=5, height=10)
print("พื้นที่: ", result2)
