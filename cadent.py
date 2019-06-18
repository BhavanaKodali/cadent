# Open and read the File in read only and copied data to Variable f
f=open("file1.txt","r")  
list1=list() # Variable
count=0
for line in f:
# Split the line into words
    words=line.split() 
# Copying 1st letter in word converting into lover case and copy to list1
    list1.append((words[0][0].lower())) 
# Sorting the data and remove the duplicate and copied to the List1 Variable
set1=sorted(set(list1)) 
# Copying Data inside set1 to list2 Variable
list2=list(set1) 
# This loop is to count the Letters
# Comparing both sorted and unsorted data
for letter_list2 in list2:
    for letter_list1 in list1:
    
        if letter_list2 == letter_list1 : 
            count=count+1 

# Output will be printed with data inside "letter_list2" variable and String Module will do Number to string convertion and print output with , seperated
    print(letter_list2+","+str(count)) 
    count=0


