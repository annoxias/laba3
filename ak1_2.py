n = int(input())
if 36 < n <= 54:
       if n % 2:
           print("боковое нижнее")
       else:
           print("боковое верхнее")
elif n % 2:
    print("купе нижнее")
else:
    print("купе верхнее")
