from werkzeug.security import generate_password_hash, check_password_hash

password = input()
pwd_encrypted = generate_password_hash(password)
#print(check_password_hash(pwd_encrypted, password))
print(pwd_encrypted)