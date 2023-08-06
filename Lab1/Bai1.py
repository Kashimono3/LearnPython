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
# câu 14
from datetime import date
print("Nhập theo Năm Tháng Ngày")
ngaydau =input("Nhập chuỗi ngày đầu : (cách nhau bằng dấu phẩy)")
chuoi = ngaydau.split(",")
ngaysau = input("Nhập chuỗi ngày sau : (cách nhau bằng dấu phẩy)")
chuoisau = ngaysau.split(",")
f_date = date(int(chuoi[0]),int( chuoi[1]), int(chuoi[2]))
l_date = date(int(chuoisau[0]),int( chuoisau[1]), int(chuoisau[2]))
delta = l_date - f_date
print("Số ngày cách nhau là : ",delta.days)
# câu 15
pi = 3.14
r = float(input("Nhập bán kính : "))
V= 4.0/3.0* pi * r**3
print('Thể tích của hình cầu là  ',V)
# câu 16
def sosanh(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 
    
nhap = int(input("Nhập số cần so sánh với 17 : "))
print(sosanh(nhap))
# câu 17
def phamvi(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
So = int( input("Nhập số cần kiểm tra : "))
if (phamvi(So) == True):
      print("Số bạn nhập có nằm trong khoảng 100 của phạm vi 1000 hoặc 2000")
else:
      print("Số bạn nhập không nằm trong khoảng 100 của phạm vi 1000 hoặc 2000")
# câu 18
def Tong(x, y, z):
     sum = x + y + z 
     if x == y == z:
      sum = sum * 3
     return sum
a = input("Nhập 3 số cần tính , cách nhau bằng dấu phấy : ")
lista = a.split(",")
print("Kết quả là : ",Tong(int(lista[0]),int(lista[1]),int(lista[2])))
# câu 19
def ChuoiMoi(text):
  if len(text) >= 2 and text [:2] == "Is":
    return text
  return "Is" + text
chuoi = input("Nhập tên : ")
print(ChuoiMoi(chuoi))
# câu 20
def lap(text, n):
   result = ""
   for i in range(n):
      result = result + text
   return result
chuoi = input("Nhập chuỗi cần lặp : ")
so  = int(input("Nhập số lần cần lặp: "))
print("Chuỗi mới : ",lap(chuoi, so))
# câu 21 
so = int(input("Nhập số : "))
kiemtra = so % 2
if kiemtra > 0:
    print("Số {0} là số lẻ ".format(so))
else:
    print("Số {0} là số chẵn ".format(so))
# câu 22
def List_check(nums,numcheck):
  count = 0  
  for num in nums:
    if num == numcheck:
      count = count + 1

  return count
sophantu = int(input("Nhập số phần tử của list : "))
chuoiso = []
for i in range(sophantu):
   val = int(input('Nhập giá trị: '))
   chuoiso.append(val)
socancheck = int(input("Nhập số cần kiểm tra : "))
print("Số lần sô cần kiểm tra xuất hiện trong chuỗi là : ",List_check(chuoiso,socancheck))
# câu 23
def copy(text, n):
  flen = 2
  if flen > len(text):
    flen = len(text)
  substr = text[:flen]
  result = ""
  for i in range(n):
    result = result + substr
  return result
text = input("Nhập chuỗi : ")
num = int(input("Nhập số : "))
print(copy(text, num))
# câu 24
def is_vowel(str,char):
    all_vowels = str
    return char in all_vowels

text = input("Nhập chuỗi : ")
kytu = input("Nhập từ : ")
is_vowel(text,kytu)
if (is_vowel(text, kytu) == True):
      print("Từ {0} có nằm trong chuỗi  {1}".format(kytu,text))
else:
       print("Từ {0} không nằm trong chuỗi  {1}".format(kytu,text))

# câu 25
def check(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False

sophantu = int(input("Nhập số phần tử của list : "))
chuoiso = []
for i in range(sophantu):
   val = int(input('Nhập giá trị: '))
   chuoiso.append(val)
socancheck = int(input("Nhập số cần kiểm tra : "))

check(chuoiso, socancheck)
if (check(chuoiso, socancheck) == True):
      print("Số {0} có nằm trong chuỗi số {1}".format(socancheck,chuoiso))
else:
       print("Số {0} không nằm trong chuỗi số {1}".format(socancheck,chuoiso))