def fact (x):
  if x==1:
    return 1
  else:
      return(x*fact(x-1))
    num=int(input("enter the number"))
    if num>=1:
        print ("factorial of",num,"is",fact(num))
