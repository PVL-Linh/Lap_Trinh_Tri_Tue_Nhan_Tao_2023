"""
Câu 9. Định nghĩa một hàm có thể tạo ra một dictionary chứa key là những số từ 1 đến 10 (bao gồm cả 1 và 10 )
và các value là các số nguyên tố khác nhau (nếu người dùng nhập vào một số không phải số nguyên tố hoặc
số nguyên tố đã được nhập vào trước đó thì yêu cầu người dùng nhập lại đến khi nào hoàn tất việc nhập 10 value .
in ra value lon nhat của dictionary .
"""
def check (soNT):
    if soNT > 2 :
        for i in (2 , soNT):
            if soNT % i != 0 :
                return soNT
            else:
                soNT = 1


d = dict()

for i in range(1,10):
    while True:
        value = int(input("Nhap value ( la so nguyen to ) : "))
        print(check(value))
        if (check(value) == value):
            d[i] = value
            break
        else:
            print("Khong phai so nguyen to ")
print("Max : " ,max(d.values()))



