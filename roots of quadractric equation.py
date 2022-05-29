def dd():
    b=int(input('enter the num1\n'))
    a=int(input('enter the num2\n'))
    c=int(input('enter the num3\n'))
    d=b*b-4*a*c
    print(d)
    if d>0:
        print("both roots are reall")
    elif d<0:
        print("equation has complex roots")
    else:
        print("equation has one reall roots")
dd()        
