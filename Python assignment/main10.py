a = int(input("Enter X"))
b = int(input("Enter Y"))
c = int(input("Enter Z"))
if a>b and a >c:
    print("X is greater than Y and is greater than Z")
elif b>c and b >a:
    print("Y is greater than X and is greater than Z")
else:
    print("Z is greater than X and is greater than Y")