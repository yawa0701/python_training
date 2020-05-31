def ss(number_list,n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

numbers = range(0,100)
sl = ss(numbers,2)
print(sl)
s2 = ss(numbers,202)
print(s2)
