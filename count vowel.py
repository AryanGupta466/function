def dd():
    n=input('enter the string\n').lower()
    count=0
    for i in n:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            count=count+1
    print(count)
dd()    
