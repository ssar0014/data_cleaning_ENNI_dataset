'''
Name : Subhasish Sarkar
Student ID: 29819253
Task 1
Date Created : 24th Sept, 2018
Date Modified : 2nd October, 2018
'''
# The purpose of this script is to read the SLI and TD transcripts and clean them using the metrics
# mentioned in the Assignment specifications. For this purpose, the re module is being used, to incorporate
# regular expressions to match certains patterns which are then replaced with empty strings to ensure that
# they are removed completely from the script.

#The re module is being imported to use regular expressions within the script
import re

# 2 lists are made which are required to clean those elements that occur within parantheses ()
# they are set to global to ensure that they can be used throughout the entire span of the code, within
# functions and outside of them.
# the first list, list_char contains all the alphabets within parantheses which can be encountered within the transcript
# the second list, list_repl is a list of replacements which will be used to replace any of the items found within the list_char
# that may appear in the transcript
global list_char
global list_repl
list_char = ['(a)','(b)','(c)','(d)','(e)','(f)','(g)','(h)','(i)','(j)','(k)','(l)','(m)','(n)','(o)','(p)','(q)','(r)','(s)','(t)','(u)','(v)','(w)','(x)','(y)','(z)']
list_repl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# The whole cleaning process is being modularised by encasing them inside this dataClean function
# This function can be called to take in an uncleaned source transcript, clean it using the code degined inside it
# And then finally write the cleaned output to a target file
# These source and target files are mentioned by name in this function's arguments as strings
# with the .txt extension
def dataClean(source, target):
# Files are opened with the file-open function in read mode  and the contents are read using the file-read function.
# Once the file is read, it is then stored into a variable called "linestr",
# which stores every line of each file within a  string.
# To ensure that all child statements are taken as a single line, and are not separated on the basis of multiple
# lines, the special charecter "\n\t" is removed. It is so because multi-line child statements have a special condition
# where there is a newline charecter immediately followed by a tab charecter.
# the data from the files are then stored inside a list also named as linestr, essentially meaning that the linestr string
# is updated into a list by splitting it on the basis of "\n"
# linestr now contains all the data in it, the elements of which are each of the individual lines within the transcript.
# a new list named "child_statements" is made which is then appended with those lines which contain "*CHI: " within them. Essentially
# rendering all the elements within child_statements to be child statements exclusively.
    fileObj = open(source,'r')
    lineStr = fileObj.read()

    fileObj = fileObj.close()

    lineStr = lineStr.replace("\n\t"," ")
    lineStr = lineStr.split('\n')

    child_statements = []
    for element in lineStr:
        if '*CHI:' in element:
            child_statements.append(element)


