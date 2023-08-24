if __name__ == '__main__':
    N = int(input())

arr = []

for _ in range(N):
    x = input().split(" ")
    
    if x[0] == "insert":
        arr.insert( int(x[1]),int(x[2]) )
    elif x[0] == "remove":
        arr.remove( int(x[1]) )
    elif x[0] == "append":
        arr.append( int(x[1]) )
    elif x[0] == "sort":
        arr.sort()
    elif x[0] == "pop":
        arr.pop()
    elif x[0] == "reverse":
        arr.reverse()
    elif x[0] == "print":
        print(arr)