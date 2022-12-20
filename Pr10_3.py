import datetime

year=int(input("Enter year:"))

month=int(input("Enter month:"))

date=int(input("Enter Date:"))


today=datetime.date(year,month,date)
print(today)

format=datetime.date.strftime(today,"%m-%d-%Y")

print(format)