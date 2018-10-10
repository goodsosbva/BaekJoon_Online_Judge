
# 문제
# 개미 N마리가 막대 위에 올라가 있다.
# 일부 개미는 왼쪽을 바라보고 있고, 나머지 개미는 오른쪽을 바라보고 있다.
# 모든 개미는 매우 작아서 크기가 없는 점으로 나타낼 수 있다.
# 시작 신호가 주어지면, 개미는 바라보고 있는 방향으로 행진을 시작한다.
# 모든 개미는 동일한 속도 초속 1mm로 이동한다.
# 두 개미가 한 점에서 충돌하는 경우가 발생할 수 있다.
# 이 경우에 두 개미는 행진하는 방향을 반대 방향으로 바꾸고, 행진을 계속하게 된다.
# 개미가 방향을 바꾸는데 걸리는 시간은 없다.
# 개미가 막대의 끝에 도착하는 경우에는, 막대에서 떨어지게 된다.
# 막대는 땅 위에 떠있다고 가정한다. 처음에 모든 개미의 위치는 서로 다르다.
# 즉, 두 개미가 막대 위의 한 점에 같이 있는 경우는 없다.
# 개미는 부호 있는 정수로 나타낼 수 있다. 이 정수를 개미의 ID라고 한다.
# 개미의 ID의 부호는 개미가 처음에 바라보고 있는 방향이다.
# -는 왼쪽을 바라보고 있는 것이고, +는 오른쪽을 바라보고 있는 것이다.
# 개미의 ID의 절대값은 1부터 109까지의 정수 중 하나이다.
# 또, 모든 개미의 ID의 절대값은 서로 다르다. 아래 그림에는 개미가 총 6마리가 있고,
# ID는 {+4, +5, -1, -3, -2, +6}이다. 각 개미의 초기 위치는 {5, 8, 19, 22, 24, 25}이며,
# 막대의 길이 L = 30이다. 화살표는 처음에 개미가 바라보고 있는 방향을 나타낸다.
# 왼쪽 끝의 좌표는 0이고, 오른쪽 끝의 좌표는 30이다. ID가 +6인 개미는 시간 t = 5일 때,
# 막대의 오른쪽 끝에 도착하며, t = 6에 막대에서 떨어지게 된다.
# 개미가 행진을 시작하기 전의 상태 (ID와 막대 상의 위치)가 주어진다.
# 두 개미가 동시에 막대의 양 끝에서 떨어지는 경우에는,
# ID가 작은 개미가 조금 더 먼저 떨어진다고 한다.
# 아래 그림은 이와 같은 경우를 나타낸 그림이다.
# 두 개미 {-1, +2}는 끝에 동시에 도착하게 된다.
# -1 < +2 이기 때문에, ID가 -1인 개미가 +2인 개미보다 조금 더 먼저 떨어지게 된다.
# 따라서, 아래 그림의 네 개미가 떨어지는 순서는 {-1, 2, 4, 3}이 된다.
# 양의 정수 1 ≤ k ≤ n이 주어졌을 때, k번째로 떨어지는 개미를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스의 첫째 줄에는 N, L, k가 주어진다.
# 다음 N개 줄에는 pi와 ai가 주어진다.
# ai는 개미의 ID이고, pi는 그 개미의 초기 위치이다.
# 항상 pi가 증가하는 순서로 (pi < pi+1) 주어진다.
# (1 ≤ pi ≤ L-1, 3 ≤ N ≤ 100,000, 10 ≤ L ≤ 5,000,000, 1 ≤ k ≤ N)
#
# 출력
# 각 테스트 케이스마다, N마리 개미 중에서 k번째로 떨어지는 개미의 ID를 출력한다.
# 개미의 ID가 양수인 경우에 +를 출력하면 안된다.

import sys

def solution(L, K, ants) :
    drop_left, drop_right = [], []

    for ant in ants :
        if ant[1] < 0 :
            drop_left.append((ant[0], ant[1]))

        else :
            drop_right.append((L - ant[0], ant[1]))

    drops = list(zip(drop_left + drop_right, ants))
    drops = sorted(sorted(drops, key = lambda drop: drop[1][1]),
                   key = lambda drop: drop[0][0])

    return drops[K - 1][1][1]

T = int(sys.stdin.readline().strip())

for _ in range(T) :
    N, L, K = list(map(int, sys.stdin.readline().strip().split()))

    ants = []

    for _ in range(N) :
        p, a = list(map(int, sys.stdin.readline().strip().split()))
        ants.append((p, a))

    print(solution(L, K, ants))
