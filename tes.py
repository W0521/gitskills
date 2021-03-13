
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline
# %config InlineBackend.figure_format='svg'
plt.rcParams['savefig.dpi'] = 600
plt.rcParams['figure.dpi'] = 300

figsize=6,5
figure,ax=plt.subplots(figsize=figsize)

font2 = {'family':'Times New Roman',
'size':10.5,
}

RHATR_W = [0.9392,0.8788,0.7696,1.1535]
RHATR_R= [0.9389,0.8703,0.7584,1.1468]
RHATR=[0.9301,0.8673,0.7512,1.1324]
x = np.arange(4)

total_width, n = 0.8, 4   
width = total_width / n
x = x - (total_width - width) / 2

plt.bar(x,RHATR_W, color = "red",edgecolor = "k",width=width,hatch = "",label='RHATR_W ')
plt.bar(x + width, RHATR_R, color = "yellowgreen",edgecolor = "k",width=width, hatch = "",label='RHATR_R')
plt.bar(x + 2 * width, RHATR , color = "lightskyblue",edgecolor = "k",width=width, hatch = "",label='RHATR')
#plt.bar(x + 3 * width,Yelp_2017 , color = "lightcoral",edgecolor = "k",width=width, hatch = "\\",label='Yelp_2017',fomt2)
#plt.tick_params(labelsize=8.5)
#labels = ax.get_xticklabels() + ax.get_yticklabels()
#[label.set_fontname('Times New Roman') for label in labels]
plt.xlabel("DataSet",font2)
plt.ylabel("RMSE",font2)
plt.legend(loc = "best",prop=font2)
plt.xticks([0,1,2,3],['Amazon_Instant_Video','Toys_and_Games','Kindle_Store','Yelp_2017'])

plt.tick_params(labelsize=8.5)

labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

my_y_ticks = np.arange(0.7, 1.2, 0.05)
plt.ylim((0.7, 1.2))
plt.yticks(my_y_ticks)

plt.savefig('Figure3.png')
plt.show()