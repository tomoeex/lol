# นี่คือฟังก์ชัน x ที่รับพารามิเตอร์ 4 ตัว คือ name, age, gender, และ number
def x(name, age, gender, number):
    """
    ฟังก์ชัน x นี้รับพารามิเตอร์ 4 ตัวคือ name, age, gender, และ number
    และพิมพ์ข้อมูลของพารามิเตอร์ทั้ง 4 ออกทางหน้าจอ
    """
    print(f"name : {name}, age: {age}, gender: {gender} number:{number} ")

# เรียกใช้ฟังก์ชัน x โดยใช้ keyword argument
x(gender='Male', name='oat', age=22, number=1)



