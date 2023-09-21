#create an empty set
s = set()

#add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
print(s)
s.remove(2)
print(s)
print(f"The Length of the set is:{len(s)}")

user_input = input("Do you want to print the minimum value in the set? (Y/N): ")

if user_input.lower() == "y":
    print(f"The min value in the set is:{min(s)}\n")
    user_input = "n"
else:
    print("Okay, I won't print the minimum value in the set.\n")
    user_input = "n"

user_input = input("Do you want to print the maximum value in the set? (Y/N): ")

if user_input.lower() == "y":
    print(f"The max value in the set is:{max(s)}\n")
    user_input = "n"
else:
    print("Okay, I won't print the maximum value in the set.\n")
    user_input = "n"

user_input = input("Do you want to append values in the set? (Y/N): ")

if user_input.lower() == "y":
    append_element = input("Enter the text/number you want to append: ")
    s.add(append_element)
    print(s,"\n")
    user_input = "n"
else:
    print("Okay.\n")
    user_input = "n"
