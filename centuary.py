year=int(input("enter the year:"))
if(year<=0):
    print("0 and there is no negative centuries")
elif(year<=100):
    print("1 st centuary")
elif(year%100==0):
    print(year/100,"centuary")
else:
    print(year/100+1,"centuary")