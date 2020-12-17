import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from matplotlib import colors
import sys, getopt, os
import csv
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

def main(argv):
#    datasets = list()
    reports = ['_allMetrics_ds11_rec.csv','_allMetrics_ds11_rec_maxfeat.csv']
#    reports = ['_allMetrics_ds01_prob.csv','_allMetrics_ds09_prob.csv','_allMetrics_ds11_prob.csv','_allMetrics_ds12_prob.csv']
    dataset_labels = [r'CT Inner Ear A ($m=\sqrt{p}$)',r'CT Inner Ear A ($m=p$)']
    ofile = 'f1_vs_training_rec_maxfeat.pdf'
#    title = None
#    ofile = None
#    try:
#        opts, args = getopt.getopt(argv,"hd:r:",["dataset=","reports=","ofile=","title="])
#    except getopt.GetoptError:
#        print('eval_reprod.py -d <01-Surgical_Video,09-MRI_Brain> -r <bow-000-009,bow-000-009> --ofile=out_file.png --title=mytitle')
#        sys.exit(2)
#    for opt, arg in opts:
#        if opt == '-h':
#            print('eval_reprod.py -d <01-Surgical_Video,09-MRI_Brain> -r <bow-000-009,bow-000-009> --ofile=out_file.png --title=mytitle')
#            sys.exit()
#        elif opt in ("-d", "--dataset"):
#            tmp = arg.split(',')
#            for i, ds in enumerate(tmp):
#                datasets.append(list())
#                tmp2 = ds.rsplit('-')
#                datasets[i] = [tmp2[0], tmp2[-1].replace('_',' ')]
#        elif opt in ("-r", "--reports"):
#            tmp = arg.split(',')
#            for i, rep in enumerate(tmp):
#                reports.append(list())
#                tmp2 = rep.rsplit('-')
#                reports[i] = [tmp2[0], tmp2[1], tmp2[-1]]
#        elif opt in ("--title"):
#            title = arg.replace('_',' ')
#        elif opt in ("--ofile"):
#            ofile = arg
#        else:
#            assert False, "unhandled option"

#    # if only one report numbers specified, take for all the same
#    if len(reports) == 1:
#        for i in range(len(datasets) - 1):
#            reports.append(reports[0])

    from collections import OrderedDict
    data_fscore = OrderedDict()
    for i_rep, rep in enumerate(reports):
        print('load csv: %s' % rep)

        with open(rep, 'rt') as csvfile:
            numreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            rep_idx = None
            fscore_idx = None
            data_fscore['%s' % rep] = list()
            for row in numreader:
                try:
                    fscore_idx = row.index('f1_score_max')
                except ValueError:
                    data_fscore['%s' % rep].append(float(row[fscore_idx]))
                    # print('fscore: %f' % float(row[fscore_idx]))

    data_fscore_mean = dict()
    data_fscore_std = dict()
    for i_rep, rep in enumerate(reports):
        my_f1_array = np.asarray(data_fscore['%s' % rep])
        data_fscore_mean['%s' % rep] = np.zeros(len(my_f1_array) // 10)
        data_fscore_std['%s' % rep] = np.zeros(len(my_f1_array) // 10)
        for i in range(len(my_f1_array) // 10):
            data_fscore_mean['%s' % rep][i] = np.mean(my_f1_array[(i*10):((i+1)*10)])
            data_fscore_std['%s' % rep][i] = np.std(my_f1_array[(i*10):((i+1)*10)])
            print('mean: %f, std: %f' % (float(data_fscore_mean['%s' % rep][i]), float(data_fscore_std['%s' % rep][i])))
    
    colors = ['r', 'c']
    markers = ['*', '>', '<', '^', 'v', 'p', '*', 'h']
    
    epoch_list = np.array([1,11,21,31,41,51,61,71,81,91])

#    epoch_list = np.array([1])
    plt.figure(figsize=(6,3))
    for i_rep, rep in enumerate(reports):
#        if i_rep < len(epoch_list):
            plt.plot(epoch_list, data_fscore_mean['%s' % rep], ms=5, lw=0, clip_on=False,
                     color=colors[i_rep % len(colors)],
                     marker=markers[i_rep % len(markers)],
                     label=r'%s' % dataset_labels[i_rep])
            plt.plot(epoch_list, data_fscore_mean['%s' % rep], marker=None, lw=1,
                     color=colors[i_rep % len(colors)])

#        plt.xlim([(1.0-pr_win), 1.0])
#        plt.ylim([(1.0-pr_win), 1.0])
    plt.xlabel(r'\textbf{Epoch}', fontsize=12)
    plt.ylabel(r'\textbf{Mean \textit{max F1-Score}}', fontsize=12)
#    plt.legend(bbox_to_anchor=(0,-0.15), loc="upper left", frameon=False)
    plt.legend(bbox_to_anchor=(1.0,1.0), loc="upper left", frameon=False)
    plt.grid()
    plt.savefig(ofile, bbox_inches="tight")
    plt.show()
    
#        plt.xticks(fontsize=fs_ax_ticks)
#        plt.yticks(fontsize=fs_ax_ticks)
        
#    data = np.array([val for (_, val) in data_fscore.items()]).transpose()
#    key_list = list(data_fscore.keys())

#    alpha = 0.1

#    # basic plot
#    plt.boxplot(data, sym='k.')

#    if title != None:
#        plt.title(r'\textbf{%s}' % title, fontsize=16)
#    plt.xticks(np.arange(1, len(key_list)+1), key_list, rotation='vertical', fontsize=10)
#    plt.yticks(fontsize=9)

#    for i in range(data.shape[1]):
#        plt.scatter(np.ones(data.shape[0])*(i+1) + np.random.uniform(-alpha, alpha, data.shape[0]), data[:,i],
#                    label=key_list[i], marker='.', s=3, color=colors.cnames['dimgrey'])

#    # get means
#    means = list()
#    for i in range(data.shape[1]):
#        means.append(np.mean(data[:,i]))
#    # get ranks
#    ranks = list(reversed([i[0] for i in sorted(enumerate(means), key=lambda x: x[1])]))

#    t = PrettyTable(['Dataset', 'Mean', 'Median', 'Std', 'Rank', 'Support'])

#    for i in range(data.shape[1]):
#        t.add_row([key_list[i], '%.4f' % means[i], '%.4f' % np.median(data[:,i]), '%.3e' % np.std(data[:,i]), '%i' % (ranks.index(i)+1), data.shape[0]])
#    print(t)

#    # plt.legend(loc='best')
#    plt.grid()
#    plt.ylabel(r'\textbf{max F1-score}', fontsize=12)

#    if ofile == None:
#        plt.subplots_adjust(bottom=0.4)
#        plt.show()
#    else:
#        plt.savefig(ofile, bbox_inches="tight")

if __name__ == "__main__":
   main(sys.argv[1:])

