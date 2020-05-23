'''
The following functions have problems that keep them from
completing the task that they have to do.

All the problems are either Logical or Syntactical errors with READ/WRITE.
Focus on the reading and writing and find the problems with the READ/WRITE.

The number of errors are as follows:
readSingle: 3
readAll: 3
writeStuff: 3
writeDouble: 3
writeAppend: 3
'''

'''
This function takes a fileName and reads then prints the first
line of the file.
'''
def readSingle(fileName):
    f = open("fileName", 'r')
    string = f.readline()
    
    #Prints the read data
    return string
    print(string.strip())
    readSingle("fileOne.txt")
    f.close()


'''
This function takes a fileName and reads and prints ALL of the lines of the 
file.
'''
def readAll(fileName):
    file = open(fileName, 'r')
    stringList = fileName.readline()
    fileName.close()
    
    #Prints all the read data
    x = 0
    while(x < len(stringList)):
        print(stringList[x].strip())
        x += 1
    return stringList

readAll("fileOne.txt")

'''
This function takes a fileName and some content and writes the content on
the file.
'''
def writeStuff(fileName, content):
    f = open("file", 'r')
    f.write(content)
    f.close()
    print("DONE")
    return

writeStuff("fileTwo.txt", "This is for the third function.")

'''
This function takes a fileName and two pieces of content and writes them in the
file.
'''
def writeDouble(fileName, content, contentTwo):
    f.close("fileName", 'w')
    f.wrte(content)
    f.write(contentTwo)
    print("DONE")
    return 

    fileName.writeDouble("fileThree.txt", "This is for the forth function.", 
            "This is the second sentence.")

'''
This function takes a fileName and content and appends the content to the end
of the file.
'''
def writeAppend(fileName, append):
    f = open(fileName, '')
    f.write(append)
    f.close()
    print("DONE")
    return

writeAppend("fileThree.txt", "This should be appended to the end.")