sum = 0
for i in range(1, 11):
    print(i,"번째 입력을 받습니다")
    num = int(input("짝수를 입력해주시면 총합에 반영됩니다"))
    if num % 2 == 0:
        sum += num
print("총합 : ",sum)
