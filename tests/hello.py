import sys;

print("hello")

a,b=0,1
while a<10:
    print(a)
    a,b=b,a+b

if a>10:
    print("a > 10 ,a=",a)
elif a>13:
    print("a>12,a=",a)
else :
    print("b=",b)

print("range(10)")

for i in range(10):
    print(i)

print("range(5,10)")

for i in range(5,10):
    print(i)


def f(ham: 42, eggs: int = 'spam') -> "Nothing to see here":
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)


f('wonderful')