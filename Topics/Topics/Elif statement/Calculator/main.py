f1 = float(input())
f2 = float(input())
op = input()

if (op == "/" or op == "mod" or op == "div") and f2 == 0:
    print("Division by 0!")
elif op == "+":
    print(f1 + f2)
elif op == "-":
    print(f1 - f2)
elif op == "*":
    print(f1 * f2)
elif op == "/":
    print(f1 / f2)
elif op == "mod":
    print(f1 % f2)
elif op == "pow":
    print(f1 ** f2)
elif op == "div":
    print(f1 // f2)
else:
    print(f"Unknown operator: {op}")
