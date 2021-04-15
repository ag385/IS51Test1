"""
Structured-English
The Salary Option Program is trying to compare and determine which two salary options pays better for 10 days of work.

The first salary option is offering $100 per day for 10 days of work equating to $1,000.

The second salary option doubles each day offering $1 the first day, $2 the second day, $4 the third day, $8 the fourth day,
$16 the fifth day, $32 the sixth day, $64 the seventh day, $128 the eighth day, $256 the ninth day, and $512 the 
tenth day for 10 days of work equating to $1,023.

Then the sum of the first and second salary option will be compared to determine which option pays better.
If the first salary option is better than the second salary option, then the first salary option is better.
If the second salary option is better than the first salary option, then the second salary option is better.
However, if the first salary option and the second salary option equal each other, then the first salary option
and second salary option are the same. 

"""

"""
Pseudo-Code

option1 is 100 * 10 (1000)

list
i is 0
while initialize less than 10
    amount = amount * 2
    add amount to list
total list (1023)
option2 is list
         
If option 1 is better:
    print "Option 1 is better."
If option 2 is better:
    print "Option 2 is better."
If option 1 and option 2 are the same:
    priont "Option 1 and Option 2 pays the same."

"""

#Python Programming Exam-End

option1 = 100 * 10     #Prints 1000
# print(option1)

list1 = []
amount = 1
while amount <= 600:
    list1.append(amount)
    amount *= 2
                                # print(list1)
                                # print(sum(list1))
option2 = sum(list1)



if option1 > option2:
    print("Option 1 is better.")
if option2 > option1:
    print("Option 2 is better.")
else:
    print("Option 1 and Option 2 pays the same.")