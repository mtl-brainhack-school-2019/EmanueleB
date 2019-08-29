## High-level summary of the project (about 50 words) include Project relevance
Aim: Management of a large dataset composed by behavioural data (sung performances) 

achieved by writing a program that is able to perform and automate the following steps
-Data cleaning
-Data organization
-Data visualization
-Data analysis (preliminary analysis)


Why this is important 

These goals are justified by the necessity to optimize time and ressources in managing and updating behavioural data that my lab is currently collecting.
The process is to eliminate almost entirely any type of manual work.

![](https://github.com/mtl-brainhack-school-2019/EmanueleB/blob/master/screenshots/flow%20chart.JPG)

## The starting point is represented by the first analysis performed by the program Tony, which extracts the notes from any single musical performance 

![](https://github.com/mtl-brainhack-school-2019/EmanueleB/blob/master/screenshots/c3.JPG)

## Every note is defined by 3 types of information: time, frequency and duration. The program generates a compressed file for each performance, as well as two .txt files for each performance. Once obtained, all the data of the entire list of performances for each participant need to be cleaned, organized and concatenated. 

![](https://github.com/mtl-brainhack-school-2019/EmanueleB/blob/master/screenshots/Unorganized%20data.JPG)

## After the application of the first script, I was able to automate entirely the process of cleaning, organization and concatenation of all the files needed (note.txt) for each performance, applying this to each participant.  The end result is a list of .csv files (for each participant):

![](https://github.com/mtl-brainhack-school-2019/EmanueleB/blob/master/screenshots/Notes_Frequency_Duration_Time_First%20Step.JPG)

### Each single .csv file displays the following information

![](https://github.com/mtl-brainhack-school-2019/EmanueleB/blob/master/screenshots/P002_example.JPG)

## In addition, the previous script was enhanced adding lines with the purpose to further summarise the data for each participant, performing two basic analyses: 
### 1 - the average of the frequency range per song
### 2 - the total number of notes per song

![](https://github.com/mtl-brainhack-school-2019/EmanueleB/blob/master/screenshots/P002_second%20analysis.JPG)

## Once the data have been cleaned and organized, I performed some basic visualizations, using bar graphs. 

![](https://github.com/mtl-brainhack-school-2019/EmanueleB/blob/master/graphs/graph1.png)

![](https://github.com/mtl-brainhack-school-2019/EmanueleB/blob/master/graphs/graph2.png)

![](https://github.com/mtl-brainhack-school-2019/EmanueleB/blob/master/graphs/graph3.png)

![](https://github.com/mtl-brainhack-school-2019/EmanueleB/blob/master/graphs/graph4.png)

## I prepered the code for the t-test that would be applied to all the participants once the all data is acquired.
![](https://github.com/mtl-brainhack-school-2019/EmanueleB/blob/master/graphs/ttest_result.png)

## I applied a machine learning technique: training and testing. 
### The training phase uses the 20% of the data to develop a model
### The testing phase applies the model developed to the remaining 80% of the data

![](https://github.com/mtl-brainhack-school-2019/EmanueleB/blob/master/graphs/training_testing_results.png)
![](https://github.com/mtl-brainhack-school-2019/EmanueleB/blob/master/graphs/training_testing_graph.png)



## Project definition (about 200 words) What were you trying to accomplish, what was your question. This section may include a link to the presentation done during week 3.

## Learning experience (about 200 words) Describe how the project actually happened. In particular, which tools, data and technologies were learned. This section should include paragraphs that you may have already written during week 2 (but it doesn't have to).

### Use of open-science best practices
-GitHub
-Pytho
-Visual Studio Code


### Skills and technologies learnt
-Data extraction
-Graphs
-Machine learning 
-Basic stats


## Results (about 200 words) The deliverables of your project, including but not limited to notebooks, code, figures, etc.
