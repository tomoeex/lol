# โปรแกรมนี้ใช้ global variable ชื่อ t
t = 0

# ฟังก์ชันที่เพิ่มค่าใน t
def a(value):
    """
    ฟังก์ชันนี้รับค่าและเพิ่มค่านั้นใน t
    """
    global t
    t += value

# ใช้ฟังก์ชัน a เพื่อเพิ่มค่าใน t
a(8)
a(4)

print("ค่าที่ได้: ", t)
