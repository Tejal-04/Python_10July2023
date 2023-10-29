#Orignal data
tableData = [['apples','oranges','cherries','banana'],
              ['Alice','Bob','Carol','David'],
              ['dogs','cats','moose','goose']]

#Empty dictonary for sorting the data
newTable = {0:[], 1:[], 2:[], 3:[]}

#Iterate through each list in tableData
for li in tableData:
    for i in range(len(li)):    #put each item of tableData into newTable by index
        newTable[i].append(li[i])

#determine the longest list by number of total characters
#for instance ['apples','Alice','dogs'] would be15 characters
#we will start with longest being zero at the start

longest = 0

#iterate through newTable.For example the first key:value will be 0:['apples','Alice','dogs'].We only really care about the value (the list) in this case

for key,value in newTable.items():
    #determine the total characters in each list so effectively len('applesAlicedogs') for the first list

    length = len(''.join(value))

    #if the length is the longest length do far, make the equal longest

    if length > longest:
        longest = length

#We will loop through the newTable one last time printing spaces infront of each list equal to the difference between the length of the longest list and length of the current list this way it's all nice and tidy to the right

for key,value in newTable.items():
    print(' ' * (longest - len(''.join(value))) + ' '.join(value))   