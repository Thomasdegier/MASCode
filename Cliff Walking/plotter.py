
import matplotlib.pyplot as plt
from matplotlib.text import Text
import seaborn as sns
import numpy as np


class GridPlotter():

    def __init__(self):
        pass

    def plotHeatmap_V(self, map):

        sns.heatmap(map, annot=True, linewidths=.5, cmap="YlGnBu")
        plt.show()


    def plotHeatmap_Q(self, map):

        flatter = []
        highest_Q = []

        for y in map:
            for x in y:
                flatter.append(x)
                highest_Q.append(max(x))

        highest_Q = np.array(highest_Q).reshape(np.array(map).shape[:2])

        plt.figure(figsize=(15,15))

        heatmap = sns.heatmap(highest_Q, annot=True, linewidths=.5, cmap="YlGnBu")

        for i, elem in enumerate(heatmap.texts):

            q_values = flatter[i]

            text = "u:{}\nr:{}\nd:{}\nl{}".format(q_values[0], q_values[1], q_values[2], q_values[3])

            elem.set_text(text)

        plt.show()