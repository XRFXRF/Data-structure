import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
x=[0.93,0.328]
y=[9.3,9]
fig=plt.figure(figsize=(4,4))
ax=plt.subplot(111)
plt.plot(x,y)
plt.scatter(x,y)
plt.plot((0.93,0.93),(-11,11))
plt.plot((0.328,0.328),(-11,11))
plt.text(0.95,9.4,'KNO3')
plt.text(0.31,9.3,'MgCl2 ')
plt.xlim(0,1)
plt.ylim(-10,10)
plt.xlabel(r'Aw')
plt.ylabel('质量增减数mg',fontproperties='SimSun')
ax.spines['bottom'].set_position(('data', 0))
sns.despine(top=True,right=True)
plt.show()
