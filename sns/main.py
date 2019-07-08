import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
tips = sns.load_dataset('tips')
dots = sns.load_dataset('dots')

sns.set()
sns.relplot(x="time", y="firing_rate", col="align",
            hue="choice", size="coherence", style="choice",
            facet_kws=dict(sharex=False),
            kind="line" , legend='full', data=dots)
plt.show()