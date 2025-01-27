def format_phone_numbers(phone_numbers, country_code):
    if not country_code:
        country_code = "+1"
    for key, value in phone_numbers.items():
        if not value.startswith("+"):
            phone_numbers[key] = country_code + value
    return phone_numbers
