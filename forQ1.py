sum=0
n=int(input('배수를 입력해주세요'))
for number in range(0, 1001, n):
    sum+= number
print("총합은",sum,"입니다")