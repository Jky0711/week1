"""
Write a Python function named speeding_ticket that evaluates whether a driver should receive a speeding ticket based on their driving speed and a special condition (their birthday).

The function should return one of three strings based on the driver's speed: "No Ticket", "Small Ticket", or "Big Ticket".
If the driver's speed is 60 mph or less, they should receive "No Ticket".
If the driver's speed is between 61 and 80 mph inclusive, they should receive a "Small Ticket".
If the driver's speed is 81 mph or more, they should receive a "Big Ticket".
On the driver's birthday, the speed limits for each ticket category are increased by 5 mph. For example, they can go up to 65 mph and still receive "No Ticket" if it is their birthday.
"""

def speeding_ticket(speed, is_birthday):
    # Adjust speed limits if it's the driver's birthday
    adjustment = 5 if is_birthday else 0

    # Determine the ticket type based on adjusted speed limits
    if speed <= 60 + adjustment:
        return "No Ticket"
    elif 61 <= speed <= 80 + adjustment:
        return "Small Ticket"
    else:
        return "Big Ticket"

print(speeding_ticket(60, False))
print(speeding_ticket(65, True)) 