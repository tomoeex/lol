# โปรแกรมนี้ใช้ global variable ชื่อ g
g = 20

# ฟังก์ชันที่เพิ่มค่า g ด้วยตัวแปร l
def i():
    """
    ฟังก์ชันนี้เพิ่มค่าของ g ด้วย l
    """
    global g
    l = 5
    g += 2

# ใช้ฟังก์ชัน i เพื่อเพิ่มค่า g
i()
print("ค่าที่ออกมา: ", g)
