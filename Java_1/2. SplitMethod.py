# write a program that takes a single input (email), extract just domain part


email = input("Give your email: ")

# gezim.ciriku@gmail.com

#print(email.split("@"))

email_split = email.split("@")

print(email_split[-1])