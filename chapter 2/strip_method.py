# name="     anjali     "
# dots="..........."
# print(name+dots);

# to remove the left side space we uses lstrip method.
# print(name.lstrip()+dots);

# to remove the right side space we uses rstrip method.
# print(name.rstrip()+dots);

# to remove both side spaces use strip()method only.
# print(name.strip()+dots);

# if name="       anja  li          "
# strip method will not remove the space between the variable.

# if you want to remove all the spaces of your variable use replace method.
name="      anj  ali     "
print(name.replace(" ",""))  #first argument is space and the second one is from whom you want to replace it so,without space.
