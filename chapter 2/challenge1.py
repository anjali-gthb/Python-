# ask user to input 3 numbers and you have to print average of three numbers using string formatting
# bonus- try to take all three comma separated inputs in one line.

num1,num2,num3 =input("enter all three marks spearted by commas").split(",")
average=int(int(num1)+int(num2)+int(num3))/3;
print(f"the average of the marks is {average}");