
import time
pwd = 'mooon'
count = 0 # Create a variable, to ensure the user has limited attempts at entering their correct username and password
while True:
	password = input("password: ")
	count += 1
	if password != pwd:
		print("your password is incorrect")
	if count == 3:
		print("\nYou made three Password Attempts. Goodbye")
		time.sleep(30)
		break
	print(count)