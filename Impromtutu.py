#product to add, multiply and average 5 numbers from user
num1 = float(input("Enter num1"))
num2 = float(input("Enter num2"))
num3 = float(input("Enter num3"))
num4 = float(input("Enter num4"))
num5 = float(input("Enter num5"))

add = num1+num2+num3+num4+num5
mul = num1*num2*num3*num4*num5
ave = (num1+num2+num3+num4+num5)/5

print(add)
print(mul)
print(ave)

print('The addition of %s and %s is %s' %(num1, num2, add))
print('The multiplication of %s and %s is %s' %(num1, num2, mul))
print('The average of %s and %s is %s' %(num1, num2, ave))

temperature = "warm"
if temperature =="cold":
    print("Wear a coat")
print("Go outside")

temp = 50
if temp<40:
    print("A little cold, innit?")
else:
    print("Nice weather we be having here")

salary = 35000
years_on_job = 3
if salary>=30000:
    if years_on_job >= 2:
        print("You qualify for the loan")
    else: print("You must have worked for at least two years to get this loan")
else: print("Sorry gee, but you no even try qualify for this loan...E go be")

salary = 35000
years_on_job = 3
if salary >= 30000 and years_on_job >= 2:
    print("You qualify")
else:
    print("You don't")

