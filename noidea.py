value = list(map(int,input().split()))
n = value[0]
m = value[1]
if( n>=1 and n<=pow(10,5) and m>=1 and m<=pow(10,5) ):
    arr = list(map(int,input().strip().split()))
    a = set(map(int,input().strip().split()))
    b = set(map(int,input().strip().split()))
    h = 0
    for i in arr:
        if(i in a):
            h = h+1
        if(i in b):
            h = h-1
    print(h)
