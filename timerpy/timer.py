from time import perf_counter

from timerpy.printer import Printer
from timerpy.utils import format_time


class Timer:
    def __init__(self, tag: str = 'timer.py', format: str = '%02d:%02d:%02d.%s',
                 ms_digits: int = 3, color: str = 'green', start: bool = False):
        self.time_data = []
        self.is_started = False
        self.start_time = None
        self.format = format
        self.ms_digits = ms_digits
        self.color = color
        self.print = Printer(tag)

        if start:
            self.start()

    def start(self) -> None:
        if self.is_started:
            self.print.error('Timer already started')
        else:
            self.start_time = perf_counter()
            self.is_started = True

    def pause(self) -> None:
        if self.is_started:
            elapsed = perf_counter() - self.start_time
            self.is_started = False

            self.time_data.append(elapsed)
        elif len(self.time_data) == 0:
            self.print.error('Timer not started')
        else:
            self.print.error('Timer already paused')

    def resume(self) -> None:
        if self.is_started:
            self.print.error('Timer already started')
        elif len(self.time_data) == 0:
            self.print.error('Timer not started')
        else:
            self.start_time = perf_counter()
            self.is_started = True

    def elapsed(self, tag: str = None, print: bool = True) -> float:
        if not self.is_started and len(self.time_data) == 0:
            self.print.error('Timer not started')

            return 0
        else:
            elapsed = perf_counter() - self.start_time if self.is_started else 0
            total_time = sum(self.time_data) + elapsed
            formatted_time = format_time(total_time, self.ms_digits, self.format)

            if print:
                self.print.info(formatted_time, tag)

            return total_time

    def stop(self, tag: str = None, print: bool = True) -> float:
        total_time = self.elapsed(tag, print)
        self.time_data = []
        self.is_started = False

        return total_time
