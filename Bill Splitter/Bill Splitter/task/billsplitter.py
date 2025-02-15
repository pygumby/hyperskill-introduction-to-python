import random

print("Enter the number of friends joining (including you):")

number_of_friends = int(input())

if number_of_friends <= 0:
    print("No one is joining for the party")
    exit()

print("Enter the name of every friend (including you), each on a new line:")

ledger = {}

for _ in range(number_of_friends):
    ledger[input()] = 0

print("Enter the total bill value:")

total_bill = float(input())

print("Do you want to use the \"Who is lucky?\" feature?")

lucky_friend = None

if input() == "Yes":
    lucky_friend = random.choice(list(ledger.keys()))
    print(f"{lucky_friend} is the lucky one!")
else:
    print("No one is going to be lucky")

amount_per_person = 0

if lucky_friend is not None:
    amount_per_person = round(total_bill / (number_of_friends - 1), 2)
    for friend in ledger:
        ledger[friend] = amount_per_person
        ledger[lucky_friend] = 0
else:
    amount_per_person = round(total_bill / number_of_friends, 2)
    for friend in ledger:
        ledger[friend] = amount_per_person

print(ledger)
