# câu 1 
# a
def tinhtong (a,b):
   c =  a+b
   return c
try: 
 so1 = int(input("Nhập a : "))
 so2 = int(input("Nhập b : "))
 print("Tổng của {0} và {1} là :{2}".format(so1,so2,tinhtong(so1,so2)))    
except:
  print("Vui lòng nhập số !")
# b 
def tinhthuong (a,b):
   c =  a/b
   return c
try: 
 so1 = int(input("Nhập a : "))
 so2 = int(input("Nhập b : "))
 print("Thương của {0} và {1} là :{2}".format(so1,so2,tinhthuong(so1,so2)))    
except:
  print("Vui lòng nhập số !") 
#c 
def tinhluythua (a,b):
   c =  pow(a,b)
   return c
try: 
 so1 = int(input("Nhập a : "))
 so2 = int(input("Nhập b : "))
 print("kết quả của {0} mũ {1} là :{2}".format(so1,so2,tinhluythua (so1,so2))) 
except:
 print("Vui lòng nhập số !")   
# câu 2 
def Tinhdientich (a,b):
   s =  a*b
   return s
chieudai = int(input("Nhập chiều dài : "))
chieurong = int(input("Nhập chiều rộng : "))
print("Diện tích hình chữ nhật có chiều dài {0} và chiều rộng {1} là : {2}".format(chieudai,chieurong,Tinhdientich(chieurong,chieudai)))  
# câu 3 
import math
def kiem_tra_so_nguyen_to(n):
   if n == 1:
       return False         
   for i in range(2, int(math.sqrt(n))+1):
       if n % i == 0:
           return False
   return True
def liet_ke_so_nguyen_to(a, b):
   for i in range(a, b + 1):
       if kiem_tra_so_nguyen_to(i):
           print(i, end=' ')
try:
   a = int(input("Nhập số đầu tiên : "))
   b = int(input("Nhập số cuối cùng : "))
   if a < 0 or b < 0:
       print("Vui lòng nhập số tự nhiên ")
   elif a > b:
       print("Số cuối cùng phải lớn hơn số đầu tiên")
   else:
       print("Dãy số nguyên tố là : ",liet_ke_so_nguyen_to(a, b))
except:
   print("Vui lòng nhập số !")
# câu 4 
def is_fibonacci(n):
  if n == 0 or n == 1:
    return True
  for i in range(2, n):
    if n % i == 0:
      return False
  return True
  
try: 
 a = int(input("Nhập n : "))
 if is_fibonacci == True:
   print("Số {0} là số Fibonacci".format(a))
 else:
   print("Số {0} là không phải số Fibonacci".format(a))
except:
  print("Vui lòng nhập số!")
# câu 5 
def fibonacci1(i):
  if i == 0:
    return 0
  elif i == 1 :
    return 1
  else: 
    return fibonacci(i-1) + fibonacci(i-2)
  
def fibonacci2(i):
  a, b = 0, 1
  for i in range(i):
    a, b = b, a + b
  return a

try:
 a = int(input("Nhập n : "))  
 print("Số Fibonacci thứ {0} là : {1} (Dùng đệ quy)".format(a,fibonacci1(a)))
 print("Số Fibonacci thứ {0} là : {1} (Không dùng đệ quy) ".format(a,fibonacci2(a)))
except: 
  print("Vui lòng nhập số")
# câu 6 

# câu 7 
import math
def TongCanBac2(n):
    sum = 0
    for i in range(1, n + 1):
     sum += math.sqrt(i)
    return sum
try:
   a = int(input("Nhập n : "))
   print("Tổng căn bậc 2 của {0} là {1}".format(a,TongCanBac2(a)))
except:
   print("Vui lòng nhập số!")    
# câu 8   
import math
def TinhNghiemPhuongTrinhBac2(a, b, c):
  if a == 0:
    if b == 0:
      print("Rỗng")
    else:
      return [-c / b]

  discriminant = b**2 - 4 * a * c
  if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Nghiệm của phương trình bao gồm : {0} và {1} ".format(x1,x2))
  elif discriminant == 0:
    x = -b / (2 * a)
    print("Nghiệm là : ",x)
  else:
   print("Rỗng")
    
try:
  print("Chương trình giải phương trình bậc 2 có dạng ax2 + bx +c = 0")
  a=int(input("Nhập a :"))
  b=int(input("Nhập b :"))
  c=int(input("Nhập c :"))
  TinhNghiemPhuongTrinhBac2(a,b,c)
except:
  print("Vui lòng nhập số!")
# câu 9
def GiaiThua(n):
  if n == 0:
    return 1
  else:
    return n * GiaiThua(n - 1)
try:
  a = int(input("Nhập số cần tính giai thừa : "))
  print("Kết quả của {0}! là : {1}".format(a,GiaiThua(a)))
except :
  print("vui lòng nhập số!")
