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
def delete_Giong (numbuer):
    mang = []
    for i in number :
        mang.append(i)
    for i in numbuer:
        for j in range (mang.count(i)):
            mang.remove(i)
def co_The_Doi_Xung_Khong (number ):
    mang = []
    mang_kem = []
    dem = 0
    dem3 = 0
    for i in number :
        mang.append(i)
    mang = sorted(mang)
    mang_copy = mang
    if check_DoiXungKhong(number) == False:
        for i in mang :
            if mang_copy.count(i) == 1 :
                dem+=1
            elif mang_copy.count(i) == 3:
                dem3+=1
            if (dem > 1 or dem3 >= 2 )or (dem == 1 & dem3==1):
                return ("Khong the bien doi ")
            else:
                for i in mang:
                    if mang.count(i) % 2 == 0 :
                        if i == mang[mang.index(i) + 1]:
                            mang.remove(mang[mang.index(i) + 1])


                    elif mang.count(i) % 3 == 0:

                        if mang_copy.count(i)//3 ==0:
                            mang_kem.append(i)
                        del mang[mang.index(i) or mang.index(i) + 1]
                        mang_kem.append(i)
                return (mang[::-1]  + mang_kem + mang)


number = int(input("day so"))
number_str = str(number)
if check_DoiXungKhong(number_str) :
    print("Day so " ,number_str ," doi xung nhau" )

else:
    print("day so " , number_str," khong doi xung nhau")
    print("Bien doi ", co_The_Doi_Xung_Khong(number_str))



