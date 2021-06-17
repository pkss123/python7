# 탈출문이란 제어문을 종료시키거나 건너뛰기 위해 사용하는 구문으로
# break, continue문이 있습니다
# break문은 실행 즉시 돌던 반복문을 완전히 종료시킵니다
# 보통 반복문을 더 돌릴 필요가 없어졌을때 실행시키며
# 이를 위해 if문과 조합해서 사용하는 경우가 많습니다
score = [92, 56, 33, 127, 99]

for s in score:
    if (s < 0 or s > 100):
        break
    print(s)
print("점수 처리 완료")
print()

for a in range(1, 11):
    print(a, end=" ")
    if a == 6:
        break
print("\n 반복문 종료")