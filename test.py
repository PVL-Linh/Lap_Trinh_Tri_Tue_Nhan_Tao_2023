import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# a. In ra số dòng và số cột trong file
data = pd.read_csv('./data/winequality-red.csv')
so_dong, so_cot = data.shape
print("Số dòng trong file:", so_dong)
print("Số cột trong file:", so_cot)

# b. Vẽ biểu đồ minh họa quan hệ giữa thuộc tính alcohol và điểm quality
alcohol = data['alcohol']
quality = data['quality']
plt.scatter(alcohol, quality)
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.title('Quan hệ giữa Alcohol và Quality')
plt.show()

# c. Sử dụng hồi quy tuyến tính để xây dựng mô hình quan hệ giữa alcohol và quality
X = alcohol.values.reshape(-1, 1)
y = quality.values.reshape(-1, 1)

model = LinearRegression()
model.fit(X, y)

# In ra độ lệch chuẩn (căn bậc hai của phương sai)
variance = mean_squared_error(y, model.predict(X))
std_deviation = variance ** 0.5
print("Độ lệch chuẩn:", std_deviation)

# Hệ số hồi quy
coefficient = model.coef_[0][0]
print("Hệ số hồi quy:", coefficient)

# Sai số
intercept = model.intercept_[0]
print("Sai số:", intercept)

# Dự báo chất lượng rượu khi cho nồng độ alcohol thay đổi (nhập)
nong_do_alcohol_nhập = float(input("Nhập nồng độ alcohol: "))
du_bao_quality = model.predict([[nong_do_alcohol_nhập]])
print("Dự báo chất lượng rượu:", du_bao_quality[0][0])