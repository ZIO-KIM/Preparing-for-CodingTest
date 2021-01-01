#그리디 알고리즘 예제 3-1 (p.87)
#거스름돈 문제
#직접 푼 것
N = int(input()) #N은 손님에게 거슬러 줘야 할 돈
count = 0
count += N//500 #//은 몫 정수형 반환 (/은 실수형 반환)
N %= 500
count += N//100
N %= 100
count += N//50
N %= 50
count += N//10
N %= 10
print(count)
