'''
Name : Subhasish Sarkar
Student ID: 29819253
Task 1
Date Created : 28th Sept, 2018
Date Modified : 11th October, 2018

'''
# The purpose of this script is to collect the statistics of all the transcripts from
# the two groups of children, compute the collective averages of all 6 statistics for
# the two groups, and visualise them onto a single graph
# For this purpose, the numpy, pandas, and matplotlib modules are imported since they allow
# for easy numerical analysis,and plotting of data.
# Numpy is aliased as np
# pandas is aliased as pd
# the pyplot function from matplotlib is aliased as plt

# Apart from these modules, since there is a need for actually calculating the statistics
# again, task 2 itself is imported, and its class used here again to find the statistics of all transcripts which are
# then stored inside lists. Each list contains 10 elements, which signify the length, vocab etc of all 10 files.
# These are then stored inside dictionaries, with keys signifying the type of stat, and the length being a list of those stats

# A new class called VisData is created here which holds methods to compute averages and visualise data
# This class takes in data in the form of a list, which is obtained from the dictionary which containes all the stats
# The compute_averages method defined inside, computes the average of each stat for all 10 files each from SLI and TD
# The visualise_statistics method defined inside, then takes all that data and plots it onto a bar graph



#All modules being imported
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from task2_29819253 import analyser

#This is a list of all the source and target lists
SLIlist = ["SLI-"]*10
TDlist = ["TD-"]*10

# sourcelist contains a list of all the source files from SLI-1 to SLI-10 and TD-1 to TD-10
# targetlist contains a list of all the target fules from SLI-1-Cleaned to SLI-10-Cleaned and TD-1-Cleaned to TD-10-Cleaned
# target_sli is then taken a sublist by slicing the targetlist from the 0th index to the 9th index since those are the SLI cleaned Files
# target_td is a sublist sliced from the targetlist from the 10th index till the end since those are the TD cleaned files
# These are then used to create the dictionaries that hold all the statistics obtained from the object which belongs to the class analyser from task 2

sourcelist = []
targetlist = []

i=1
for item in SLIlist:
    item = item+str(i)+".txt"
    i+=1
    sourcelist.append(item)


i=1
for item in TDlist:
    item = item+str(i)+".txt"
    i+=1
    sourcelist.append(item)

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


target_sli = targetlist[0:10]
target_td = targetlist[10:]

# this object belongs to the analyser class imported from task 2

AObj = analyser()

# all these lists will hold statistics from the cleaned SLI transcripts
# they will be stored in a dictionary
SLI_dict_length = []
SLI_dict_vocab = []
SLI_dict_repeat = []
SLI_dict_retrace = []
SLI_dict_gerr = []
SLI_dict_pause = []

# item iterates over the target_sli list
# item in each iteration thus holds the name of a cleaned SLI file
# The object is then used to access the analyse_script method and find the stats of
# the file, which are then stored in their respective lists

for item in target_sli:
    AObj.analyse_script(item)
    SLI_dict_length.append(AObj.datastats['Length'])
    SLI_dict_vocab.append(AObj.datastats["Vocab"])
    SLI_dict_repeat.append(AObj.datastats["Repeats"])
    SLI_dict_retrace.append(AObj.datastats["Retraces"])
    SLI_dict_gerr.append(AObj.datastats["g-errors"])
    SLI_dict_pause.append(AObj.datastats["pauses"])

SLI_dict = {'len':SLI_dict_length,
            'voc':SLI_dict_vocab,
            'rep':SLI_dict_repeat,
            'ret':SLI_dict_retrace,
            'ger':SLI_dict_gerr,
            'pau':SLI_dict_pause}

# this list can then be made by accessing the keys of the dictionary
# this is thus a list which contains all the stats of the SLI group as a list of 6 lists
# each element being a list that contains the actual stat for each SLI transcript
# this list is then used as arguments when objects are made of this class
SLI_statslist = [SLI_dict['ger'], SLI_dict['len'], SLI_dict['pau'], SLI_dict['rep'], SLI_dict['ret'], SLI_dict['voc']]

# The same thing is done with TD cleaned scripts
BObj = analyser()

TD_dict_length = []
TD_dict_vocab = []
TD_dict_repeat = []
TD_dict_retrace = []
TD_dict_gerr = []
TD_dict_pause = []

for item in target_td:
    BObj.analyse_script(item)
    TD_dict_length.append(BObj.datastats['Length'])
    TD_dict_vocab.append(BObj.datastats["Vocab"])
    TD_dict_repeat.append(BObj.datastats["Repeats"])
    TD_dict_retrace.append(BObj.datastats["Retraces"])
    TD_dict_gerr.append(BObj.datastats["g-errors"])
    TD_dict_pause.append(BObj.datastats["pauses"])


TD_dict = {'len':TD_dict_length,
            'voc':TD_dict_vocab,
            'rep':TD_dict_repeat,
            'ret':TD_dict_retrace,
            'ger':TD_dict_gerr,
            'pau':TD_dict_pause}



TD_statslist = [TD_dict['ger'], TD_dict['len'], TD_dict['pau'], TD_dict['rep'], TD_dict['ret'], TD_dict['voc']]


