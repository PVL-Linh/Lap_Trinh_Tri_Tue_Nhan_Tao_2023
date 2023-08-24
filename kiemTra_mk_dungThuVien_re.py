def is_valid_password(password):
    # Kiểm tra độ dài của mật khẩu
    if len(password) < 6 or len(password) > 12:
        return False

    # Kiểm tra chữ cái thường
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        return False

    # Kiểm tra chữ cái hoa
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        return False

    # Kiểm tra số
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        return False

    # Kiểm tra ký tự đặc biệt
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-']
    has_special_char = False
    for char in password:
        if char in special_chars:
            has_special_char = True
            break
    if not has_special_char:
        return False

    return True


# Nhập mật khẩu từ người dùng
passwords = input("Nhập các mật khẩu, phân cách nhau bởi dấu phẩy: ").split(",")

# Kiểm tra tính hợp lệ của từng mật khẩu và in ra mật khẩu hợp lệ
valid_passwords = []
for password in passwords:
    password = password.strip()
    if is_valid_password(password):
        valid_passwords.append(password)

# In danh sách các mật khẩu hợp lệ
print("Các mật khẩu hợp lệ:")
print(", ".join(valid_passwords))