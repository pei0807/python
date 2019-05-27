### determine if it is a prime number using recursivex
def main():
    ans= is_prime(20,2)
    print(ans)

def is_prime(a,b):

    if a == 2:
        return True

    elif a%b== 0:
        if a==b:
            return True
        else:
            return False

    prime = is_prime(a, b + 1)
    return prime

main()