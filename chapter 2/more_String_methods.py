# replace() method in string 

# replace("which is to replace","from which to replace","and count")

# myself="Hello my name is Anjali";
# print(myself.replace(" ","_"));

# myself="Hello my name is anjali and i am 100yrs old and i like to travel . "
# print(myself.replace("and",",",1));
# print(myself.replace("and",",",2));
# print(myself.replace("and",",",3));




# find() method in string-> it will give the position.

# myself="Hello my name is anjali and i am 100yrs old and i like to travel ."
# print(myself.find("and"));

# myself="and i am 100yrs old and i like to travel ."
# print(myself.find("and"));
# myself="and i am 100yrs old and i like to travel ."

# print(myself.find("and",1));
# here 1 is the position from where it will start searching "and".
# pos1=myself.find("i");
# print(myself.find("i",pos1+1));




# center() method 
# name="Anjali"
#**Anjali**
# print(name.center(8,"*")); 8=len(name)+2stars.

# *Anjali*
# print(name.center(7,"*")); 7=len(name)+1star.

name=input("enter yur name ");
print(name.center(len(name)+4,"😎"));



