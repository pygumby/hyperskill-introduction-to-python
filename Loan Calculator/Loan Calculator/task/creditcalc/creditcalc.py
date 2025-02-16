import math

print("Enter the loan principal:")
principal = int(input())

print("What do you want to calculate?")
print("type \"m\" - for number of monthly payments,")
print("type \"p\" - for the monthly payment:")
calculation = input()

if calculation == "m":
    print("Enter the monthly payment:")
    installments = int(input())
    months = math.ceil(principal / installments)
    print(f"It will take {months} month{'' if months == 1 else 's'} to repay the loan.")
else:
    print("Enter the number of months:")
    months = int(input())
    installments = math.ceil(principal / months)
    if principal % months != 0:
        last_installment = principal - (months - 1) * installments
        print(f"Your monthly payment = {installments} and the last payment = {last_installment}")
    else:
        print(f"Your monthly payment = {installments}")
