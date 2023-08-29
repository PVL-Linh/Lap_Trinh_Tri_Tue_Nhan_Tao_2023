"""
Câu 10. Hiện thực lớp đối tượng DIENTHOAI với các đặc điểm sau:
	Thuộc tính :
	HANGSX: chuỗi .
	MODEL : chuỗi
	GIATIEN : số nguyên
	MANHINH (kích thước màn hình ): số thực
	Phương thức :
•	Thêm thông tin điện thoại
•	Sửa thông tin điện thoại
•	Xóa thông tin điện thoại
•	Xuất thông tin điện thoại
a)	Hãy xây dựng các hàm cần thiết để cho phép nhận vào từ bàn phím các thông tin để thực hiện danh sách (List)
    các đối tượng  DIENTHOAI
b)	Sắp xếp và xuất ra danh sách (List) các đối tượng DIENTHOAI theo thứ tự kích thước màn hình lớn đến nhỏ

"""

class DienThoai:

    def __init__(self ,hangsx, model, giatien, manhinh):
        self.HANGSX = hangsx
        self.MODEL = model
        self.GIATIEN = giatien
        self.MANHINH = manhinh

    def hien_Thi_Thong_Tin (self):
        print("Hang san xuat : ",self.HANGSX)
        print("Model : " , self.MODEL)
        print("Gia tien : " , self.GIATIEN)
        print("Kich thuoc man hinh " , self.MANHINH)

danhSach_SP = []
def them_thong_tin ():
    hangsx = input("Hang SX : ")
    model = input("Model : ")
    giatien = int(input("Gia Tien : "))
    manhinh = float(input("Man hinh :"))
    dien_Thoai = DienThoai(hangsx , model , giatien , manhinh)
    danhSach_SP.append(dien_Thoai)
def sua_Thong_Tin ():
    model = input("Sua model ")
    for i in danhSach_SP:
        if i.MODEL == model:
            hangsx = input("Sua hang san xuat : ")
            giatien = input("Sua gia tien : ")
            manhinh = input("Sua thong so Man Hinh : ")

            i.HANGSX = hangsx
            i.GIATIEN = giatien
            i.MANHINH = manhinh
            print("Thong tin dien san pham da duoc cap nhat ")
            return
    print("Khong tin thay dia chi model")

# Xóa thông tin điện thoại
def delete_SP ():
    model = input("Thong so model : ")
    for i in danhSach_SP:
        if i.MODEL == model:
            danhSach_SP.remove(i)
            print("San pham da duoc xoa !!! ")
            return
    print("Khong tim thay model ???")

# Sap Xep thông tin điện thoại
def sort_SP ():
    sort_SanPham =  sorted(danhSach_SP,key=lambda i : i.MANHINH , reverse=True)
    for i in sort_SanPham:
        i.hien_Thi_Thong_Tin()
while True:
    print("----- MENU -----")
    print("1. Thêm điện thoại")
    print("2. Sửa thông tin điện thoại")
    print("3. Xóa điện thoại")
    print("4. Xuất danh sách điện thoại")
    print("5. Sắp xếp và xuất danh sách theo kích thước màn hình")
    print("0. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ")

    if choice == "1":
        them_thong_tin()
    elif choice == "2":
        sua_Thong_Tin()
    elif choice == "3":
        delete_SP()
    elif choice == "4":
        for dt in danhSach_SP:
            dt.hien_Thi_Thong_Tin()
    elif choice == "5":
        sort_SP()
    elif choice == "0":
        break