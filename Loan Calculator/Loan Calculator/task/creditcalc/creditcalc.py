import argparse
import math
import sys

# Command-line arguments

parser = argparse.ArgumentParser()

parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()
numeric_args = [args.payment, args.principal, args.periods, args.interest]

# Functions for input validations

def print_msg_and_exit():
    print("Incorrect parameters")
    exit()

def check_args_n():
    if len(sys.argv) != 5:
        print_msg_and_exit()

def check_type_arg_correct():
    if args.type not in ["annuity", "diff"]:
        print_msg_and_exit()

def check_interest_arg_not_none():
    if args.interest is None:
        print_msg_and_exit()

def check_payment_arg_none_if_diff():
    if args.type == "diff" and args.payment is not None:
        print_msg_and_exit()

def check_numeric_args_positive():
    negative_values = [arg for arg in numeric_args if arg is not None and arg.startswith('-')]
    if negative_values:
        print_msg_and_exit()

# Functions for loan calculations

def calc_ann_payment(principal, interest, periods):
    return principal * (interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)

def calc_ann_principal(payment, interest, periods):
    return payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))

def calc_ann_periods(principal, interest, payment):
    return math.log(payment / (payment - interest * principal), 1 + interest)

def calc_diff_payment(principal, interest, current_period, total_periods):
    return principal / total_periods + interest * (principal - principal * (current_period - 1) / total_periods)

# Check provided arguments

check_args_n()
check_type_arg_correct()
check_interest_arg_not_none()
check_payment_arg_none_if_diff()
check_numeric_args_positive()

# Calculate and print loan data

principal = float(args.principal) if args.principal is not None else None
payment = float(args.payment) if args.payment is not None else None
periods = int(args.periods) if args.periods is not None else None
interest = float(args.interest)
nominal_interest = float(args.interest) / (12 * 100)

if args.type == "annuity":
    if payment is None:
        payment = calc_ann_payment(principal, nominal_interest, periods)
        print(f"Your monthly payment = {math.ceil(payment)}")
    if principal is None:
        principal = calc_ann_principal(payment, nominal_interest, periods)
        print(f"Your loan principal = {principal}!")
    if periods is None:
        periods = calc_ann_periods(principal, nominal_interest, payment)
        years = math.floor(math.ceil(periods) / 12)
        months = math.ceil(math.ceil(periods) % 12)
        if months == 0:
            print(f"It will take {years} years to repay this loan.")
        else:
            print(f"It will take {years} years and {months} months to repay this loan.")
        print(f"Overpayment = {principal - payment * math.ceil(periods)}")

if args.type == "diff":
    if payment is None:
        payments = [
            math.ceil(calc_diff_payment(principal, nominal_interest, m, periods))
            for m in range(1, periods + 1)
        ]
        for i, payment in enumerate(payments, 1):
            print(f"Month {i}: {payment}")
        print(f"Overpayment = {sum(payments) - principal}")
