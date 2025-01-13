First = input ("Введите первое число")
Second = input("Введите второе число")
Third =input ("Введите третье число")
if First == Second == Third:
    print(3)
elif First == Second or First == Third or Second == Third:
    print(2)
else: print(0)
