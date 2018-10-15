'''
Name : Subhasish Sarkar
Student ID: 29819253
Task 1
Date Created : 28th Sept, 2018
Date Modified : 11th October, 2018

'''
# The purpose of this script is to make an analyser class that analyses each transcript
# and produces 6 statistics for the two groups of children.
# The statistics for each individual file can then be accessed and seen using the menu
# based user interaction system built into the script.
# The user needs to first select a script, and analyse it using the analyse_script method
# defined in the class below, by accessing it using an object called from the same class.
# The user can then show the statistics which then displays all the statistics that were
# calculated in the analyse_script method.

# The re module is imported again, as there are certain special symbols like apostrophe (')
# and colon (:) exist within words and need to be removed from the script to ensure that
# there are no discrepancies in the statistics obtained.
import re

# the class definition starts here
class analyser:
    # this is a class which contains methods to analyse the data obtained from cleaning
    # transcripts from the ENNI dataset

    # the constructor consists of the structure of each instance
    # in this case, each instance exists as a dictionary, whose keys are the names of the stats needed
    # and whose keys are the values of those stats for any given script
    # all of them are initialised to 0, so if the user tries to read/display these values without
    # analysing the script first, there will be an error message that is displayed
    def __init__(self):
        self.datastats = {}
        self.datastats['Length'] = 0
        self.datastats["Vocab"] = 0
        self.datastats["Repeats"] = 0
        self.datastats["Retraces"] = 0
        self.datastats['g-errors'] = 0
        self.datastats['pauses'] = 0

    # the __str__ method was overwritten to ensure that when a user wants to print out the stats of the
    # object, they get the desired result instead of the memory location of where the object is stored.
    def __str__(self):
        # if the dictionary's length value is 0 (which is not possible since any script will have atleast one line)
        # while the user tries to print it, it will imply that the user has not analysed the script.
        # in this case, there is an error message.
        if self.datastats["Length"] == 0:
            return "Transcript has not been analysed yet. Please select a transcript to be analysed."

        # once a script has been analysed, and all it's statistics calculated, they are then updated
        # and can thus be displayed
        else:
            lenstr = "The length of the transcript is: "+str(self.datastats["Length"])
            vocabstr = "The size of vocabulary used: "+str(self.datastats["Vocab"])
            repeatstr = "The number of words or phrases repeated done: "+str(self.datastats["Repeats"])
            retracestr = "The number of words or phrases retraced: "+str(self.datastats["Retraces"])
            gerror = "The number of grammatical errors made: "+str(self.datastats["g-errors"])
            pausestr = "The number of pauses made: "+str(self.datastats["pauses"])

            return lenstr+"\n"+vocabstr+"\n"+repeatstr+"\n"+retracestr+"\n"+ gerror+"\n"+pausestr

    # this method calculates the different stats required
    # it takes an extra argument, where the name of the file is entered, and that file is then analysed.
    def analyse_script(self, cleaned_file):

        # for this purpose, the files that were cleaned in task 1 are opened in read mode
        # and each line is read by the file-readlines function
        # an empty list numlines is created which will store all the lines in the cleaned script.
        # since every element of this list will be one line in the script, calculating the length of this list
        # will give us the number of lines in the transcript (length of transcript)
        # an empty set is created which will store the words appearing in each line of the transcript
        # since a set contains distinct elements, the length of the set will indicate how many unique words there are
        # in every line, thus indicating the size of the vocabulary.
        # The number of repetitions are obtained by counting the number of occurrences of [/]
        # The number of retraces are obtained by counting the number of occurrences of [//]
        # The number of grammatical errors are obtained by counting the number of occurrences of [*]
        # The number of pauses made are obtained by counting the number of occurrences of (.)
        fileObj_analyse = open(cleaned_file,"r")
        fileReader = fileObj_analyse.readlines()
        numLines = []
        vocabSet = set()

        for lines in fileReader:
            lines = lines.rstrip() # rstrip is used to remove any trailing whitespaces so that there are no discrepancies in data
            # here it is assumed that every line ends with either an exclamation point (!), question mark (?) or period (.)
            if lines.endswith("!") or lines.endswith("?") or lines.endswith("."):
                numLines.append(lines)
        #print(len(numLines))

        self.datastats['Length'] = len(numLines)

        for lines in fileReader:

            lines = lines.rstrip()
            # words here is a list containing all the charecters and words appearing in the transcript
            words = lines.split()
            for word in words:
                pattern = re.compile(r"[':]") #this re is used to remove all occurrences of (') and (:) from in between words
                word = re.sub(pattern,'',word)

                # a charecter is only taken as a word if it is alphabetical in nature
                # "i" and "a" are also taken as unique words, but all other single charecter alphabets are not
                if word.isalpha() and (len(word)>1 or word == "i" or word == "a"):
                    vocabSet.add(word)

        self.datastats["Vocab"] = len(vocabSet)

        fileObj_analyse = open(cleaned_file,"r")
        fileReader = fileObj_analyse.readlines()
        pattern = "[/]"
        rep_count = 0
        for lines in fileReader:
            rep_count += lines.count(pattern)

        # once the count of each stat is calculated, it is then updated in the
        # self charecteristics
        # this is done for all six stats
        self.datastats["Repeats"] = rep_count

        fileObj_analyse = open(cleaned_file,"r")
        fileReader = fileObj_analyse.readlines()
        pattern = "[//]"
        retr_count = 0
        for lines in fileReader:
            retr_count += lines.count(pattern)

        self.datastats["Retraces"] = retr_count

        fileObj_analyse = open(cleaned_file,"r")
        fileReader = fileObj_analyse.readlines()
        pattern = "[*]"
        gerr_count = 0
        for lines in fileReader:
            gerr_count += lines.count(pattern)

        self.datastats["g-errors"] = gerr_count

        fileObj_analyse = open(cleaned_file,"r")
        fileReader = fileObj_analyse.readlines()
        pattern = "(.)"
        pause_count = 0
        for lines in fileReader:
            pause_count += lines.count(pattern)

        self.datastats["pauses"] = pause_count

        fileObj_analyse.close()


# This menu functionality needs to only be present when task 2 is being run
# Since the analyser class is being imported in task 3 for further computations,
# This should not run when task 3 is being run.
# for that purpose the menu functionality is put inside the __name__ == "__main__" block
# This menu gives 3 options

if __name__ == "__main__":
    while True:
        opt = int(input('''
                1. Select a transcript to analyse
                2. Show Statistics
                3. Exit

                Enter your choice here: 
                '''))
        if opt == 1:
            # option 1 creates an object of the analyser class, and is used to access
            # the analyse_script method inside this class.
            script = input("Enter the name of the file: ")
            analObj = analyser()
            analObj.analyse_script(script)
        elif opt == 2:
            # option 2 is used to then show the statistics obtained from the analyse_script method
            # by printing the object which then returns the overloaded __str__ method
            print(analObj)
            continue
        elif opt == 3:
            # option 3 is used to exit the menu
            break
        else:
            # for any other input an error message is displayed and the menu is displayed until a valid
            # input is obtained
            print("Please enter a valid number")
            continue
