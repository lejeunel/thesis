import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

dataset_nbr = '11_prob'

xx = list()
mse = list()
mse_val = list()

print('reading 1....')
with open('log_ds' + dataset_nbr + '.csv', 'rt') as csvfile:
    csv_reader = csv.reader(filter(lambda row: row[0] != '#', csvfile), delimiter=';', quotechar='|')
    for (i, row) in enumerate(csv_reader):
        if i > 0:
            xx.append(float(row[0]))
            mse.append(float(row[2]))
            mse_val.append(float(row[8]))

print('plotting....')
plt.figure(figsize=(8, 2))
plt.plot(xx, mse, 'k')
plt.plot(xx, mse_val, 'r')
plt.grid()
plt.xlabel(r'\textbf{Epochs}', fontsize=12)
plt.ylabel(r'\textbf{Loss}', fontsize=12)
plt.legend([r'BCE Training Loss',r'BCE Validation Loss'])

plt.savefig('learning_curve_ds' + dataset_nbr + '.pdf', bbox_inches="tight")
plt.show()

