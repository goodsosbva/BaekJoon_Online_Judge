
# 문제
# 상근이는 2863번에서 표를 너무 열심히 돌린 나머지 5와 6을 헷갈리기 시작했다.
# 상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 
# 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.
# 두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다. 
# 이때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 
# 최솟값과 최댓값을 구해 출력하는 프로그램을 작성하시오.
# 
# 입력
# 첫째 줄에 두 정수 A와 B가 주어진다. (1 <= A,B <= 1,000,000)
# 
# 출력
# 첫째 줄에 상근이가 구할 수 있는 두 수의 합 중 최솟값과 최댓값을 출력한다.

arr = list(input().split())
print(sum(map(lambda x: int(x.replace('6', '5')), arr)),
       sum(map(lambda x: int(x.replace('5', '6')), arr)))