# โปรแกรมนี้มีฟังก์ชัน c ที่รับ parameter 2 ตัวคือ value1 และ value2
# โดยมี default parameter คือ 0
# และใช้ keyword argument เมื่อเรียกใช้งานฟังก์ชัน

def c(value1=0, value2=0):
    """
    ฟังก์ชันนี้รับ value1 และ value2 เพื่อคำนวณผลรวมของค่าทั้งสอง
    """
    total = value1 + value2
    return total

# เรียกใช้ฟังก์ชัน c โดยไม่ระบุพารามิเตอร์ใด ๆ
result1 = c()
print("ผลรวม: ", result1)

# เรียกใช้ฟังก์ชัน calculate_total โดยระบุค่า value1 เป็น 10 และ value2 เป็น 5
result2 = c(value1=10, value2=5)
print("ผลรวม: ", result2)
