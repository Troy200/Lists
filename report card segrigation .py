import random

marks = []

U30 = []
U70 = []
U100 = []

for i in range(21):
    R = random.randint(0, 100)
    marks.append(R)


for i in marks:
    if i <= 30:
        U30.append(i)
    elif i <= 70:
        U70.append(i)
    elif i <= 100:
        U100.append(i)


print("These were all the grades:")
print(marks)
print("These are segregated the grades 1-30, 31-70, 71-100:")
print("1-30:", U30)
print("31-70:", U70)
print("71-100:", U100)
print("Thees are the amount of students in each category ")
print("1-30:",len(U30))
print("31-70:",len(U70))
print("71-100:",len(U100))
