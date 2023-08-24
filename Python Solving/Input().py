# Enter your code here. Read input from STDIN. Print output to STDOUT

x = input().split()
p = input()

p = p.replace("x",x[0])

print(eval(p)==int(x[1]))