T = int(input("Enter No. of test cases = "))
h = int(input("Enter monster prsent health = "))
x = int(input("Enter monster decrese health = "))
y = int(input("Enter monster increse health = "))
for i in range(T):
    a = h+y
    b = a-x
    if b <= 0:
        print("1")
    elif b > x:
        print("0")
