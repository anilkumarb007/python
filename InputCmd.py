import sys

args = sys.argv

print("Size of agrs", len(args))

print("Name ==> ", args[1], "Age ==> ", args[2])
"""
python InputCmd.py Anil         20
        argv[0]    argv[1]     argv[2]
"""


employee_salary = input("Enter expected salary")
employee_hike = input("Enter hike value")
print((int(employee_salary) * int(employee_hike))/100)