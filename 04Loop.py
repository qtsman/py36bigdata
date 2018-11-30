# 반복문
# 특정 문장/코드를 지정한 횟수/조건에 의해 반복 실행

# # 어떤 문장을 한번 출력하고 싶다면?
# print('선생님~ 사랑해요')
#
# # 어떤 문장을 여러번 출력하고 싶다면?
# print('선생님~ 사랑해요')
# print('선생님~ 사랑해요')
# print('선생님~ 사랑해요')

# 그런데, 문장을 수정해야 한다면?
# print('선생님~ 미워요!')
# print('선생님~ 미워요!')
# print('선생님~ 미워요!')

# 반복문을 사용한다면?
# 반복 용이성과 수정 편리성 지원
# for i in range(1, 3+1):
# for i in [1, 2, 3]:
#     print('선생님~ 미워요!', i)

# 반복처리 : for
# for 변수 in range(시작, 끝-1, 증가):
#     반복할 문장/코드
# for 변수 in range(시작, 끝-1, 증가):
#     반복할 문장/코드      (변수사용하지 않을때는)


# ex1) 1 ~ 10 까지 정수 출력
# for i in range(1, 11):
#     #print(i) # 자동 줄바꿈이됨
#     print(i, end=',')  # 줄바꿈 없이 출력
# print()
# # ex2) 1 ~ 50 사이 짝수 출력
# for i in range(1, 50+1):
#     if i%2==0:
#         print(i, end=' ')
# print()
# # ex3) 1 ~ 50 사이 홀수 출력
# for i in range(1, 50+1):
#     if i%2==1:
#         print(i, end=' ')
# print()
# # ex4) 1 ~ 100 까지 총합을 구하세요
# sum = 0
# for i in range(1, 101):
#     #sum=sum+i
#     sum += i
# print(sum)
# print()
# # ex5) 1 ~ 100 까지 홀수의 총합을 구하세요
# sum = 0
# for i in range(1, 100+1):
#     if i%2==1:
#         sum +=i
# print(sum)
# print()
# # ex6) 1 ~ 100 까지 5의 배수의 총합을 구하세요
# sum = 0
# for i in range(1, 100+1):
#     if i%5==0:
#         sum +=i
# print(sum)
# print()
#
# # ex7) 구구단 중 특정 단을 입력받아 출력
# dan = int(input('출력할 단? :'))
# fmt = '%d x %d = %d'
# for i in range(1,9+1):
#     print(fmt % (dan,i ,dan*i))

# ex8) 구구단 중 2단 ~ 9단 출력
# 중첩 for문 사용

# while 문 : 특정조건을 만족하면 반복 실행
# 변수 = 초기값
# while 조건식:
#     반복할문장
#     변수증가

# i = 1
# while (i <= 3):
#     print('선생님~ 미워용!!')
#     #i=i+1
#     i += 1
#
# # ex9) 1 ~ 50 사이 짝수 출력
# i = 1
# while (i <= 50):
#     if i%2==0:
#         print(i, end=' ')
#     i +=1
# print()
# # ex10) 1 ~ 50 사이 홀수 출력
# i = 1
# while (i <= 50):
#     if i%1==0:
#         print(i, end=' ')
#     i +=1
# print()
#
# # ex11) 1 ~ 100까지 총합을 구하세요
# sum = 0
# i = 1
# while (i <= 100):
#     sum = sum + i
#     i += 1
# print(sum)
#
# # ex12) 1 ~ 100까지 5의 배수의 총합을 구하세요
# sum = 0
# i = 1
# while (i <= 100):
#     if i%5==0:
#         sum = sum + i
#     i += 1
# print(sum)
#
# # 무한 반복
# # while문의 조건식에 True 라고 기입하면 반복을 무한대로 실행하는 반복문 생성
# while True:
#     print('선생님~ 미워요!!!')
#
#
# # 반복문 실행 중단 : break
# # 계속 반복하는 코드를 실행중단 하고자 할 때 사용
#
# # ex13) 1 ~ 무한대 범위까지의 합을 구하세요 단, 총합이 20181128보다 크면 반복을 자동중단 한다
# sum = 0
# i = 1
# while (i <= 1000):
#     sum = sum + i
#     if sum>20181128:
#         break
# print(sum)


# Q20 복권발행 문제
# bok = int(input('복권발행번호(3자리) 입력하숑!!'))
#
# from random import *
# ran = randint(1,9),randint(1,9),randint(1,9)
#

# Q22 숫자맞추기 II
# for _ in range(100):
#     num1 = int(input('숫자를 맞춰보자!!(1~100) :'))
#
#     from random import *
#     num2 = randint(1,100)
#
#     if num1 > num2:
#         print('추측한 숫자가 큽니다 다시!')
#         print(num2)
#     elif num1 < num2:
#         print('추측한 숫자가 작습니다 다시!')
#         print(num2)
#     elif num1 == num2:
#         print('빙고 숫자를 맞췄습니다.')
#         print(num2)
#         break


# Q30 구구단 테이블
print('\t\t\tMultiplication Table')
for k in range(1,10):
    print('  ',k, end=' ')
print()
print('----------------------------------------')
i=1

while i <= 9:
    print(i,' |', end='\t')
    j = 1
    while j <= 9:
        gugu = i*j
        print(gugu, end='\t')
        j += 1
    i+= 1
    print()



# Q32 주민번호 유효성 검사


















