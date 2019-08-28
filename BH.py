import pandas
import glob
import os

# PARTICIPANTS WHO DO NOT HAVE NOTE FILES TXT
# P001
# P007
# P008
# P009
# P010
# P012

# focus on participants  ['02', '04', '05', '11', '13', '14', '15', '16', '17','19', '20'] 

list_of_participants =  ['02', '04', '05', '11', '13', '14', '15', '16', '17','19', '20']       # list of strings

for participant in list_of_participants: # for loop to change folders

    # method that finds files that match a specified string (the string in orange)
    
    filenames = glob.glob(r'\Users\Emanuele\Desktop\UdeM\PhD\Study 1 - improvisation and amusia\NEW_STUDY_Singing_Improvisation_participants\DATA\Singing\P0' + participant + '*\*_note.txt')
   
    arrays = []  # initializing the array

    numNotes = [] # Initializing empty list for the number of notes per song
    songsArray = [] # Initializing empty list for the codes for all the songs
    freqArray = [] # Initializing empty list for the frequency range

    for fname in filenames:                                     # This for loop reads one by one the notes files for a participant
        head, tail = os.path.split(fname)                       # This function splits the two parts identified: head & tail. Tail = anything that follows the last "\", which means the file name
                                                                # Example of a tail is: P004_AS2_track.txt
        participantID, song, extension = tail.split('_')        # This function splits the the file name (e.g. P004_AS2_track.txt) into 3 parts (identified by the "_"), such as P004, AS2, track.txt
                                                                # The parts split are stored into the variables: participantID, song, extension

        data = pandas.read_csv(fname,delimiter='\t', header=None)   # Pandas is taking the content from the .txt files and storing it into the variable "data"
        data.insert(0,'Song', song)                                 # A column is generated, named "Song", associating the variable string song to it
        arrays.append(data)                                         # The data is added to a list containing the data from all the note files
        
        numNotes.append( len(data.index))                           # Counts number of notes for each song (by counting the number of rows of each song file ) and adds it to a list
        songsArray.append(song)                                     # Adds the song IDs to a list
        freqArray.append(data[1].max()-data[1].min())               # Adds the range of frequencies to a list 

        
    newdf =  pandas.DataFrame(list(zip(songsArray, numNotes, freqArray)), columns =['Song', 'Number of Notes', 'Frequency Range']) # Creates a DataFrame from the songsID list, number of notes list and range freq list
    
    newdf.to_csv(r'\Users\Emanuele\Desktop\UdeM\PhD\BrainHack\data_analysis\P0' + participant +'.csv')  # Saves the DataFrame as a .csv
    

    df = pandas.concat(arrays)                   # Organizing the list under specific axes. By alligning the data, pandas transforms the list into a data frame          
    
    df.columns= [ 'Song', 'Time', 'Frequency', 'Duration']   # Assigning specific names to the columns

    #df.to_csv(r'\Users\Emanuele\Desktop\UdeM\PhD\BrainHack\List of extracted csv\P0' + participant +'.csv') # Puts the data frame into a csv newly generated 