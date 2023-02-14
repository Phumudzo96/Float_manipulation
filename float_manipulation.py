import math                                        # Import the bulit-in function "import math"
from statistics import median                          
list = []
i = 0
for i in range(10):                                # this should be done till it reaches the range
    question = float(input("Enter float value: "))      # Ask user a question
    list.append(question)                          # Add users answer into the list
print(list)                                        # print list with the users inputs

sum = sum(list)                                    # add the numbers in the list
print(f"The totais is {round(sum)}")               

print(f"The max number is {max(list)}")            # print the biggest number in the list
print(f"The min is {min(list)}")                   # print the smalllest number in the list

avarage = sum / 10                                 # calculate the list's avarage
print(f"The avarage is {avarage}")

sum1 = median(list)                                # find the lists median
print(f"The median is {sum1}")
