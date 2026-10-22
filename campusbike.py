# CampusBike settings and price.
# Run with: python3 campusbike.py   (Windows: py campusbike.py)

# Longest rental without a late fee, in hours
MAX_RENTAL_HOURS = 3

# Price per hour, in DKK
PRICE_PER_HOUR = 10

# Extra fee if the bike is kept too long, in DKK
LATE_FEE = 50


def rental_price(hours):
    """Price in DKK for one rental. Late fee if the bike is kept too long."""
    price = hours * PRICE_PER_HOUR
    if hours > MAX_RENTAL_HOURS:
        price = price + LATE_FEE
    return price


if __name__ == "__main__":
    print("Max rental time:", MAX_RENTAL_HOURS, "hours")
    print("Price for 2 hours:", rental_price(2), "DKK")
    print("Price for 4 hours:", rental_price(4), "DKK")
