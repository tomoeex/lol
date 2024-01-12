# โปรแกรมนี้ใช้ฟังก์ชัน d ที่รับ parameter ชื่อของผู้ใช้ (name)
# โดยกำหนด default parameter ให้ name เป็น "Guest"

def d(name="tom"):
    """
    ฟังก์ชันนี้สร้างข้อความทักทายผู้ใช้
    """
    o = f"Hi, {name}!"
    print(o)

# เรียกใช้ฟังก์ชัน d โดยไม่ระบุชื่อ
d()

# เรียกใช้ฟังก์ชัน d โดยระบุชื่อเป็น "oat"
d("mai")
