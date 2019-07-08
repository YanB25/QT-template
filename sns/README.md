# sns examples
this directory show examples for seaborn
## prerequisis
``` python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
tips = sns.load_dataset('tips')
dots = sns.load_dataset('dots')

sns.set()
```
## relplot drawing
在relplot中，x和y都必须是数值的。无论是打点还是连线，都必须同时提供x和y，x和y的位置一一对应，成为$(x_i, y_i)$对，然后再画图。
### dots
``` python
sns.relplot(x="total_bill", y="tip", col="time",
            hue="smoker", style="smoker", size="size",
            data=tips)
```
### line
``` python
sns.relplot(x="time", y="firing_rate", col="align",
            hue="choice", size="coherence", style="choice",
            facet_kws=dict(sharex=False),
            kind="line" , legend='full', data=dots)
plt.show()
```

## catplot
在catplot中，x或者y不需要是数值类型的，只需要是有限集中的元素。例如x可以是`['Thur', 'Fri', 'Sat', 'Sun']`集合的元素。

下列的两段代码，视觉效果不同

``` python
sns.catplot(x="day", y="total_bill", hue="smoker", kind="swarm", data=tips)
```

``` python
sns.catplot(x="day", y="total_bill", hue="smoker", kind="violin", split=True, data=tips)
```
注意：下面这行代码不是一般意义上的bar。它展示的是mean value和confidence interval

``` python
sns.catplot(x="day", y="total_bill", hue="smoker", kind="bar", data=tips)
```