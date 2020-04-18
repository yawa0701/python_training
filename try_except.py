a=input("type a number:")
b=input("type a another:")
a=int(a)
b=int(b)
try:
    print(a/b)
except ZeroDivisionError:
    print("b cannot be zero.")
