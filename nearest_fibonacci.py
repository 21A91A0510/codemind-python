def fib(n):
    if(n==0):
        print(0)
        return
    a=0
    b=1
    c=a+b
    while(c<=n):
        a=b
        b=c
        c=a+b
    if(abs(c-n)>abs(b-n)):
        print(b)
    elif(abs(c-n)==abs(b-n)):
        print(b,c)
    else:
        print(c)
n=int(input())
fib(n)
