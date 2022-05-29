def dd():
    n=input("enter the string\n")
    a=input("enter the char you want search\n")
    count=0
    for i in n:
        if i==a:
            count=count+1
    print(count)
dd()    
