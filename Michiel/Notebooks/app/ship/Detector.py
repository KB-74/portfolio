import math

import numpy as np
from scipy.stats import stats
import matplotlib.pyplot as plt

from .Walker import Walker


class Detector:
    height: int
    width: int
    clean_std_coeff: int
    max_upper_boundary: int
    boundaries: np.ndarray
    frame: np.ndarray

    def __init__(self, sample_size=8, max_upper_boundary=100, clean_std_coeff=1):
        self.sample_size = sample_size
        self.max_upper_boundary = max_upper_boundary
        self.clean_std_coeff = clean_std_coeff
        self.frame = None
        self.width = 0
        self.height = 0
        self.start_points = []
        self.walkers = []
        self.heat_map_devider = 50
        self.filterd_points = []


    def set_frame(self, frame):
        self.frame = frame
        self.width = frame.shape[1]
        self.height = frame.shape[0]
        self.set_starting_points()

    def set_starting_points(self):
        start_x = [i for i in range(0, self.width, math.ceil(self.width / 50))]
        start_y = [i for i in range(600, 800, math.ceil((800 - 600) / 50))]
        self.start_points = np.array(list(zip(start_x, start_y)))

    def get_line(self):
        try:
            slope, intercept, _, _, _ = stats.linregress(self.filterd_points)
            return slope, intercept
        except:
            return None, None

    def detect(self):
        for i in self.start_points:
            fr = self.frame
            for j in range(-15, 15, 6):
                walker = Walker(fr, i[0], i[1], j, 10)
                walker.walk()
                if walker.found_boundary:
                    # plt.scatter(walker.found_boundary[0], walker.found_boundary[1], c='red', s=15)
                    self.walkers.append(walker)
        self.generate_heat_map()
        self.clean_outliers_with_heat_map()

    def distance_2d(self, a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    def distance_line2point(self, pnt, slope, intercept):
        pnt = np.array(pnt)
        x0 = pnt[0]
        y0 = pnt[1]
        a = slope
        c = intercept
        b = -1
        return abs(a * x0 + b * y0 + c) / ((a ** 2 + b ** 2) ** 0.5)

    def remove_outliers(self, slope, intercept):
        points_distance = []
        for n in range(len(self.boundaries)):
            points_distance.append(self.distance_line2point(self.boundaries[n], slope, intercept))
        points_distance_std = np.std(points_distance)
        # assert self.boundaries
        assert type(self.boundaries) is np.ndarray
        self.boundaries = self.boundaries[points_distance <= self.clean_std_coeff * points_distance_std]

    def clean_outliers(self):
        # slope, intercept, r_value, p_value, std_err
        for i in range(1):
            slope, intercept, _, _, _ = stats.linregress(self.boundaries)
            self.remove_outliers(slope, intercept)

    def sort_bounaries(self):
        self.boundaries = sorted(self.boundaries, key=lambda x: x[0])

    def generate_heat_map(self):
        self.heat_map = np.zeros([math.ceil(self.height / self.heat_map_devider), math.ceil(self.width / self.heat_map_devider)])
        for walker in self.walkers:
            boundary = walker.found_boundary
            self.heat_map[math.floor(boundary[1] / self.heat_map_devider), math.floor(boundary[0] / self.heat_map_devider) - 1] += 1
        # plt.imshow(self.heat_map)
        # plt.colorbar()

    def clean_outliers_with_heat_map(self):
        for walker in self.walkers:
            evaluation = walker.evaluate(self.heat_map, self.heat_map_devider)
            if evaluation:
                self.filterd_points.append(walker.found_boundary)
                plt.scatter(walker.found_boundary[0], walker.found_boundary[1], c='cyan', s=15)
