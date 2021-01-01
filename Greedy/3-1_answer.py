#그리디 알고리즘 예제 3-1 (p.87)
#거스름돈 문제
#교재 코드 참조
N = int(input())
count = 0

#큰 단위의 화폐부터 차례대로 확인
coin_types = [500,100,50,10]
for coin in coin_types :
    count += N // coin
    N %= coin

print(count)
