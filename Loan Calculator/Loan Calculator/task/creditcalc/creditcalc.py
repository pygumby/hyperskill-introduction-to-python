import argparse
import math
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--payment")
parser.add_argument("-p", "--principal")
parser.add_argument("-n", "--periods")
parser.add_argument("-i", "--interest")

args = parser.parse_args()

if len(sys.argv) != 4 or args.interest is None:
    exit("Three arguments need to be provided, including the interest.")

def calculate_payment(p, i, n):
    return p * (i * (1 + i) ** n) / ((1 + i) ** n - 1)

def calculate_principal(a, i, n):
    return a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))

def calculate_periods(p, i, a):
    return math.log(a / (a - i * p), 1 + i)

nominal_interest = float(args.interest) / (12 * 100)

if args.payment is None:
    a = calculate_payment(float(args.principal), nominal_interest, int(args.periods))
    print(f"Your monthly payment = {math.ceil(a)}")
elif args.principal is None:
    p = calculate_principal(float(args.payment), nominal_interest, int(args.periods))
    print(f"Your loan principal = {p}!")
else:
    n = calculate_periods(float(args.principal), nominal_interest, float(args.payment))
    years = math.floor(math.ceil(n) / 12)
    months = math.ceil(math.ceil(n) % 12)
    if months == 0:
        print(f"It will take {years} years to repay this loan.")
    else:
        print(f"It will take {years} years and {months} months to repay this loan.")

# import math

# print("Enter the loan principal:")
# principal = int(input())

# print("What do you want to calculate?")
# print("type \"m\" - for number of monthly payments,")
# print("type \"p\" - for the monthly payment:")
# calculation = input()

# if calculation == "m":
#     print("Enter the monthly payment:")
#     installments = int(input())
#     months = math.ceil(principal / installments)
#     print(f"It will take {months} month{'' if months == 1 else 's'} to repay the loan.")
# else:
#     print("Enter the number of months:")
#     months = int(input())
#     installments = math.ceil(principal / months)
#     if principal % months != 0:
#         last_installment = principal - (months - 1) * installments
#         print(f"Your monthly payment = {installments} and the last payment = {last_installment}")
#     else:
#         print(f"Your monthly payment = {installments}")
