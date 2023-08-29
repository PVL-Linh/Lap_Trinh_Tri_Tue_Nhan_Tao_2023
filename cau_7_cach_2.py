"""
Câu 8. Viết chương trình Python nhập một dãy số nguyên cách nhau bởi khoảng trắng ,
sau đó kiểm tra xem nó có đối xứng hay không ?
Nếu dãy số nhập vào không đối xứng , kiểm tra xem có thể biến đổi nó để trở thành đối xứng hay không ?
Nếu có khả năng đối xứng thì biến đổi nó trở thành đối xứng , ngược lại xuất ra màn hình KHÔNG CÓ KHẢ NĂNG ĐỐI XỨNG .
"""
def check_DoiXungKhong (number):
    if number == number[::-1]:
        return True
    return False

def doi_Str_thanh_List (number ):
    mang = []
    for i in number :
        mang.append(i)
    mang.sort()
    return mang

def not_edit_Doi_Xung (number):
    dem1 = 0
    dem_Le = 0
    for i in number:
        if number.count(i) == 1:

            dem1+=1
        elif number.count(i) % 3 == 0:
            dem_Le+=1
    if dem1 >= 2 or dem_Le>3:
        return False
    return True
def edit_DoiXung (number):
    right = []
    left = []
    mid = []
    for i in number:
        if number.count(i) % 2 == 0 :
            if number.count(i) == 2 :
                if i not in right :
                    right.append(i)
                elif i not in left:
                    left.append(i)
            else:
                if right.count(i) < (number.count(i)//2) :
                    right.append(i)
                elif left.count(i) < (number.count(i)//2):
                    left.append(i)
        else:
            mid.append(i)
    return (left+mid+right[::-1])




number = int(input("day so"))
number_str = str(number)
mang = doi_Str_thanh_List(number_str)

if check_DoiXungKhong(number_str) :
    print("Day so " ,number_str ," doi xung nhau" )

else:
    print("day so ", number_str, " khong doi xung nhau")
    print(not_edit_Doi_Xung(mang))
    if not_edit_Doi_Xung(mang) == True :
        print("Bien doi ", edit_DoiXung(mang))
    else:
        print("Khong the bien doi")



