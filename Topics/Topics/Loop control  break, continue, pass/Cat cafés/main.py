cafes = {}

while True:
    s = input()
    if s == "MEOW":
        break
    cafe = s.split()
    cafes.update({cafe[0]: int(cafe[1])})

print(max(cafes, key=lambda x: cafes[x]))
