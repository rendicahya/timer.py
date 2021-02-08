from time import perf_counter
from time import sleep

from print_color import print as print_color


class Timer:
    def __init__(self, label='timer.py', format='%02d:%02d:%02d.%s', ms_digits=3, color='green'):
        self.label = label
        self.start_time = None
        self.format = format
        self.ms_digits = ms_digits
        self.color = color

    def start(self):
        self.start_time = perf_counter()

    def get_elapsed(self):
        return perf_counter() - self.start_time

    def stop(self):
        if self.start_time is None:
            print_color('Timer not started', tag=self.label, tag_color='red', color='white')
        else:
            stop_time = perf_counter()
            elapsed = stop_time - self.start_time
            self.start_time = None

            print_color(self.format_time(elapsed), tag=self.label, tag_color=self.color, color='white')

    def format_time(self, time):
        hour = time // 3600
        min = time % 3600 // 60
        sec = time % 60
        ms = str(time % 1)[2:self.ms_digits + 2]

        return self.format % (hour, min, sec, ms)


if __name__ == '__main__':
    t = Timer('test')
    # t.start()
    sleep(1)
    t.stop()
