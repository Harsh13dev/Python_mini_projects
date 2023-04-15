import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

'''Point Plot- only one parameter'''
# sns.distplot(tips['tip'])
# sns.rugplot(tips['total_bill'])
# sns.kdeplot(tips['tip'])

'''Distribution plots- two parameter'''
# sns.residplot(data=tips, x='total_bill', y='tip')
# sns.jointplot(data=tips, x='total_bill', y='tip', kind='hex ')

'''Pair plots- all possible combinations'''
dots = sns.load_dataset('dots')
# in dots file there are 3 parameters - time,coherence,firing_rate. therefore we will get 3x3 i.e 9 graphs

# sns.pairplot(dots)                        # same colour
# sns.pairplot(dots, hue='choice')            # T1 and T2 are separated with 2 different colours

'''Categorial plots- '''
sns.countplot(data=tips, x='day')           # How many times a particular day is repeated



plt.show()
