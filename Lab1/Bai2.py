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
