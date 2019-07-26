
d1 = int(input("enter the first date of the month:"))  
d2 = int(input("enter the second date of the same month :"))   
if d1 == d2:
    print("Invalid date")
elif  d1 == 32:
    print("Invalid date")
elif  d2 == 32:
    print("Invalid date")
else:
    res = d2-d1
    print("the differnce between the days are: ", res)
