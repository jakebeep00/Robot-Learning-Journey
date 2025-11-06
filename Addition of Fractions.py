import math

def solution(numer1, denom1, numer2, denom2):
    num = (numer1*denom2) + (numer2*denom1)
    den = (denom1*denom2)
    gcd = math.gcd(num,den) #최대공약수를 구하는 방식
    
    fin_num = num / gcd
    fin_den = den / gcd
    
    
    return [fin_num,fin_den]

print(solution(1,2,3,4))