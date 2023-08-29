"""
Viết chương trình nhạp vào một mảng hai chiều các số thực A ( m hàng , n cột ) từ bàn phím .
a.	Tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột
b.	Tìm phần tử lớn nhất và phần tử nhỏ nhất của mảng A  cùng các chỉ số hàng và cột của 2 phần tử này.
c.	Trong mảng A có bao nhiêu phần tử lớn nhất .
"""
import numpy as np

# A ) Tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột
def max_min_rows (matrix):
    max_cols = np.max(matrix, axis=0)
    min_cols = np.min(matrix, axis=0)
    return  max_cols , min_cols

# B) Tìm phần tử lớn nhất và phần tử nhỏ nhất của mảng A  cùng các chỉ số hàng và cột của 2 phần tử này.
def max_min_cols_chiSo (matrix):
    max_matrix = np.max(matrix)
    seach_matrix_max = np.where(matrix == max_matrix)
    seach_matrix_max  = seach_matrix_max[0][0], seach_matrix_max[1][0]

    min_maxtrix = np.min(matrix)
    seach_matrix_min = np.where(matrix==min_maxtrix)
    seach_matrix_min = seach_matrix_min[0][0] , seach_matrix_min[1][0]

    return max_matrix, seach_matrix_max , min_maxtrix , seach_matrix_min
# C ) Trong mảng A có bao nhiêu phần tử lớn nhất .
def count_max (matrix):
    max_matrix = np.max(matrix)
    count_max_matrix = np.count_nonzero(matrix == max_matrix)
    return  count_max_matrix

m = int(input("hang :"))
n = int(input("Cot : "))

matrix = np.zeros((n , m ))

for i in range(n):
    for j in range(m):
        matrix[i][j] = float(input("Phan tu trong mang "))

max_cols , min_cols = max_min_rows(matrix)
max_matrix  , seach_max , min_matrix , seach_min = max_min_cols_chiSo(matrix)
count_max = count_max(matrix)

print("Gia tri lon nhat cua cot",max_cols )
print("Gia tri lon nhat cua cot",min_cols)
print("----------------")
print("Gia tri lon nhat cua matrix ",max_matrix)
print("Chi so cua phan tu lon nhat ",seach_max)
print("Gia tri nho nhat cua matrix ",min_matrix)
print("Chi so cua phan tu nho nhat ",seach_min)
print("----------------")
print("So luong phan tu lon nhat ",count_max)
