# 과제 11
ex1 = input("임의의 숫자 5개를 입력:").split()
char1 = input("임의의 문자 1개를 입력:")
ex1.append(char1)
print(ex1)

# 과제 12
ex2 = input("임의의 숫자 5개를 입력:").split()
del ex2[-2:]
print(ex2)

# 과제 13
ex3 = input("임의의 숫자 5개를 입력:").split()

for index, value in enumerate(ex3, start=101):
    print(index,value)

# 과제 14
a = [10, 20, 30, 40, 30, 20, 10]
result = a.count(20)
print(result)

# 과제 15
ex5 = input("임의의 숫자 10개를 입력:").split()
min_value = min(ex5)
max_value = max(ex5)
print(min_value, "and", max_value)

# 과제 16
ex6 = list(map(int, input("임의의 숫자 10개를 입력: ").split()))

min_val = min(ex6)
max_val = max(ex6)

ex6.remove(min_val)
ex6.remove(max_val)

total = sum(ex6)
print(total)

# 과제 17
a = [10, 20, 30, 40, 30, 20, 10]

while 20 in a:
    a.remove(20)

print(a)

# 과제 18
ex8 = [i for i in range(1, 6)]
print(ex8)

# 과제 19
ex9 = [i for i in range(1, 21) if i % 2 == 1]
print(ex9)

# 과제 20
a = int(input("첫 번째 정수 입력 (1~20):"))
b = int(input("두 번째 정수 입력 (10~30):"))

power = [2 ** i for i in range(a, b + 1)]

del power[1]      
del power[-2]     

print(power)

# 과제 21
text = input("Hello, world!를 입력:")  
new_text = text.replace("Hello", "Hi")
print(new_text)

# 과제 22
chars = input("임의의 4개의 문자 입력:").split()
result = '/'.join(chars)
print(result)

# 과제 23
name = input("성을 영어로 입력하세요:")
lower_name = name.lower()
ex13 = lower_name.rjust(10)
print(ex13)

# 과제 24
data = input("물품 가격들을 세미콜론(;)으로 구분해 입력하세요: ")
prices = list(map(int, data.split(";")))
prices.sort(reverse=True)

for price in prices:
    print(str(price).rjust(9))