# Once the child statements have been extracted from the transcripts into a list, they are then extracted
# sequentially from the list by iterating over a for loop, and cleaned.
# For this purpose, the a file is opened in write mode, and regular expressions are applied to match all the
# cases mentioned in the assignment documentation.
    fileObj_write = open(target, "w")
    for item in child_statements:
        # item is sliced so that the initial tabs are not included in the cleaned file or while matching
        # regular expressions
        item = item[5:]
        # initially all the charecter elements that occur inside parantheses are cleaned
        # for this purpose the two global lists are used, and wherever an alphabet charecter exists within
        # parantheses, they are replaced with the alphabets without the parantheses from the list_repl list
        # thus removing the parantheses
        for elem in list_char:
            if elem in item:
                repl_elem = list_repl[list_char.index(elem)]
                item = item.replace(elem,repl_elem)
        # the following statements are regular expressions for:
        # 1. Removing those words that have either ‘[’ as prefix or ‘]’ as suffix but retaining these three
        # symbols: [//], [/], and [*]
        # 2. Retaining those words that have either ‘<’ as prefix or ‘>’ as suffix but removing those two symbols
        # 3. Removing those words that have prefixes of ‘&’ and ‘+’
        # By matching occurences of above mentioned cases, the function re.sub substitutes the matched string with
        # whatever is written as the 2nd argument, from the element mentioned as the 3rd argument
        match = item
        match = re.sub(r'\* m\:\+ed','*',match)
        match = re.sub(r'\*\sm(\:\W\w\w)*','*',match)
        match = re.sub(r'\[\W\s\w*?\W*?\w*?\]','',match)
        match = re.sub(r'\[\W(\s\w+)+?\]','',match)
        match = re.sub(r'\[\W*(\s\w+){2}?\W\w+\W\]','',match)
        match = re.sub(r'\[\?\]|\[\!\]|\[/\-\]','',match)
        match = re.sub(r'\[\^.+?\]','',match)
        match = re.sub(r'\+.*','.',match)
        match = re.sub(r'\[\w\s\d\]','',match)
        match = re.sub(r'\<|\>','',match)
        match = re.sub(r'\&\W*\w*|\+(\.)*','',match)
        match = re.sub(r'\(\.\.\)|\(\.\.\.\)','(.)',match)

        # Here all the remaining tabs are removed, and a newline charecter added so that the new file
        # now contains every cleaned child statement as an individual line
        match = match.replace("\t","")
        match = match + "\n"

        pattern = re.compile(r"\(\w{2,}\)")
        matchPar = pattern.findall(match)

        for iters in matchPar:
            iters = iters.replace("(","")
            iters = iters.replace(")","")
            repl = iters
            match = re.sub(pattern,repl,match)

        # Once the cleaning has been done, the cleaned data is written onto the target file and the file is closed.
        fileObj_write.write(match)

    fileObj_write.close()


# The following is a list of source and target lists stored in the form of list of strings
# sourcelist contains a list of all the source files from SLI-1 to SLI-10 and TD-1 to TD-10
# targetlist contains a list of all the target fules from SLI-1-Cleaned to SLI-10-Cleaned and TD-1-Cleaned to TD-10-Cleaned
# These lists are then passed as arguments recursively into the above defined function for data readind, cleaning, and finally writing
# Since the order of SLI and TD transcripts being added is maintained,
# the source-target pairing is always consistent when the files go into the cleaning function

SLIlist = ["SLI-"]*10 # creates a list of 10 "SLI-" elements
TDlist = ["TD-"]*10 # creates a list of 10 "TD-" elements

sourcelist = []
targetlist = []

# An iterator i is defined which can be used to make all the list names
i=1
for item in SLIlist:
    item = item+str(i)+".txt"
    i+=1
    sourcelist.append(item) # creates a list of all SLI files from SLI-1.txt to SLI-10.txt


i=1
for item in TDlist:
    item = item+str(i)+".txt"
    i+=1
    sourcelist.append(item) # appends to the previous list, a list of all TD files from TD-1.txt to TD-10.txt
                            # so sourcelist now becomes a list of 20 elements, from SLI-1.txt to TD-10.txt

#Similarly from the below block of code, the targetlist is a list of 20 elements, from SLI-1-Cleaned.txt to TD-10-Cleaned.txt
i=1
for item in SLIlist:
    item = item+str(i)+"-Cleaned.txt"
    i+=1
    targetlist.append(item)

i=1
for item in TDlist:
    item = item+str(i)+"-Cleaned.txt"
    i+=1
    targetlist.append(item)

# An iterator filenumber is made so that the every file is sequentially cleaned within the for loop
# The iterator gets updated every loop iteration to ensure every file gets cleaned
filenumber = 0
for temp_iter in range(len(sourcelist)):
    dataClean(sourcelist[filenumber],targetlist[filenumber])
    filenumber+=1

print("\nAll SLI transcripts have been cleaned. The cleaned files will be named as 'SLI-i-Cleaned.txt' (i will range from 1 to 10), please access them as so.\n")
print("\nAll TD transcripts have been cleaned. The cleaned files will be named as 'TD-i-Cleaned.txt' (i will range from 1 to 10), please access them as so.\n")
