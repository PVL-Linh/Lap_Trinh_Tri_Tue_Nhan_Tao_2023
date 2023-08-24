"""
Câu 14. Cho tập tin thống kê môn học với tên k2021.csv nội dung như sao :
a)	Viết câu lệnh đọc file k2021.csv >
b)	In 5 dòng đầu tiên và 5 dòng cuối cùng của dữ liệu ra màn hình?
c)	Thống kê xem lớp có bao nhiêu bạn trượt môn (điểm dưới 4 hoặc không có điểm )
d)	Thống kê xem lớp có bao nhiêu bạn điểm loại giỏi (điểm từ 8 trở lên )

"""
import pandas as pd

a = pd.read_csv("./data/k2020.csv" , index_col=0)

#B

print(a.head(5))
print(a.tail(5))
# C

print(f"So luong hoc sinh dat loai gioi la : " ,len(a[a.Diem >=8]) , " sinh vien ")
print(f"So luong sinh vien truoc mon la : " , len(a[(a.Diem < 4  )|( a.Diem.isnull())]) , " sinh vien ")


