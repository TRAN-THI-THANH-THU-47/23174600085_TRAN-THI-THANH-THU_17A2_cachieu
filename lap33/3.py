#a)
print("Các số nguyên tố từ 100 đến 1000 (kể cả số 1000 là : ")
for i in range(100, 1001):
  check = True
  for j in range(2, int(i**0.5) + 1):
    if i % j == 0:
      check = False
      break
  if check:
    print(i,end = " ") 
#b)
print("Các số chính phương từ 1 đến 1000 là:")
for i in range(1, 1001):
    if int(i ** 0.5) ** 2 == i:
        print(i)
#c)
a, b = 0 , 1
print("Chuỗi Fibonacci sao cho số cuối cùng nhỏ hơn 100 là:")
print(a, end=" ")
for i in range(0,100): 
    if b >= 100:
        break
    print(b, end=" ")
    a, b = b, a + b
#d)
print("Các số hoàn hảo nhỏ hơn 500 là : ")
sum = 1
for i in range(2, 500):
  for j in range(2, int(i ** 0.5) + 1):
    if i % j == 0:
      sum += j + i // j
  if sum == i:
    print(i)
  sum = 1
  #e)
print("Tổng của các số ngũ giác trong đoạn từ 1 đến 200 (kể cả số 200) là :")
sum = 0
for n in range(1,201,1):
    sum = sum + (n * (3*n-1)) / 2
print(sum)
