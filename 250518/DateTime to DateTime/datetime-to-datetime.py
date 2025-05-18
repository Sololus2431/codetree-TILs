a, b, c = map(int, input().split())

# Please write your code here.
result = a*1440+ b*60 +c - 11*1501
if(result < 0):
    print(-1)
else:
    print(result)