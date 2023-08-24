"""
Câu 12: Thực hiện lớp đối tượng QUEUE và các thuộc tính và phương thức sau:
	Thuộc tính :
	Element : danh sách (List)
	Front : số nguyên
	Phương thức :
•	Kiểm tra hàng đợi rổng
•	Trả về phần tử ở hàng đợi
•	Thêm một phần tử vào hàng đợi
•	Xóa phần tử ở hàng đợi
•	Xuất hàng đợi ra màn hình

a)	Hãy xây dựng các hàm cần thiết bắt buộc người nhập vào một số nguyên tố
    ( nếu giá trị nhập vào không phải số nguyên tố thì cần thiết yêu cầu phải nhập vào ) .
    Thêm các số nguyên tố được nhập vào hàng đợi Q là đối tượng kế thừa từ lớp QUEUE .
    Xuất ra màn hình hàng đợi Q .

b)	Tuần tự thực hiện các thao tác sao khi hàng đợi Q rỗng :
    Tìm và xuất ra màn hình phần tử đầu danh sách Q :
    Xóa phần tử đầu danh sách Q và xuất ra màn hình hàng đợi Q.

"""
class Queue :
    def __init__(self):
        self.Element = []
        self.Front = None

    # kiem tra hang doi co rong hay khong
    def is_empty (sefl):
        return len(sefl.Element) == 0

    # phan tu dau trong hang doi
    def get_front(self):
        return self.Front

    # thêm một phần tử vào cuối hàng đợi
    def enqueue (self , item):
        self.Element.append(item)
        if self.Front is None :
            self.Front = item

    # loại bỏ phần tử đầu tiên khỏi hàng đợi
    def dequeue (seft ):
        if not seft.is_empty():
            seft.Element.pop(0)             # pop(0) la ham bo phan tu dau trong hang doi
            if not seft.is_empty():
                seft.Front =seft.Element[0]
            else:
                seft.Front = None
        else:
                print("Hang doi rong")
    # hiển thị các phần tử trong hàng đợi
    def dispalay (seft):
        if not seft.is_empty():
            print("hang doi")
            for i in seft.Element:
                print(i)
        else :
            print("hang doi rong ")
def is_so_Nguyen_To ( n ) :
    if n < 2:
        return False
    for i in range(2, int(n**0.5 )+1):
        if n % i == 0:
            return False
    return True

Q = Queue()

while True :
    num = int(input("Nhap so nguyen to "))
    try :
        if is_so_Nguyen_To(num):
            Q.enqueue(num)
        else:
            print("Vui long nhap lai so nguyen to ")
    except ValueError :
        print("Vui long nhap lai so nguyen to")

    chon = input("Tiep tuc hay khong ? (y , n )")
    if chon.lower() == "n":          # ham lower dung de chuyen doi ki tu viet hoa thanh viet thuong
        break

Q.dispalay()

while not Q.is_empty():
    print("Phan tu dau trong danh sach " , Q.get_front())
    Q.dequeue()
    Q.dispalay()




