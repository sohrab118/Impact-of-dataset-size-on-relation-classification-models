import matplotlib.pyplot as plt
import numpy as np

x = np.array([1/128, 1/64, 1/32, 1/16, 1/8, 1/4, 1/2, 1])

y1 = np.array([0.1608, 0.1894, 0.2697, 0.4008, 0.5657, 0.6606, 0.7433, 0.7907])



plt.plot(x, y1, marker = 'o', label ='R-BERT')

plt.xlabel("Training size")
plt.ylabel("F score")

# plt.axvline(x=0.25, linewidth=1.5, linestyle=":", color="green")
plt.axvline(x=0.50, linewidth=1.5, linestyle=":", color="green")
# plt.axvline(x=0.75, linewidth=1.5, linestyle=":", color="green")

# x_labels = ['1/128', '1/64', '1/32', '1/16', '1/8', '1/4', '1/2', '1']  

# plt.xticks(x, x_labels)  

plt.legend()
plt.show()

