# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = set()

for i in range(n):
    country = input()
    arr.add(country)
print(len(arr))