lbs = []
kgs = []
#giving the input
total = int(input("Enter the number of students:"))
for i in range(total):
    num = int(input('Enter the weights:'))
    lbs.append(num)
    #convert lbs to kgs
    kilograms = num * 0.454
    kgs.append(round(kilograms))
    #print the data
print(lbs,kgs)
