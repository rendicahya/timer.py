from time import perf_counter, sleep

from timerpy.printer import Printer
from timerpy.utils import format_time


class Timer:
    def __init__(self, tag: str = 'timer.py', format: str = '%02d:%02d:%02d.%s', ms_digits: int = 3,
                 color: str = 'green'):
        self.time_data = []
        self.is_started = False
        self.start_time = None
        self.format = format
        self.ms_digits = ms_digits
        self.color = color
        self.print = Printer(tag)

    def start(self) -> None:
        if self.is_started:
            self.print.error('Timer already started')
        else:
            self.start_time = perf_counter()
            self.is_started = True

    def pause(self) -> None:
        if self.is_started:
            elapsed = perf_counter() - self.start_time
            self.time_data.append(elapsed)
            self.is_started = False
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

    def elapsed(self, print: bool = True, tag: str = None) -> float:
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

    def stop(self, print: bool = True, tag: str = None) -> float:
        total_time = self.elapsed(print, tag)
        self.time_data = []
        self.is_started = False

        return total_time


if __name__ == '__main__':
    t = Timer()
    t.start()
    sleep(1)
    t.elapsed(tag='elapsed')
    t.stop(tag='stop')
