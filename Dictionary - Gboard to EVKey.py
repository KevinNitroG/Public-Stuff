input=""" """

list = []
for i in input.split("\n"):
    list.append(i.split("\t"))

for i in list:
    print("||".join(i)[:-2])

#Made by LongTo
#Xuất Từ điển của GBoard
#Giải nén
#Copy toàn bộ
#Chạy chương trình Python này và paste vào
#Copy kết quả vào file mẫu từ điển của EVKey
#Reload từ điển EVKey
