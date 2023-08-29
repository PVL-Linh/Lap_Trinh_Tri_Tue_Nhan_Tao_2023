"""
Câu 2. Viết chương trình nhập vào từ bàn phím một chuỗi S .
Hãy tạo từ điển D trong đó key là các chữ cái xuất hiện trong S (chữ cái không được trùng nhau ) ,
value tương ứng với số lần xuất hiện của các chữ cái trong S .
"""

s = input("Nhập chuỗi S :")
dem = {}
for i in s :
    if i in dem :
        dem[i] +=1
    else:
        dem[i] = 1
print(dem)

