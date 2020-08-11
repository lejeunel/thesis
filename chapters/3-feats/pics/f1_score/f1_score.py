import pickle
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

with open('data.pkl', 'rb') as f:
    data = pickle.load(f)
    pr_x = data['mean']['pr_curve']['rec']
    pr_y = data['mean']['pr_curve']['pre']

f1_score = 2 * (np.multiply(pr_x, pr_y)) / (pr_x + pr_y)

idx_max = np.argmax(f1_score)

plt.subplots(figsize=(8, 2))
plt.subplot(121)
plt.plot(pr_x, pr_y, 'k')
plt.plot(pr_x[idx_max], pr_y[idx_max], 'go')
plt.grid()
plt.xlabel(r'\textbf{Recall}', fontsize=12)
plt.ylabel(r'\textbf{Precision}', fontsize=12)

plt.subplot(122)
plt.plot(pr_x,f1_score, 'k')
plt.plot(pr_x[idx_max], f1_score[idx_max], 'go')
plt.grid()
plt.xlabel(r'\textbf{Recall}', fontsize=11)
plt.ylabel(r'\textbf{F1-Score}', fontsize=11)

plt.subplots_adjust(wspace=0.4)

plt.savefig('f1_score.pdf', bbox_inches="tight")
plt.show()

