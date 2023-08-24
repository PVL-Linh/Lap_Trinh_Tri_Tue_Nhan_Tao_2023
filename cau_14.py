"""
Câu 15. Dữ liệu : winequality-red.csv có các số đo và chắc lượng của rựu vang đó , các thuộc tính .
a.	Viết chương trình Python :
In ra xem bao nhiêu dòng và bao nhiêu cột trong file.
b.	Vẽ biểu đồ mình họa Dataset với thuộc tính alcohol và điểm của quality.
c.	Sử dụng hồi quy tuyến tính để xây dựng quan giữa thuộc tính alcohol và quality:
    - In ra độ lệch chuẩn ( căn bặc 2 phương sai )
    Hồi số hồi quy
    Sai số
    Dự báo về chất lượng rượu khi cho nồng độ alcohol thay đổi ( Nhập)

"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model , metrics
data = pd.read_csv("./data/winequality-red.csv" , index_col=0)

print("Cot trong data winequality-red.csv : ",len(data.columns))
print(data.columns)
alcohol = data['alcohol']
quality = data['quality']
plt.plot(alcohol , quality ,"go")
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.show()

x = alcohol.values.reshape(-1,1)
y = quality.values.reshape(-1 , 1)


model = linear_model.LinearRegression()
model.fit(x,y)

mse = metrics.mean_squared_error(model.predict(x) , y)

print("Tong binh phuong sai so tren tap mau " , mse)
print("he so hoi quy : " , model.coef_)
print("Sai so " , model.intercept_)

while True :
    z = float(input("nhap nong do alcohol (nhap 0 de dung )"))
    if z == 0:
        break
    print("Nong do ruou " , z , " do , du bao chat luong " , model.predict([[z]]))
