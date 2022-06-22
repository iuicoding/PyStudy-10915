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