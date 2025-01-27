def categorize_items(categories, items):
    categorized = {}
    for category, item in zip(categories, items):
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(item)
    return categorized
