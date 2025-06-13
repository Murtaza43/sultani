#Date
#1
from datetime import datetime, timedelta
today = datetime.now()
five_days_ago = today - timedelta(days=5)
print("Today:", today)
print("5 days ago:", five_days_ago)
#2
from datetime import date, timedelta
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
#3
from datetime import datetime
now = datetime.now()
no_microseconds = now.replace(microsecond=0)
print("With microseconds:", now)
print("Without microseconds:", no_microseconds)
#4
from datetime import datetime
date1 = datetime(2025, 6, 13, 12, 0, 0)
date2 = datetime(2025, 6, 12, 10, 0, 0)
difference = date1 - date2
seconds = difference.total_seconds()
print("Difference in seconds:", seconds)
#Generators
#1
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2
for num in square_generator(5):
    print(num, end=" ")
#2
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
n = int(input("Enter a number: "))
evens = list(even_generator(n))
print(", ".join(map(str, evens)))
#3
def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
for num in div_by_3_and_4(50):
    print(num, end=" ")
#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
for val in squares(3, 7):
    print(val)
#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
for num in countdown(5):
    print(num, end=" ")
#math
#1
import math
degree = 15
radian = math.radians(degree)
print("Input degree:", degree)
print("Output radian:", round(radian, 6))
#2
height = 5
base1 = 5
base2 = 6
area = 0.5 * (base1 + base2) * height
print("Expected Output:", area)
#3
import math
num_sides = 4
side_length = 25
area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
print("The area of the polygon is:", round(area, 2))
#4
base = 5
height = 6
area = base * height
print("Expected Output:", float(area))