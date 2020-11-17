print("Numbers:")
a = int(input())
b = int(input())
sum = 0
while b > 0:
  if b % 2 == 1:
    sum = sum + a 
  a = 2*a
  b = b // 2
print(sum)