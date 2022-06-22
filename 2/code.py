score = float(input(">기말 준비 정도는?"))
if score == 5:
    print("완벽")
elif 4 <= score:
     print("이게 다 한거야?")
elif 3 <= score:
     print("아직 아니야")
elif 2 <= score:
     print("정신 차려")
elif 1 <= score:
     print("사람이야?")
else:
     print("9등급 인생 포기해")




#6교시 수업내용
alist = [1,2,3,4,5]

print(alist)

if 4 in list:
     print("O")
if 144 not in alist:
     print("X")

print(alist[1])

alist = alist + [1]
alist = alist * 2
alist.append(8)
print(alist)

del alist[0]
alist.remove(2)
alist.pop(4)
print(alist)

print(alist + [2])
print(alist * 3)

for element in a:
     print(element)

