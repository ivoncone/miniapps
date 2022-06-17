
url_input = input("enter url :")
words = ['https://www']
x = [word for word in words if(word in url_input)]
proof = ''
proof = (bool(x))
val = proof
if val == False:
	print("invalid url")
if val == True:
	print("continue...")


	