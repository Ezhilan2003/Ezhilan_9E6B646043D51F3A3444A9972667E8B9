year=int(input("Enter the year:"))
if((year%100==0)or( year%400==0)):
    print(year,"is a leap year")
if(year%4==0):
    print(year,"is not a leap year")
        
