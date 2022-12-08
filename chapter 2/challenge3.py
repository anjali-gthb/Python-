# take two comma separated inputs from users
# 1. users name
# 2. a single character

# output - 2 print lines 
# 1. users name length
# 2.count the charcter that user inputed(bonus: case insensitive count)

# 1.
name,charcter=input("enter the name and a single character separated by commas ").split(",");
print(len(name));
# print(name.count(charcter));
# if the input is anjali, a   
# so the count will it give-> 0
#because see clearly after comma i give a space then "a" it will consider spacea and find it in name variable 

# its solution
print(name.strip().lower().count(charcter.strip().lower()))
# char.strip().lower()


# 2.
# print(f"the count is {name.lower().count(charcter.lower())} ")
