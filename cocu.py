
Classroom
Python Programming Essentials Training
November 27-December 8, 2023
Home
Calendar
Enrolled
To-do
Day 3 Act 2
#Ill update this as soon as Im free


""""IT_years_service = int(input("Enter years of service in I.T.:"))
Accounting_years_service = int(input("Enter years of service in accountinh:"))
HR_years_service = int(input("Enter years in service in Human Resource"))"""

#Not done yet, dont have a time
#IT Department

IT_incentive_10_years = 10000
IT_incentive_5_years = 5000

#Accounting Department

Accounting_incentive_10_years = 12000
Accounting_incentive_5_years = 6000

#HR Department

HR_incentive_10_years = 13000
HR_incentive_5_years = 7000

#Check if IT Department is eligible for incentives
if IT_years_service >= 10:
  IT_incentive = IT_incentive_10_years
elif IT_years_service >= 5:
  IT_incentive = IT_incentive_5_years
else:
  IT_incentive = 0

#Check if Accounting Department is eligible for incentives
if Accounting_years_service >= 10:
  Accounting_incentive = Accounting_incentive_10_years
elif Accounting_years_service >= 5:
  Accounting_incentive = Accounting_incentive_5_years
else:
  Accounting_incentive = 0

#Check if HR Department is eligible for incentives
if HR_years_service >= 10:
  HR_incentive = HR_incentive_10_years
elif HR_years_service >= 5:
  HR_incentive = HR_incentive_5_years
else:
  HR_incentive = 0

#Print the incentives for each department
print("IT Department Incentive:", IT_incentive)
print("Accounting Department Incentive:", Accounting_incentive)
print("HR Department Incentive:", HR_incentive)

#Identify which Department are eligible to have incentives
if IT_incentive > 0:
  print("IT Department is eligible for incentives")
if Accounting_incentive > 0:
  print("Accounting Department is eligible for incentives")
if HR_incentive > 0:
  print("HR Department is eligible for incentives")
Ituralde_Darrel_day3_act2.py
