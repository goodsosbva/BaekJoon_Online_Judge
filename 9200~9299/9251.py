
# 문제
# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
# 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
#
# 입력
# 첫째 줄과 둘째 줄에 두 문자열이 주어진다.
# 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
#
# 출력
# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

def LCS(str1, str2, str1_len, str2_len) :

    if str1_len == 0 or str2_len == 0 :
        return 0

    elif str1[str1_len - 1] == str2[str2_len - 1] :
        return 1 + LCS(str1, str2, str1_len - 1, str2_len - 1)

    else :
        return max(LCS(str1, str2, str1_len, str2_len - 1), LCS(str1, str2, str1_len - 1, str2_len))

str1 = input()
str2 = input()        

print(LCS(str1, str2, len(str1), len(str2)))
