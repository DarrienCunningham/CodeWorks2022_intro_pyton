file = open("files/paragraph.txt", "r")

par = file.read()
par1 = par.replace(',','')
par1 = par1.replace('\'','')

#turn the paragraph into a list of words

list = par1.split(' ')
file.close()
list.sort()
#the variable where you will store the dictionary file
myDict ={}

for x in list:
    if x in myDict:
        a = myDict.get(x) + 1
        myDict.update({x : a})
    else:
        myDict.update({x : 1})


print(myDict)
save = open("files/wordCount.txt", "w")
save.write(str(myDict))
save.close()

#your code
