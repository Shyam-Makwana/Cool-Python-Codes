email = str(input("Enter your Email Id : ")).strip()
username = email[:email.index('@')] 
domain = email[email.index('@')+1:]
text = "Your username is '{}' and domain name is '{}'"
print(text.format(username,domain))

