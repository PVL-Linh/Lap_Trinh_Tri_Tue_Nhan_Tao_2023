"""
Câu 13. Viết chương trình python theo OOP.
-	Class InHoaDon (in ra hóa đơn)
    bán hàng Rau Qủa trong đó các thuộc tính .
-	Ngay , LoaiRauQua , SoLuong , DonGia , ThanhTien.

"""
from datetime import datetime

class InHoaDon:
    def __init__(self , ngay , LoaiRauQua , SoLuong , DonGia ):
        self.ngay = ngay
        self.LoaiRauQua = LoaiRauQua
        self.SoLuong = SoLuong
        self.DonGia = DonGia
        self.ThanhTien = self.SoLuong * self.DonGia
    def hien_Thi (seft):
        print("------- Hoa Don ------------")
        print("Ngay mua hang : " , seft.ngay)
        print("Loai rau qua : " , seft.LoaiRauQua)
        print("So luong : " , seft.SoLuong)
        print("Don Gia : " , seft.DonGia)

ngay = str(datetime.now())
loaiRauQua = input("Loai rau qua : ")
while True:
    soLuong = int(input("So luong : "))
    donGia = int(input("Don gia : "))
    if soLuong < 0 or donGia < 0:
        print("Vui long nhap loai")
    else:
        break
hoaDon = InHoaDon(ngay , loaiRauQua , soLuong , donGia)
hoaDon.hien_Thi()

