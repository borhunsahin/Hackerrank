if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr = list(arr)
first_point = max(arr)

while(first_point == max(arr)):
    arr.remove(max(arr))
    
print(max(arr))