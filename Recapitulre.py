def myfunc():
    return 10

i = myfunc()
print(i)

def numar_ales():
    try:
        num = float(input("Enter a number :"))
    except ValueError:
        print('Nu ati ales un numar valid')
    else:
        if num> 0:
            print("Pozitive number")
        elif num == 0:
            print("Zero")
        else:
            print("Negative number")
    finally:
        print("Sfarsitul functiei")