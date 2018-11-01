
import matplotlib.pyplot as plt
import seaborn as sns


class GridPlotter():

    def __init__(self):
        pass

    def plotHeatmap(self, map):



        sns.heatmap(map, annot=True, linewidths=.5, cmap="YlGnBu")


        plt.show()