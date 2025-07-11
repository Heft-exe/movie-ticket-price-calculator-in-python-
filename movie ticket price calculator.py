age = int(input("Enter your age: "))

# Ticket price logic
if age <= 3:
    ticket_price = 0
    print("You are a baby, free show.")
elif age <= 12:
    ticket_price = 5
    print("You are a child, half price. $5")
elif age <= 60:
    ticket_price = 10
    print("You are an adult, full price. $10")
else:
    ticket_price = 5
    print("You are a senior citizen, half price. $5")

# Ask about popcorn
popcorn = input("Would you like popcorn? (YES/NO): ").strip().upper()

# Calculate total
if popcorn == "YES":
    popcorn_price = 5
    total = ticket_price + popcorn_price
    print("Popcorn added: $5")
else:
    popcorn_price = 0
    total = ticket_price
    print("No popcorn added.")

# Final output
print(f"\n🎟️  Final bill: Ticket = ${ticket_price} + Popcorn = ${popcorn_price}")
print(f"💰 Total to pay: ${total}")
print("Welcome to the Movie Ticket Booking System!")
print("Enjoy your movie!")