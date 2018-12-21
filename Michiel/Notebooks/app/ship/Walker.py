import math

import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt

class Walker:
    def __init__(self, frame, x_start, y_start, delta_x, delta_y, sample_size=8, max_upper_boundary=.35,
                 max_upper_color=.5):
        self.sample_size = sample_size
        self.max_upper_color = max_upper_color
        self.max_upper_boundary = max_upper_boundary
        self.x_start = x_start
        self.y_start = y_start
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.width = frame.shape[1]
        self.height = frame.shape[0]
        self.frame = frame
        self.found_boundary = None

    def get_frame_window_points(self, x, y, size):
        start_x = max(int(y - size / 2), 0)
        start_y = max(int(x - size / 2), 0)
        end_x = min(int(y + size / 2), self.width)
        end_y = min(int(x + size / 2), self.width)
        return start_x, start_y, end_x, end_y

    def get_average(self, x, y):
        start_x, start_y, end_x, end_y = self.get_frame_window_points(x, y, self.sample_size)
        samples = self.frame[start_x:end_x, start_y:end_y]
        sample_stream = samples.transpose(2, 0, 1).reshape(3, -1)
        return np.mean(sample_stream, axis=1)

    def walk(self):
        # aan het begin is er nog geen scheiding tussen water en land
        baseline = self.get_average(self.x_start, self.y_start)

        x_pos = self.x_start
        y_pos = self.y_start

        plot_counter = 1

        # zolang er geen scheiding tussen water en land is loop de walker verder
        while not self.found_boundary:
            # bereken de huidige x positie
            # door de begin x bij de uitkomst van
            # het product met de richtingscooficient
            x_pos = x_pos + self.delta_x
            y_pos = y_pos - self.delta_y

            # plt.scatter(x_pos, y_pos, c='green', s=5)

            # als de walker buiten de image valt break uit de while loop
            if x_pos > self.width or x_pos < 0 or y_pos < 0 or y_pos > self.height:
                break

            # bereken de euclidean distance
            average = self.get_average(x_pos, y_pos)
            average = average / 255
            baseline = baseline / 255
            euclidean_distance = distance.euclidean(average, baseline)

            # als de euclidean distance groter is dan de voraf gezette boundary
            # word boundary gezet en stopt de loop bij de volgende iteratie
            if euclidean_distance > self.max_upper_boundary and np.all(average < self.max_upper_color):
                self.found_boundary = [x_pos, y_pos]
                plt.scatter(x_pos, y_pos, c='red', s=15)

            # gebruik de vorige baseline voor de volgende iteratie
            baseline = self.get_average(x_pos, y_pos)

    def evaluate(self, heatmap, frame_divider):
        if self.found_boundary:
            found_boundary_index = [math.floor(self.found_boundary[1] / frame_divider),
                                    math.floor(self.found_boundary[0] / frame_divider)]
            max_width = heatmap.shape[1]
            max_height = heatmap.shape[0]
            evidence = []
            x_pos = self.x_start / frame_divider
            y_pos = self.y_start / frame_divider
            while True:

                if x_pos > max_width - 1 or x_pos < 0 or y_pos < 0 or y_pos > max_height - 1:
                    break

                # plt.scatter(x_pos, y_pos, c='magenta')

                count = heatmap[math.floor(y_pos), math.floor(y_pos)]
                if count > 0:
                    evidence.append({
                        'x': math.floor(x_pos),
                        'y': math.floor(y_pos),
                        'found_points': count
                    })
                x_pos = x_pos + self.delta_x / frame_divider
                y_pos = y_pos - self.delta_y / frame_divider

            maximum = {'found_points': 0, 'x': 0, 'y': 0}
            for e in evidence:
                if e['found_points'] > maximum['found_points']:
                    maximum = e

            return found_boundary_index[0] == maximum['y'] and found_boundary_index[1] == maximum['x']
