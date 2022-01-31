if __name__ == "__main__":
    import math
    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))
    D = b*b-4*a*c
    if D < 0:
        print("Корней нет")
    elif D == 0:
        x1 = (-b/(2*a))
        print("Корень уравнения: "+x1)
    else:
        x1 = ((-1*b+math.sqrt(D))/(2*a))
        x2 = ((-1*b-math.sqrt(D))/(2*a))
        print("Первый корень: "+x1+"; Второй корень: "+x2)
