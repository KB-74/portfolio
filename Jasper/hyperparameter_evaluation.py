import pandas as pd
import matplotlib.pyplot as plt


statistics = pd.read_csv('hyperparameter.csv', index_col=0)
mean_statistics = statistics[['parameter', 'value', 'tp', 'fp', 'fn', 'tn']].groupby(['parameter', 'value']).mean()

print(mean_statistics)


def f1_score(row):
    tp, tn, fp, fn = row.tp, row.tn, row.fp, row.fn
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1 = 2 * (precision * recall)/(precision+recall)
    return f1

parameters = ["max_upper_color","max_upper_distance_boundary","heat_map_devider", "edge_overlay_divider",
              "gaussian_blur_coeff","canny_edge_lower_coeff","canny_edge_upper_coeff"]

for i in parameters:
    sliced_stats = mean_statistics.loc[i]
    stats_f1_scores = {}
    for j in range(len(sliced_stats)):
        stats_f1_scores[j] = f1_score(sliced_stats.iloc[j])
    plt.plot(list(sliced_stats.index.values), stats_f1_scores.values())
    plt.xlabel('value')
    plt.ylabel('f1 score')
    plt.title(i)
    plt.grid(True)
    plt.show()
    plt.close()

plt.show()

canny_stats = mean_statistics.loc['canny_edge_lower_coeff']
canny_f1_scores = {}


for i in range(len(canny_stats)):
    canny_f1_scores[i] = f1_score(canny_stats.iloc[i])




#per parameter value tegenover f1 score
#x value, y f1
plt.plot(list(canny_stats.index.values), canny_f1_scores.values())
plt.show()
