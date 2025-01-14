print("Enter the number of friends joining (including you):")

number_of_friends = int(input())

if number_of_friends <= 0:
    print("No one is joining for the party")
    exit()

print("Enter the name of every friend (including you), each on a new line:")

ledger = {}

for _ in range(number_of_friends):
    ledger[input()] = 0

print(ledger)
