from math import floor
from time import perf_counter

from print_color import print as print_color


class Timer:
    def __init__(self, label=None, format='%d:%d:%02d.%s', ms_digits=3, color='green'):
        self.label = label
        self.start_time = None
        self.format = format
        self.ms_digits = ms_digits
        self.color = color

    def start(self):
        self.start_time = perf_counter()

    def stop(self):
        time = perf_counter() - self.start_time
        hour = time // 3600
        min = time % 3600 // 60
        sec = floor(time % 60)
        ms = str(time % 1)[2:self.ms_digits + 2]
        time_str = self.format % (hour, min, sec, ms)

        print_color(time_str, tag=self.label, tag_color=self.color, color='white')
