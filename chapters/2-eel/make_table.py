#!/usr/bin/env python3

import pandas as pd
import numpy as np

scores = [[0.687, 0.963, 0.974, 0.976], [0.551, 0.428, 0.482, 0.592],
          [0.687, 0.963, 0.974, 0.976], [0.223, 0.239, 0.431, 0.631],
          [0.346, 0.949, 0.959, 0.985], [0.239, 0.711, 0.725, 0.851],
          [0.687, 0.963, 0.974, 0.976], [0.506, 0.367, 0.494, 0.665]]

scores = np.array(scores)
# scores = np.concatenate((scores, np.zeros(scores.shape[0])[..., None]), axis=1)

datasets = ['Brain', 'Cochlea', 'Tweezer', 'Slitlamp']
method = ['Vilarino et al. \cite{vilarino07}', 'Probability Est.', 'EL', 'EEL']
metrics = ['AUC', 'F1']

index = pd.MultiIndex.from_product([datasets, metrics],
                                   names=['Type', 'Metric'])
# columns = pd.MultiIndex.from_product([method], names=['Method'])
columns = method
df = pd.DataFrame(scores, index=index, columns=columns)


# add bold tags
def myformat(r):
    idx = r.values.argmax()

    r.iloc[:, idx] = '$\\bm{' + r.iloc[:, idx].apply(str) + '}$'

    return r


df = df.groupby(['Type', 'Metric']).apply(myformat)

caption = "Area Under the Curve (AUC) and performances for each approach on each dataset. Highlight maximum values in bold."

out_path = 'results.tex'
print('writing table to {}'.format(out_path))
table = df.to_latex(
    escape=False,
    # column_format='llp{1.8cm}',
    multirow=True,
    caption=caption,
    label='tab:results')

# add horiz line below ours
with open(out_path, 'w') as tf:
    for line in table.splitlines():
        # if line.startswith('KSPTrack/GMM'):
        #     line += '\n\hdashline'
        tf.write(line + '\n')
