def calculate_total(prices: dict[str, float], quantities: dict[str, int]) -> float:
    total = 0.0
    for item in prices:
        total += prices[item] * quantities[item]
    return total
