"""
Câu 8. Viết chương trình Python nhập một dãy số nguyên cách nhau bởi khoảng trắng ,
sau đó kiểm tra xem nó có đối xứng hay không ?
Nếu dãy số nhập vào không đối xứng , kiểm tra xem có thể biến đổi nó để trở thành đối xứng hay không ?
Nếu có khả năng đối xứng thì biến đổi nó trở thành đối xứng , ngược lại xuất ra màn hình KHÔNG CÓ KHẢ NĂNG ĐỐI XỨNG .
"""
def check_DoiXungKhong (number):
    if number == number[::-1]:
        return True
    return False

def bienDoi (number):
    if check_DoiXungKhong(number) == False:
        list_number = number+number[::-1]
    return list_number

number = int(input("day so"))
number_str = str(number)
number_list = list(number_str)
if check_DoiXungKhong(number_list) :
    print("Day so " ,number_str ," doi xung nhau" )
else:
    print("day so " , number_str," khong doi xung nhau")
    print("Bien doi day so tren thanh doi xung : " , (bienDoi(number_list)))


