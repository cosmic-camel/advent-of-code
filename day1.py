currentTotal = 0
#for number in input:
#    currentTotal+=int(number)
#print currentTotal

repeat = 100000000
baseList = ['a']
positives = baseList * repeat
negatives = baseList * repeat
result = 'i am a liar'
index = 0
notFound = True
while notFound:
    input = open("day1Input", "r")
    notFound = True
    for number in input:
        number = int(number)
        currentTotal += number
        print(str(number) + " | " + str(currentTotal))
        #print(str(currentTotal) + " is the total")
        if currentTotal > 0 and type(positives[currentTotal]).__name__ != 'int':
            #print(str(currentTotal) + " positives | " + type(positives[currentTotal]).__name__)
            positives[currentTotal] = currentTotal
        elif currentTotal <= 0 and type(negatives[abs(currentTotal)]).__name__ != 'int':
            #print (str(currentTotal) + " negatives |" +type(negatives[currentTotal]).__name__)
            negatives[abs(currentTotal)] = currentTotal
        else:
            result = currentTotal
            print("i repeated")
            notFound = False
            break

print(result)
