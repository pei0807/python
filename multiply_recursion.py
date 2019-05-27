### create recursion function to calculate a*b + c


def main():
    print(multiplicaiton(3,7))
    print(ab_c_plus(3,7,2))

def multiplicaiton(a,b):
    if b ==1:
        sum = a
        return sum

    sum = multiplicaiton(a,(b-1))
    sum = a+ sum

    return sum

def ab_c_plus(a,b,c):
    ans = multiplicaiton(a, b)
    ans = ans+c

    return ans

main()