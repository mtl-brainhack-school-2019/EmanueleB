import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ['02', '04', '05', '11', '13', '14', '15', '16', '17','19', '20']    # list of strings

list_of_participants = ['02', '04', '05', '11', '13', '14', '15', '16', '17','19', '20'] 

totalNotes = []
freqAvrg = []

songList1 = [9, 16, 17, 18] # ['DAN', 'HEA', 'LOV', 'LUL']
df2 = pd.DataFrame(columns=['DAN', 'HEA', 'LOV', 'LUL'])
songList2 = [15, 20, 8, 21 ] # ['HAP2', 'SAD2', 'ASL', 'TSL']
df3 = pd.DataFrame(columns=['HAP2', 'SAD2', 'ASL', 'TSL'])

for participant in list_of_participants: # for loop to change folders

    df = pd.read_csv(r'\Users\Emanuele\Desktop\UdeM\PhD\BrainHack\data_analysis\P0' + participant + '.csv') 
    
    totalNotes.append(df['Number of Notes'].sum())
    freqAvrg.append(df['Frequency Range'].mean())

    df2 = df2.append(pd.DataFrame([df.loc[songList1, 'Number of Notes'].values], columns = df2.columns))
    df3 = df3.append(pd.DataFrame([df.loc[songList2, 'Number of Notes'].values], columns = df3.columns))

## Graph for Total Notes / participants
plt.figure()
y_pos = np.arange(len(list_of_participants))
plt.bar(y_pos, totalNotes, align='center', alpha=0.5)
plt.xticks(y_pos, list_of_participants)
plt.ylabel('Total Notes')
plt.xlabel('Participants')
plt.title('Total notes for all songs')
plt.savefig(r'C:\Users\Emanuele\Documents\GitHub\EmanueleB\graphs\graph1.png')

## Graph for Freq range Average / participants
plt.figure()
y_pos = np.arange(len(list_of_participants))
plt.bar(y_pos, freqAvrg, align='center', alpha=0.5, color='magenta')
plt.xticks(y_pos, list_of_participants)
plt.ylabel('Frequency Range Average (Hz)')
plt.xlabel('Participants')
plt.title('Frequency range average for all songs')
plt.savefig(r'C:\Users\Emanuele\Documents\GitHub\EmanueleB\graphs\graph2.png')
#plt.show()

##  Multi-bar graph FIRST SET OF SONGS ['DAN', 'HEA', 'LOV', 'LUL']
plt.figure()
# plot data
x =  np.arange(len(list_of_participants))
bar_width = 0.15
plt.bar(x, df2['DAN'], width=bar_width, color='blue', zorder= 2) #blue
plt.bar(x+bar_width, df2['HEA'], width=bar_width, color='green', zorder= 2) #green
plt.bar(x+bar_width*2, df2['LOV'], width=bar_width, color='red', zorder= 2) #red
plt.bar(x+bar_width*3, df2['LUL'], width=bar_width, color='purple', zorder= 2) #purple


# Labels
plt.xticks(x + bar_width*1.5, list_of_participants)
plt.ylabel('Total Notes')
plt.xlabel('Participants')
plt.title('Total notes per song per participant')

# Legend
green_patch = mpatches.Patch(color='blue', label = 'DAN') #blue
blue_patch = mpatches.Patch(color='green', label = 'HEA')  #green
red_patch = mpatches.Patch(color='red', label = 'LOV') #red
purple_patch = mpatches.Patch(color='purple', label = 'LUL') #purple
plt.legend(handles=[green_patch, blue_patch, red_patch, purple_patch ])

# Grid
plt.grid(axis='y')

#plt.show()
plt.savefig(r'C:\Users\Emanuele\Documents\GitHub\EmanueleB\graphs\graph3.png')

##  Multi-bar graph SECOND SET OF SONGS ['HAP2', 'SAD2', 'ASL', 'TSL']
plt.figure()
# plot data
x =  np.arange(len(list_of_participants))
bar_width = 0.15
plt.bar(x, df3['HAP2'], width=bar_width, color='orange', zorder= 2) 
plt.bar(x+bar_width, df3['SAD2'], width=bar_width, color='darkkhaki', zorder= 2) 
plt.bar(x+bar_width*2, df3['ASL'], width=bar_width, color='violet', zorder= 2) 
plt.bar(x+bar_width*3, df3['TSL'], width=bar_width, color='slategray', zorder= 2) 


# Labels
plt.xticks(x + bar_width*1.5, list_of_participants)
plt.ylabel('Total Notes')
plt.xlabel('Participants')
plt.title('Total notes per song per participant')

# Legend
orange_patch = mpatches.Patch(color='orange', label = 'HAP2') 
darkkhaki_patch = mpatches.Patch(color='darkkhaki', label = 'SAD2') 
violet_patch = mpatches.Patch(color='violet', label = 'ASL')
slategray_patch = mpatches.Patch(color='slategray', label = 'TSL') 
plt.legend(handles=[orange_patch, darkkhaki_patch, violet_patch, slategray_patch ])

# Grid
plt.grid(axis='y')

#plt.show()
plt.savefig(r'C:\Users\Emanuele\Documents\GitHub\EmanueleB\graphs\graph4.png')