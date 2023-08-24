def mutate_string(string, position, character):
    stringArr = list(string)
    stringArr.insert(position,character)
    stringArr.pop(position+1)
    
    return "".join(stringArr)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)