def gh():
    n=input("enter the string\n")
    new=''
    count=0
    for i in n:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            new=new+i.upper()
        else:
            new=new+i
    print(new)
gh()    
        
