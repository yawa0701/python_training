try:
    a=input("type a number:")
    b=input("type a another:")
    a=int(a)
    b=int(b)
    print(a/b)
except (ZeroDivisionError,ValueError):
    print("Invited input.")
