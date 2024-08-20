"""numbers = 10
increment = 1
while increment <= numbers:
    print(increment)
    increment += 1
else:
    print("checking code is executing or not")
"""
'''
incrementTill = 20
incrementBy = 1
forTable = int(input("Enter table number"))
while incrementBy <= incrementTill:
    print(forTable,' * ',incrementBy,' = ',(forTable * incrementBy))
    incrementBy = incrementBy + 1
else:
    print(f"Completed printing the table {forTable}")
'''

# [18,12,15,5,20,10,87,12]
"""for value in range(1, 10, 2):
    print(value+1)
"""
"""attendance = [18,12,15,5,20,10,87,12]
day = 1
for element in attendance:
    print("Day ",day, 'attendance count is :',element)
    day = day + 1
"""

"""
value = 1
status = True 
while status:
    print(value) 
    if value>5:
        break
    value+=1 
    """
    
'''#continue statement
incrementTill = 20
incrementBy = 1
forTable = int(input("Enter table number"))
while incrementBy <= incrementTill:
    print()
    if incrementBy == 5:
        incrementBy = incrementBy + 1
        continue
    print(forTable,' * ',incrementBy,' = ',(forTable * incrementBy))
    incrementBy = incrementBy + 1'''
    
incrementTill = 20
incrementBy = 1
forTable = int(input("Enter table number"))
while incrementBy <= incrementTill:
    if incrementBy == 5:
        pass    
    else:
        print("incrementBy value is :", incrementBy)
    incrementBy = incrementBy+1
    

