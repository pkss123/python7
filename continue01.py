# continue명령은 실행시 돌고 있던 바퀴를 강제로 종료시키고
# 바로 다음 바퀴로 넘어가는 탈출구문입니다
# 전체 반복문의 종료 여부에는 영향을 미치지 않으며 오로지
# 돌고 있던 바퀴만 스킵하는 기능을 가지고 있습니다

score = [97, 46, 22, -1, 87]

for s in score:
    if (s == -1):
        continue
    print(s)
print("점수 처리 완료")
print()

for a in range(1,11):
    if not a % 2:
        continue
    print(a, end=" ")
print()