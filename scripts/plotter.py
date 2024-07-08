import pandas as pd
import matplotlib.pyplot as plt
import os

class Plotter:
    def __init__(self, json_file):
        self.df = pd.read_json(json_file)
        if not os.path.exists('plots'):
            os.makedirs('plots')

    def draw_plots(self):
        plots_paths = []

        _, ax = plt.subplots()
        self.df.plot(x='gt_corners', y='rb_corners', kind='scatter', ax=ax)
        plot_path = os.path.join('plots', 'gt_vs_rb_corners.png')
        plt.title('Ground Truth Corners vs Predicted Corners')
        plt.savefig(plot_path)
        plots_paths.append(plot_path)
        plt.close()

        _, ax = plt.subplots()
        self.df['mean'].plot(kind='hist', ax=ax)
        plot_path = os.path.join('plots', 'mean_deviation.png')
        plt.title('Histogram of Mean Deviation')
        plt.savefig(plot_path)
        plots_paths.append(plot_path)
        plt.close()

        _, ax = plt.subplots()
        self.df['max'].plot(kind='hist', ax=ax)
        plot_path = os.path.join('plots', 'max_deviation.png')
        plt.title('Histogram of Max Deviation')
        plt.savefig(plot_path)
        plots_paths.append(plot_path)
        plt.close()

        _, ax = plt.subplots()
        self.df['min'].plot(kind='hist', ax=ax)
        plot_path = os.path.join('plots', 'min_deviation.png')
        plt.title('Histogram of Min Deviation')
        plt.savefig(plot_path)
        plots_paths.append(plot_path)
        plt.close()

        return plots_paths
