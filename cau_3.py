"""
Câu 4. Viết  tính tần suất xuất hiện của các từ được nhập vào từ input .
In ra màn hình danh sách các từ sau khi đã được sắp xếp theo chữ cái .
"""

nhap = input("Nhâp chuỗi chữ : ")
def xuatHien ( nhap ):
    dem = {}
    for i in nhap:
        if i in dem:
            dem[i] += 1
        else:
            dem[i] = 1
    SapXep = sorted(dem.keys())
    return dem , SapXep
dem , SapXep = xuatHien(nhap)
print("Đã được sắp xếp",SapXep)


