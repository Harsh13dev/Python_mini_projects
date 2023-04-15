import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 10, 20)
y = x * x
z = x + y
print(x, '\n', y, '\n', z)

plt.plot(y, x)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Test Graph')
plt.show()

# plt.subplot(2, 2, 1)
# plt.plot(x,x)
# plt.subplot(2, 2, 2)
# plt.plot(x,y)
# plt.subplot(2, 2, 3)
# plt.plot(y,y)
# plt.subplot(2, 2, 4)
# plt.plot(y,x)

# plt.subplot(3, 2, 1)
# plt.plot(x,y)                 - line graph
# plt.subplot(3, 2, 2)
# plt.scatter(x,y)              - dotted line graph
# plt.subplot(3, 2, 3)
# plt.hist(x,y)                 - histogram graph
# plt.subplot(3, 2, 4)
# plt.bar(x,y)                  - bar graph
# plt.subplot(3, 2, 5)
# plt.fill(x,y)                 - fill graph

# plt.plot(x, y, label='first line')
# plt.legend(loc=1)
'''legend is like index. we can give a particular label 
   or name to different color lines. 
   there are 10 locations from 1-10 '''
# --------------------------------------------------------------------
'Object oriented plots'
# fig = plt.figure()
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes.plot(x, y)

'subplots using object oriented'
# fig, axes = plt.subplots(1,2)
# axes[0].plot(x,y)
# axes[1].plot(y,x)
# plt.tight_layout()
# plt.show()

'Figure size'
# fig = plt.figure(figsize=(5,6))
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

'Labels'
# axes.set_xlabel('x-axis')
# axes.set_ylabel('y-axis')
# axes.set_title('The graph')
# plt.show()

'Stylling plots'
# axes.plot(x, y, color='red', linewidth=5, alpha=0.5, linestyle='-.')
# axes.plot(x, y, marker='o', markersize=5, markerfacecolor='red')                        # 2 types - 1 or o

'Setting limit'
# axes.set_xlim((0,6))
# axes.set_ylim((0,50))
# axes.plot(x,y)

# plt.show()