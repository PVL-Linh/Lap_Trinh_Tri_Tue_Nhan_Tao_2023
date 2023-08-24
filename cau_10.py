"""
Câu 11. Hiện thức lớp đối tượng SINHVIEN với các thuộc tính và phương thức sau :
	Thuộc tính :
	MSSV : chuỗi
	HOTEN :chuỗi
	DIEMKT1 : số thực
	DIEMKT2 : số thức
	DIEMTB : (DIEMKT1+DIEMKT2)/2
	Phương thức :
•	Thêm thông tin sinh viên
•	Sửa thông tin sinh viên
•	Xuất thông tin sinh viên
a)	Hãy xây dựng các hàm cần thiết để cho phép nhập vào từ bàn phím các thông tin
    để thực danh sách (List) các đối tượng SINHVIEN
b)	Sắp xếp và xuất ra danh sách (List) các đối tượng SINHVIEN theo thứ tự DIEMTB từ cao đến thấp

"""
class SINHVIEN:
    def __init__(self , MSSV , HOTEN , DIEMKT1 , DIEMKT2 ):
        self.MSSV =MSSV
        self.HOTEN = HOTEN
        self.DIEMKT1 = DIEMKT1
        self.DIEMKT2 = DIEMKT2
        self.DIEMTB = (DIEMKT1+DIEMKT2)/2

    def nhap_Thong_Tin_SV (seft):
        seft.MSSV = input("Ma so sinh vien : ")
        seft.HOTEN = input("Ten sinh vien : ")
        test = True
        while test == True:
            seft.DIEMKT1 = float(input("Diem kiem tra 1 : "))
            seft.DIEMKT2 = float(input("Diem kiem tra 2 : "))
            if (0<= seft.DIEMKT1 <= 10) & ( 0 <=  seft.DIEMKT2 <= 10):
                break
            else:
                print("diem kiem tra >=0 va <= 10")
                test = True
        seft.DIEMTB = (seft.DIEMKT1 + seft.DIEMKT2) / 2

    def sua_Thong_Tin_SV (seft):
        seft.HOTEN = input("Nhap ho ten : ")
        test = True
        while test == True:
            seft.DIEMKT1 = float(input("Diem kiem tra 1 : "))
            seft.DIEMKT2 = float(input("Diem kiem tra 2 : "))
            if (0 <= seft.DIEMKT1 <= 10) & (0 <= seft.DIEMKT2 <= 10):
                break
            else:
                print("diem kiem tra >=0 va <= 10")
                test = True
        seft.DIEMTB = (seft.DIEMKT1 + seft.DIEMKT2) / 2


    def hien_Thi_Thong_Tin (seft):
        print("Ma so sinh vien : " , seft.MSSV)
        print("Ho & ten : " , seft.HOTEN)
        print("Diem kiem tra 1 : " , seft.DIEMKT1)
        print("Diem kiem tra 2 : " , seft.DIEMKT2)
        print("Diem Trung binh : " , ((seft.DIEMKT1 + seft.DIEMKT2) / 2))
        print(" ")
danh_sach_sinh_vien = []

def them_Thong_tin_vao_danh_sach ():
    number_sv = int(input("So luong sinh vien "))
    for i in range (number_sv):
        print(f"Nhap thong tin sinh vien {i + 1} : ")
        sinh_Vien = SINHVIEN("" , "" , 0 , 0 )
        sinh_Vien.nhap_Thong_Tin_SV()
        danh_sach_sinh_vien.append(sinh_Vien)
    return danh_sach_sinh_vien

def sua_Thong_Tin_SV ():
    mssv = input("Nhap ma sinh vien : ")
    for i in danh_sach_sinh_vien :
        if  i.MSSV == mssv:
            i.sua_Thong_Tin_SV ()
            print("Da cap nhat thong tin ")
            return
        print("Khong tim thay Ma so sinh vien nay !!!")
def delete_SV ():
    mssv = input("Nhap ma sinh vien ")
    for i in danh_sach_sinh_vien:
        try:
            if i.mssv == mssv:
                danh_sach_sinh_vien.remove(mssv)
                print("Thong tin sinh vien ", mssv, " da duoc xoa ")
                return
        except ValueError:
            print("Khong tin thay ma sinh vien  !!! " )

def sap_Xep ():
    danh_sach = sorted(danh_sach_sinh_vien , key=lambda sv : sv.DIEMTB , reverse=True )
    for i in danh_sach :
        i.hien_Thi_Thong_Tin ()
while True:
    print("----------MENU------------")
    print("1 : Them thong tin sv")
    print("2 : Sua thong tin sv")
    print("3 : Xoa thong tin sv")
    print("4 : Hien thi thong tin sv")
    print("5 : Sap xep diem sv ")
    print("0 : Thoat chuong trinh ")

    chon = int(input("Nhap so chon : "))

    if chon ==1 :
        them_Thong_tin_vao_danh_sach()
    elif chon == 2 :
        sua_Thong_Tin_SV()
    elif chon == 3:
        delete_SV()
    elif chon == 4 :
        for i in danh_sach_sinh_vien:
            i.hien_Thi_Thong_Tin ()
    elif chon == 5 :
        sap_Xep()
    elif chon ==0 :
        break
