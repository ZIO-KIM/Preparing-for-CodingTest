#그리디 알고리즘 예제 3-2 : 큰 수의 법칙 (p.92)
#수행 시간 측정 코드 추가

import time
start_time = time.time() # 측정 시작

print('배열의 크기 N, 숫자가 더해지는 횟수 M, 특정 수가 연속해서 더해질 수 있는 횟수 K를 입력하시오 :')
N, M, K = map(int, input().split()) # N,M,K를 공백으로 구분하여 입력받기
print('N개의 자연수를 입력하시오 :')
data = list(map(int, input().split())) # N개의 수를 공백으로 구분하여 입력받기

data.sort() # 입력받은 수들 정렬하기 (오름차순 정렬 됨)
first = data[N-1] # 첫번째로 큰 수
second = data[N-2] # 두번째로 큰 수

result = 0

while True :
    for i in range (K) :

        if M == 0 :
            break
        result += first
        M -= 1
    if M == 0 :
        break
    result += second
    M -= 1

print('큰 수의 법칙에 따른 결과는 :')
print(result)

end_time = time.time() # 측정 종료
print("time :", end_time - start_time) # 수행 시간 출력
