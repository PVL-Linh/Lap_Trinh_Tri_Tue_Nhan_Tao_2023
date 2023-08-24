"""
Câu 3. Cho tập tin text.txt với nội dụng : dsak1257$%3*&4pk6819
Xây dựng hàm đọc nội dung tập tin text.txt .
Thực hiện lọc và lấy số lẻ đưa vào danh sách (List ) SoLe và các số chẵn đưa vào danh sách list SoChan

"""
chan = []
le = []
try:
    with open("./data/test.txt", encoding="utf-8") as f:
        a = f.read()
    for i in a:
        if (i.isdigit()):
            i = int(i)
            if (i % 2 == 0):
                chan.append(i)
            else:
                le.append(i)
except FileNotFoundError:
    print("Khong tin thay file")

print(" số chẳn " , chan)
print("Số lẽ : " , le)









