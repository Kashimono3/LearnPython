# Câu 1 
print("Twinkle, twinkle, little star, \n \t How I wonder what you are! \n \t \t Up above the world so high, \n \t \t Like a diamond in the sky. \n Twinkle, twinkle, little star, \n \t How I wonder what you are!")
# câu 2 
import platform
print("Phiên bản Python đang sử dụng là : ",platform.python_version())
# câu 3 
import datetime # Dùng thư viện ngày giờ của Python
now = datetime.datetime.now()
print ("Hôm nay là ngày : {ngay}, Và thời gian ngay lúc này là : {gio} ".format(ngay = now.strftime("%d-%m-%Y"),gio = now.strftime("%H:%M:%S")))
# câu 4 
from math import pi
r = float(input ("Nhập bán kính hình tròn : "))
Dientich = pi*r**2
print ("Diện tích hình tròn có bán kính :  " + str(r) + " là : " + str(Dientich))
# câu 5
ten = input("Nhập tên của bạn : ")
ho = input("Nhập họ của bạn : ")
print ("Hello  " + ten + " " + ho)
# câu 6
values = input("Nhập dãy số (cách nhau bằng dấu phẩy) : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
# câu 7 
filename = input("Nhập tên tệp của bạn vào : ")
f_extns = filename.split(".")
print ("Phần mở rộng của tệp là :  " + repr(f_extns[-1]))
# câu 8
values = input("Nhập màu (cách nhau bằng dấu phẩy) : ")
color_list = values.split(",")
print( "Màu đầu trong dãy là %s và màu cuối trong dãy là %s"%(color_list[0],color_list[-1]))
# câu 9
exam_st_date = (11,12,2014)
print( "Ngày thi sẽ bắt đầu từ : %i / %i / %i"%exam_st_date) 
# câu 10
a = int(input("Nhập số : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
kq = n1+n2+n3
print ("Kết quả của {} + {} + {} = {}".format(n1,n2,n3,kq))
# câu 11
print(abs.__doc__)
# câu 12
import calendar # dùng thư viện lịch
y = int(input("Nhập năm : "))
m = int(input("Nhập tháng : "))
print(calendar.month(y, m))
# câu 13
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")
