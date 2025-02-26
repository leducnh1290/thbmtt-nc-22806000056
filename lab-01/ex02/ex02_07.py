# Nhập thông tin người dùng
print("Nhập thông tin người dùng (Nhập 'done' để kết thúc):")
line =  []
while True:
    line = input()
    if line.lower() == 'done':
        break
    line.append(line)
    #Chuyển các dòng thành chữ in hoa và in ra màn hình
    for i in line:
        print(i.upper())