# The class is then made
class VisData:
    #this is a class that contains methods to obtain visual representations
    #of the analysis done between the two data sets

    # the instance variable's structure is made in this constructor
    # it takes data as an argument whenever an instance is created
    # this argument is will be either the SLI_statslist or the TD_statslist depending on the which group's object is being made

    def __init__(self,data):
        self.data = data
        self.gerr = self.data[0]
        self.len = self.data[1]
        self.pau = self.data[2]
        self.rep = self.data[3]
        self.ret = self.data[4]
        self.voc = self.data[5]
        self.avg_gerr = 0
        self.avg_len = 0
        self.avg_pau = 0
        self.avg_ret = 0
        self.avg_rep = 0
        self.avg_voc = 0
        # This dictionary stores all the stats, as list stored in the values which are represented by their respective keys
        # This dictionary is then converted into a dataframe for storage
        self.datadict = {'gerr':self.gerr, 'len':self.len, 'pau':self.pau, 'rep':self.rep, 'ret':self.ret, 'voc':self.voc}
        self.df1 = pd.DataFrame(self.datadict,index = ['Script 1', 'Script 2', 'Script 3','Script 4','Script 5','Script 6','Script 7','Script 8','Script 9','Script 10',])

    # This is a method that is used to display the data as a dataframe where the column names are the names of each statistic
    # and the row names are the names of each script
    def returnDataFrame(self):
        return self.df1

    # This method computes the averages of all the statistics
    # The stats are each stored as lists, which are then converted to numpy arrays
    # The advantage of that is that they can then be used to calculate aggregate averages by using the array.mean() function
    def compute_averages(self):
        mean_arr = np.array(self.gerr)
        mean_gerr = mean_arr.mean()
        self.avg_gerr = mean_gerr

        mean_arr = np.array(self.len)
        mean_len = mean_arr.mean()
        self.avg_len = mean_len

        mean_arr = np.array(self.pau)
        mean_pau = mean_arr.mean()
        self.avg_pau = mean_pau

        mean_arr = np.array(self.rep)
        mean_rep = mean_arr.mean()
        self.avg_rep = mean_rep

        mean_arr = np.array(self.ret)
        mean_ret = mean_arr.mean()
        self.avg_ret = mean_ret

        mean_arr = np.array(self.voc)
        mean_voc = mean_arr.mean()
        self.avg_voc = mean_voc

        # Each of the averages are then printed out onto the console with their respective strings
        statement = "Average length of Transcript: " + str(mean_len) + "\n" + "Average Grammatical Errors: " + str(mean_gerr) + "\n" + "Average Number of Pauses: " + str(mean_pau) + "\n" + "Average Number of Repetitions of Words/Phrases: " + str(mean_rep) + "\n" + "Average Number of Words/Phrases Retraced: " + str(mean_ret) + "\n" + "Average Size of Vocabulary: " + str(mean_voc)
        print(statement)

    # This method will take all the means calculated above, and store them inside 2 lists namely the script_stats_TD and script_stats_SLI lists
    # Since this method needs to plot both the graphs simultaneously, there needs to be 2 objects used
    # the self will denote which child group's object is being used to call the method, and the other will be the object of the other child group
    # these will then be used to store the means of all the stats in the 2 lists mentioned above
    # these lists will store the values which will then be plotted on the bar graph
    def visualise_statistics(self,other):
        stats_labels = ["Len", "Errors", "Pau", "Rep", "Retr", "Vocab"] # these are the labels which will appear below each bar
        x_label = "Statistics" # this is the label of the x axis
        y_label = "Mean Difference" # this is the label of the y axis
        title = "Mean difference in the statistics of SLI vs. TD measured" # this is the title of the plot

        script_stats_SLI = [self.avg_len, self.avg_gerr, self.avg_pau, self.avg_rep, self.avg_ret, self.avg_voc]
        script_stats_TD = [other.avg_len, other.avg_gerr, other.avg_pau, other.avg_rep, other.avg_ret, other.avg_voc]

        # since plt.bar cannot take string values as arguments, a temporary array containing numbers from 0 to 5 are taken
        # these are then mapped to the labels defined in the stats_labels list above
        # mapping is done based on the index of the elements and the number in the array
        ypos_SLI = np.arange(len(script_stats_SLI))
        ypos_TD = np.arange(len(script_stats_TD))
        plt.xticks(ypos_SLI,stats_labels)
        plt.xticks(ypos_TD,stats_labels)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.bar(ypos_SLI+0,script_stats_SLI, color = 'r',label = "SLI",width=0.4) # plots the bar graph of SLI averages
        plt.bar(ypos_SLI+0.4,script_stats_TD, color = 'g', label = "TD", width = 0.4) # plots the bar graph of TD averages, shifted 0.4 from that of the SLI bar
        plt.legend()
        plt.show()

# Objects are then made for TD and SLI belonging to the above defined VisData class
# these objects are then used to access all the methods inside and thus display the graph containing the averages
# of all stats for both the groups
visualiserObj_TD = VisData(TD_statslist)
visualiserObj_SLI = VisData(SLI_statslist)
print('\nTD Statistics: \n')
visualiserObj_TD.compute_averages()
print('\nSLI Statistics: \n')
visualiserObj_SLI.compute_averages()

df1 = visualiserObj_TD.returnDataFrame()
df2 = visualiserObj_SLI.returnDataFrame()

print("\nTD Statistics Data Frame\n")
print(df1)
print("\nSLI Statistics Data Frame\n")
print(df2)

visualiserObj_SLI.visualise_statistics(visualiserObj_TD)
