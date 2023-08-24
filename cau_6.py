"""
Câu 7. Viết chương trình để kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào .
Các tiêu chí kiểm tra mật khẩu bao gồm :
    1.	Ít nhất 1 chữ cái nằm tròng [a-z]
    2.	Ít nhất 1 số nằm trong [0-9]
    3.	Ít nhất 1 kí tự nằm trong [A-Z]
    4.	Ít nhất 1 ký tự nằm trong [S#@]
    5.	Độ dài mật khẩu tối thiểu là 6
    6.	Độ dài tối da là 12
Chương trình phải chấp nhận mật khẩu phân cách nhâu bởi dấu  ,
và kiểm tra xe chúng có đap ứng những tiêu trí trên hay không .
Mật khẩu hợp lệ sẽ được in , mỗi mật khẩu cách nhau bởi dấu phẩy
Vd : mật khẩu nhập vào chương trình là : Abd1234@1,aF1#,2wE*,2We3345
Thì đầu ra là Abd1234@1

"""
import numpy as np


def checkPassword (matkhau):


    # Ít nhất 1 chữ cái nằm tròng [a-z]
    if not np.any([char.islower() for char in matkhau]):
        return False

    # 2.	Ít nhất 1 số nằm trong [0-9]
    if not np.any([char.isdigit() for char in matkhau]):
        return False

    # 3.	Ít nhất 1 kí tự nằm trong [A-Z]
    if not np.any([char.isupper() for char in matkhau]):
        return False

    # 4.	Ít nhất 1 ký tự nằm trong [S#@]
    ky_Tu = ['$','@',"#"]
    if not np.any([char in ky_Tu for char in matkhau]):
        return False

    # 5.	Độ dài mật khẩu tối thiểu là 6
    # 6.	Độ dài tối da là 12
    if len(matkhau) < 6 or len(matkhau)>12:
        return False

    return  True

matKhau = input("Nhap mat khau : ").split(",")

TinhHopLe = []
for i in matKhau:
    i = i.strip()
    if checkPassword(i):
        TinhHopLe.append(i)
if len(TinhHopLe) == 0:
    print("Mat khau khong hop le ")
else:
    print("mat khau hop le /n".join(TinhHopLe))
