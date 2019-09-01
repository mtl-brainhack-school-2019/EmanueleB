#EMANUELE BLASIOLI
# FINAL REPORT

#EMANUELE BLASIOLI
# FINAL REPORT

## High-level summary of the project (about 50 words)
My project focuses on investigating statistical properties of sung performances in a population of subjects affected by a congenital condition known as congenital amusia (experimental group), as well as in a population of healthy individuals (control group).  Considering the current state of my project (data collection phase). The main priority, for me, refers to learning how to program in python in order to manipulate a growing dataset by automating a series of critical operations (data cleaning, data organization, data analysis). 


## Project definition (about 200 words) 
The main question that guided my effort refers to the possibility to create a program with the aim to completely automate a sequence of operations (data cleaning, re-organization, analysis, visualization). Achieving this general goal might be very important at this stage, since it would allow me (and my lab) to save a significant amount of time as well as manual work, consequently reducing the probability that human mistakes due to the data manipulation might occur. 
In particular, I tried to accomplish the following main tasks
-	Being able to concatenate several files per participant, each one containing detailed information (frequency, duration and time) of each musical performance, into a single file. 
-	Reorganization of the single file created, enhancing clarity and logical structure of the components 
-	Assembling various information that derive from different musical characteristics of the performances into a single file per participant, 
-	Create the backbone of some analytical processes, deriving from some machine learning techniques (such as the creation of a predictive model based on the training-testing methodology), that will be applied later one once the data collection is complete
-	Create scripts to display visually (through graphs) basic information describing the main characteristics of the behavioural data collected. 
The intent is to achieve all the steps mentioned above by creating scripts with a single language (python), easily understandable by the other members of the lab, also easy to adapt to new data acquired and easy to update. 


## Learning experience (about 200 words) 
I began this project without any previous exposure to python. Therefore, I used a proactive approach to interact with the members of the workshop, asking for technical support and feedback. 
Since the beginning of week 2, I immediately identified what libraries in python would have represented a good fit for my goals (such as pandas, matplotlib, scipy, sklearn). By the end of week 2 I became familiar with these libraries and during week 3 I learned how to use these libraries, utilizing the data that I currently have in my main dataset. Given my priorities, related to learn as much as possible how to program in python and how to use tools and packages never used before, I decided to concentrate most of my efforts to learn how to code and how to find the retrieve the information I need online (for example searching on “stack overflow”). I learned that knowing how to find the right information it’s probably even more important that know how to code, at least at this stage. 
Despite I initially used Jupyter notebook, during week 2, I decided to move to Visual Studio Code due to a more user-friendly interface. I found working with this platform easier and more effective. Moreover, an additional motivation that pushed to stay on VSCode relates to the fact that it can be used with other programming languages. 


## Results (about 200 words) The deliverables of your project, including but not limited to notebooks, code, figures, etc. 
The first script (BH.py) was created in order to clean, organize and concatenate data from .txt files outputted by the Tony program. The “pandas” library helped with creating a “DataFrame” structure containing information for each note reorganized and concatenated into one .csv file for each participant. This script was then enhanced by adding lines with the purpose of summarising the data for each participant further, such as calculating the average of the frequency range per song and the total number of notes per song. I once again used the “pandas” library, which allowed me to reorganize the data and use methods for “DataFrames” that simplified data manipulation (e.g., dataframe.max() and dataframe.min()). 
The second script (bar_graphs.py) was created in order to perform some basic visualizations in the form of bar graphs. I used the “matplotlib” library to graph simple bar plots and multi-bar plots. 
The third script (T-Test.py) was created in order to prepare a template for a t-test that would eventually be applied to all participants to compare amusic performance to non-amusic, once the data is acquired. I used the “scipy” library to compute the t-test and p-value.
The fourth and final script (scikitTest.py) was created in order to test the machine learning technique “training and testing” with the help of the “sklearn” library. The training phase uses 20% of the data to develop a model. The testing phase applies the model to the remaining 80% of the data. Of course, for now there is not enough data for this method to work as intended, but it is interesting to consider in the future.





