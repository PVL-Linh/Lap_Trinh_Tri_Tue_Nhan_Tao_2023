"""
Viết chương trình cho phép nhập vào từ bàn phím họ và tên đầy đủ của sinh viên trong lớp ,
mỗi sinh viên được nhập trên một dòng .Việc nhập sẽ kết thúc khi người dung gõ vào dòng trống .
Sau đó , hãy in ra tất cả các họ và tên không trùng nhau của sinh viện trong lớp.
"""



student = []
while True:
    fullname = input("Ho & ten :")
    if fullname == "":
        break
    else:
        student.append(fullname)

list_Student = set(student)     # ham set thuc hien loc cac ten trung nhau

for i in list_Student:
    print(i)


