
def main():
    s = input('Please enter desired string')
    a = reverseString(s)
    print('Reversed string will be: %s'%a)

def reverseString(s):
        if len(s)==0:
            return s
        else:
            return reverseString(s[1:]) + s[0]
main()

