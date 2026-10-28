
print("Welcome to PayUp!")

event = input("what is the event? ")
cost = float(input("what is the cost? "))
service_charge = int(input("was there any service charge? if yes enter a whole number (e.g. 30 for 30%) ").strip("%"))
group_size = int(input("how many people are splitting the bill? "))
grand_total = (cost + (cost * service_charge / 100))
total_per_person = (grand_total / group_size)
print()
print("---" * 14)

print() 
print(f"Here's the breakdown for {event}:")
print()
print(f"Cost: ${cost:.2f}")
print(f"Service charges: ${service_charge:.2f}")
print(f"total service charges: ${cost * service_charge / 100:.2f}")
print(f"Group size: {group_size}")
print(f"Grand total: ${grand_total:.2f}")
print()
print(f"Each person must PayUp: ${total_per_person:.2f}")
print("---" * 14)




