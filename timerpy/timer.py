from time import perf_counter

from timerpy.printer import Printer
from timerpy.utils import format_time


class Timer:
    def __init__(self, tag='timer.py', format='%02d:%02d:%02d.%s', ms_digits=3, color='green'):
        self.time_data = []
        self.is_started = False
        self.start_time = None
        self.format = format
        self.ms_digits = ms_digits
        self.color = color
        self.print = Printer(tag)

    def start(self):
        if self.is_started:
            self.print.error('Timer already started')
        else:
            self.start_time = perf_counter()
            self.is_started = True

    def pause(self):
        if self.is_started:
            elapsed = perf_counter() - self.start_time
            self.time_data.append(elapsed)
            self.is_started = False
        elif len(self.time_data) == 0:
            self.print.error('Timer not started')
        else:
            self.print.error('Timer already paused')

    def resume(self):
        if self.is_started:
            self.print.error('Timer already started')
        elif len(self.time_data) == 0:
            self.print.error('Timer not started')
        else:
            self.start_time = perf_counter()
            self.is_started = True

    def get_elapsed(self):
        elapsed = perf_counter() - self.start_time
        total_time = sum(self.time_data) + elapsed

        return format_time(total_time, self.ms_digits, self.format)

    def stop(self):
        if not self.is_started and len(self.time_data) == 0:
            self.print.error('Timer not started')
        else:
            if self.is_started:
                elapsed = perf_counter() - self.start_time
                self.time_data.append(elapsed)

            total_time = sum(self.time_data)
            self.is_started = False
            formatted_time = format_time(total_time, self.ms_digits, self.format)
            self.time_data = []

            self.print.info(formatted_time)
