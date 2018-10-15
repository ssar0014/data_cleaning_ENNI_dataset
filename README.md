# data_cleaning_ENNI_dataset
Includes processes for data cleaning, pre-processing, analysis and visualisation for the ENNI dataset to find out mean differences in some statistics for children with SLI and regular children

This program aims to implement a basic language analyser to investigate the 
linguistic characteristics of children with some form of language disorders. The 
analyser is able to perform basic statistical analysis on a number of linguistic 
features and also to present the analysis results using some form of 
visualisation.

Each of the narrative transcripts is a record of the story-telling task performed 
by a child for the two groups (SLI and TD), under the supervision of an 
examiner (investigator). The stories are elicited by presenting pictures with a 
number of different animal characters to the children participating in the study.

The main objective of this 
program is to read these transcripts of the given dataset, for both the SLI and 
TD groups. We will then conduct a number of pre-processing tasks to extract
only the relevant contents or texts needed for analysis in the subsequent tasks. 

Upon completing the pre-processing tasks, each of the cleaned transcript will be 
saved as an individual output file.

The data required for processing and analysis is the narrative produced by the 
children, which are those statements (or lines) indicated by the label of ‘*CHI:’ 
in the transcripts. The first step is that, for each original  transcript, only those 
statements which are prefixed or begin with ‘*CHI:’ are extracted.
The next step is to perform a set of pre-processing or filtering tasks. We want to 
remove certain words (generally referred as tokens) in each statement that 
consist of some CHAT symbols as either prefixes or suffixes, but retaining 
certain symbols and words for analysis in Task 2.  


The List of Symbols that are filtered out:
1.  Those words that have either ‘[’ as prefix or ‘]’ as suffix are removed but 
these three symbols: [//], [/], and [*] are retained
2.  Those words that have either ‘<’ as prefix or ‘>’ as suffix are retained but 
these two symbols are removed
3.  Those words that have prefixes of ‘&’ and ‘+’ are removed
4.  Those words that have either ‘(’ as prefix or ‘)’ as suffix are retained but 
these two symbols are removed.
It should be noted that there are certain assumptions that have been made while 
these filtering tasks were carried out:

  1.  Anything which comes inside  ‘[ ]’ have been removed without 
  discrimination. 
  
  2.  As such elements which have CHAT significance like [* m] and [* 
  m:+ed] were also getting affected. Thus to ensure that the number of 
  grammatical errors did not get affected, both of those elements i.e., both
  [* m] and [* m:+ed] have been replaced with [*], which are then counted.
  
  3.  It is assumed that long and medium pauses indicated by (..) and (…) need 
  to be counted as pauses. As such all occurrences of (..) and (…) have 
  been replaced by (.), which are subsequently counted.
  
  The second task is about collating the required data for analysis. The main task 
is to produce a number of statistics for the two groups of children transcripts. 
These statistics are those that might serve as good indicators for distinguishing 
between the children with SLI and the typically developed (TD) children.
The statistics for each individual file can then be accessed and seen using the 
menu-based user interaction system built into the script. The user needs to first 
select a script, and analyse it using the analyse_script method defined in the 
class, by accessing it using an object called from the same class. The user can 
then show the statistics which then displays all the statistics that were
calculated in the analyse_script method.
The statistics for each of child transcript that we are interested in are:
• Length of the transcript — indicated by the number of statements
• Size of the vocabulary — indicated by the number of unique words
• Number of repetition for certain words or phrases — indicated by the 
CHAT symbol [/]
• Number of retracing for certain words or phrases — indicated by the 
CHAT symbol [//]
• Number of grammatical errors detected — indicated by the CHAT 
symbol [*]
• Number of pauses made — indicated by the CHAT symbol (.)
Since the length of each child transcript is measured by the number of 
statements, the end of each statement can be determined based on the following 
punctuation marks: either a full stop ‘.’, a question mark ‘?’, or an exclamation 
mark ‘!’
The re module is imported again, as there are certain special symbols like 
apostrophe (') and colon (:) exist within words and need to be removed from the 
script to ensure that there are no discrepancies in the statistics obtained.

In the last task, a class to visualise the statistics collected in Task 2 is 
implemented, as a form of bar graph. The implementation of this visualiser class
makes use of the external Python packages, such as NumPy, SciPy, Pandas, 
and/or Matplotlib in order to create the suitable graphs for comparing the 
statistics collected for the two groups of children transcripts.
Since the data stored is in the form of a dataframe, an additional method called 
as returnDataFrame was made inside the visualiser class. This method simply 
returns the dataframe which allows the representation of the statistics in a 
tabular format, where the columns denote the statistic types and the rows denote 
the statistic counts of each child transcript.
In the visualise_statistics method, two arguments are being taken (self and 
other). This is done so because the invocation of this method by an object, 
should trigger the visualisation of both the bar graphs, which will not be 
possible unless the other object is also taken as an argument. 
This decision assumes that the invocation of the method should immediately 
trigger the display of the graph rather than plot the graph separately outside of 
the class definition.

