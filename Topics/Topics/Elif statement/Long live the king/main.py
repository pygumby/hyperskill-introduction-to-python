def is_position_valid(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8

x = int(input())
y = int(input())

valid_moves = 0

if is_position_valid(x - 1, y):
    valid_moves += 1
if is_position_valid(x + 1, y):
    valid_moves += 1
if is_position_valid(x, y - 1):
    valid_moves += 1
if is_position_valid(x, y + 1):
    valid_moves += 1
if is_position_valid(x - 1, y - 1):
    valid_moves += 1
if is_position_valid(x - 1, y + 1):
    valid_moves += 1
if is_position_valid(x + 1, y - 1):
    valid_moves += 1
if is_position_valid(x + 1, y + 1):
    valid_moves += 1

print(valid_moves)
