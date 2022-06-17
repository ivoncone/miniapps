
rfc = input("enter your rfc: ")

if len(rfc) < 12 or len(rfc) > 13:
		print("Enter valid rfc")

if rfc == 'XAXX010101000':
		print("You can use this rfc")

if any(char.islower() for char in rfc):
		print("Enter valid rfc")

if not any(char.isdigit() for char in rfc):
		print("Enter valid rfc")