# Câu 10
# Câu 11
def DoiGioPhutGiay(seconds):
  hours = seconds // 3600
  minutes = (seconds % 3600) // 60
  seconds %= 60
  return hours, minutes, seconds

try:
  seconds = int(input("Nhập số giây:  "))
  hours, minutes, seconds = DoiGioPhutGiay(seconds)
  print("Thời gian được quy đổi : {}:{}:{}".format(hours, minutes, seconds))
except:
  print("Vui lòng nhập số!")
# Câu 12 
import random
def TaoMangRandom(n):
    random_numbers = [random.randint(1, 100) for i in range(n)]
    return random_numbers
def TaoMangNhapTay(n):
    chuoi =[]
    for i in range(n):
     number = int(input("Nhập số thứ {0}: ".format(i+1)))
     chuoi.append(number)
    return chuoi
# 12.a
def XuatSoLeKhongChiaHetCho5(numbers):
  odd_numbers = [number for number in numbers if number % 2 == 1]
  return [number for number in odd_numbers if number % 5 != 0]
try: 
 a = int(input("Nhập n : "))
 chuoi = TaoMangRanDom(a)
 print(chuoi)
 print(XuatSoLeKhongChiaHetCho5(chuoi))
except:
  print("Vui lòng nhập số!")
# 12.b
def is_fibonacci(n):
   a, b = 0, 1
   while a <= n:
    if a == n:
      return True
    a, b = b, a + b
   return False
def XuatSoFibonacci(numbers):
  fibonacci_numbers = []
  for number in numbers:
    if is_fibonacci(number):
      fibonacci_numbers.append(number)
  return fibonacci_numbers  
try: 
 a = int(input("Nhập n : "))
 chuoi = TaoMangRanDom(a)
 print(chuoi)
 kq = XuatSoFibonacci(chuoi)
 print(kq)
except:
  print("Vui lòng nhập số!")
#12.c
def TimSoNguyenToLonNhat(array):
  largest_prime = array[0]
  for number in array:
    if KiemTraSoNguyenTo(number):
      largest_prime = number
  return largest_prime

def KiemTraSoNguyenTo(number):
  if number <= 1:
    return False
  for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
      return False
  return True

chuoi = TaoMangRandom(5)
print(chuoi)
a = TimSoNguyenToLonNhat(chuoi)
print(a)
#12.d
def TimSoFibonacciBeNhat(array):
  SoFiBeNhat = float("inf")
  for number in array:
    if is_fibonacci(number):
      SoFiBeNhat = min(SoFiBeNhat, number)
  return SoFiBeNhat
try: 
 a = int(input("Nhập n : "))
 chuoi = TaoMangRanDom(a)
 print(chuoi)
 kq = TimSoFibonacciBeNhat(chuoi)
 print(kq)
except:
  print("Vui lòng nhập số!")
#12.e
def TrungBinhCongSoLe(array):
  total = 0
  count = 0
  for number in array:
    if number % 2 != 0:
      total += number
      count += 1
  return total / count
#12.f
def TinhTichSoLeKhongChiaHetCho3(array): 
  kq = 1
  for number in array:
    if number % 2 != 0 and number % 3 != 0:
      kq *= number
  return kq
#12.g
def DoiCho(list, position1, position2):
  temp = list[position1]
  list[position1] = list[position2]
  list[position2] = temp
  return list
try :
  a  = int(input("Nhập vị trí đổi đầu : "))
  b = int(input("Nhập vị trí đổi cuối"))
  c = int(input("Số phần tử tạo mảng random"))
  chuoi = TaoMangRandom(c)
  print(chuoi)
  print(DoiCho(chuoi,a,b))
except:
  print("Vui lòng nhập số!")
#12.h
def DaoNguocTratTu(list):
  reversed_list = []
  for i in range(len(list) - 1, -1, -1):
    reversed_list.append(list[i])
  return reversed_list
#12.i

#12.j
def Tong(list):
  sum = 0
  for number in list:
    sum += number
  return sum
#12.k
def DemSoLanXuatHien(list, number):
  count = 0
  for element in list:
    if element == number:
      count += 1
  return count
#12.l
def DemSoLanLapLaiCua1So(list, n):
  occurrences = {}
  for number in list:
    if number in occurrences:
      occurrences[number] += 1
    else:
      occurrences[number] = 1

  numbers_with_n_occurrences = [number for number, occurrence in occurrences.items() if occurrence == n]

  print(numbers_with_n_occurrences)
#12.m
def SoLapLaiNhieuNhat(list):
  occurrences = {}
  for number in list:
    if number in occurrences:
      occurrences[number] += 1
    else:
      occurrences[number] = 1

  most_frequent_number = max(occurrences.values())
  most_frequent_numbers = [number for number, occurrence in occurrences.items() if occurrence == most_frequent_number]

  print(most_frequent_numbers)