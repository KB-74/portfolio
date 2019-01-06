import time

import cv2
import matplotlib.pyplot as plt
import numpy as np
import ship
from PIL import Image

# inladen van de image en vertalen naar een array van rgb waardes


# base parameters voor het algoritme
Y_POS = 240
X_START = 400
SAMPLE_SIZE = 10
MAX_UPPER_BOUNDARY = 100
MAX_UPPER_COLOR_BOUNDARY = 160
START_RADIUS = 600
X_COEFF = 1
Y_COEFF = 1 / 1.8
CLEAN_STD_COEFF = 2
INTERVAL_COEFF = 0.005
MAX_DISTANCE_TO_NEIGHBOURS = 50


def detect_image():
    image = Image.open('../resources/boat_undistorted/camera_3/frame_6.jpg', 'r').convert('RGB')
    image_data = np.array(image.getdata()).reshape((image.height, image.width, 3))

    start_time = time.time()
    detector = ship.Detector()
    detector.set_frame(image_data)
    detector.detect()
    elapsed_time = time.time() - start_time
    print('elapsed time: {}'.format(elapsed_time))
    slope, intercept = detector.get_line()

    xi = np.arange(0, image.width)
    line = slope * xi + intercept
    # plt.plot(xi, line, linewidth=3, color='orange')


    # cleaned_data_points
    # plt.scatter(plt_bounds[0], plt_bounds[1], color='blue', s=25)
    start_points = detector.start_points
    start_points = start_points.transpose()
    # plt.plot(start_points[0], start_points[1], color='orange')
    plt.imshow(image_data)
    plt.show()
    plt.close()

    # plt.imshow(detector.heat_map)
    # plt.colorbar()
    # plt.show()
    # plt.close()


def video():
    INPUT_VIDEO = '/datc/shipping/Job/wall_detection/undistorted_cameradata/camera_3.mp4'
    OUTPUT_PATH = 'camera_3_wall.avi'

    cap = cv2.VideoCapture(INPUT_VIDEO)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (width, height))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    counter = 0

    detector = ship.Detector()

    while True:

        # read the frames
        has_next, frame = cap.read()

        if not has_next:
            break

        # fit a line
        detector.set_frame(frame)
        detector.detect()
        intercept, slope = detector.get_line()

        # A line
        try:
            if intercept and slope:
                cv2.line(frame, (0, int(slope)), (width, int(intercept * width + slope)), (0, 255, 0), 3)
                cv2.putText(frame, 'frame numer: {}'.format(counter), (20, 50), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0))
                cv2.putText(frame, 'slope: {:2.4f}'.format(intercept), (20, 90), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0))
                cv2.putText(frame, 'intercept: {:2.4f}'.format(slope), (20, 130), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0))
                cv2.putText(frame, 'valid point count: {}'.format(len(detector.boundaries)), (20, 170),
                            cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0))
        except:
            pass

        out.write(frame)
        print('frame: %i of %i (%f%%)' % (counter, frame_count, (counter / frame_count * 100)))
        counter = counter + 1

    out.release()
    cap.release()

def hsv_test():
    image = Image.open('../resources/boat_undistorted/camera_3/frame_8.jpg', 'r').convert('RGB')
    image_data = np.array(image.getdata()).reshape((image.height, image.width, 3))

    walker = ship.Walker(image_data)
    walker.walk(1000, 700, 10, 30)

    plt.show()
    plt.close()

if __name__ == '__main__':
    detect_image()
