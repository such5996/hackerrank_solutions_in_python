if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    l = len(arr)
    a = 0
    for i in range(0,l):
        for j in range(i+1, l):
            if(arr[i] < arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    for i in range(0, l-1):
        if(arr[i] == arr[i+1]):
            i = i+1
        else:
            a = arr[i+1]
            break
    print(a)
            
