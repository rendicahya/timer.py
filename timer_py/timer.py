from time import perf_counter

from timer_py.printer import Printer
from timer_py.utils import format_time


class Timer:
    def __init__(
        self,
        tag: str = "timer.py",
        format: str = "%02d:%02d:%02d.%s",
        ms_digits: int = 3,
        color: str = "green",
        start: bool = False,
    ):
        self.time_data = []
        self.is_started = False
        self.start_time = None
        self.format = format
        self.ms_digits = ms_digits
        self.color = color
        self.printer = Printer(tag)

        if start:
            self.start()

    def start(self, tag: str = None):
        if tag is not None:
            self.printer.set_tag(tag)

        if self.is_started:
            self.printer.error("Timer already started")
        else:
            self.start_time = perf_counter()
            self.is_started = True

        return self

    def pause(self) -> None:
        if self.is_started:
            elapsed = perf_counter() - self.start_time
            self.is_started = False

            self.time_data.append(elapsed)
        elif len(self.time_data) == 0:
            self.printer.error("Timer not started")
        else:
            self.printer.error("Timer already paused")

    def resume(self) -> None:
        if self.is_started:
            self.printer.error("Timer already started")
        elif len(self.time_data) == 0:
            self.printer.error("Timer not started")
        else:
            self.start_time = perf_counter()
            self.is_started = True

    def restart(self) -> None:
        self.start_time = perf_counter()
        self.time_data = []
        self.is_started = True

    def elapsed(self, tag: str = None, print: bool = True, raw: bool = False):
        if not self.is_started and len(self.time_data) == 0:
            self.printer.error("Timer not started")

            return 0
        else:
            elapsed = perf_counter() - self.start_time if self.is_started else 0
            total_time = sum(self.time_data) + elapsed
            formatted_time = format_time(total_time, self.ms_digits, self.format)

            if print:
                self.printer.info(formatted_time, tag)

            return elapsed if raw else formatted_time

    def set_tag(self, tag: str) -> None:
        self.printer.set_tag(tag)

    def stop(self, tag: str = None, print: bool = True) -> str:
        elapsed_time = self.elapsed(tag, print, raw=True)
        formatted_time = format_time(elapsed_time, self.ms_digits, self.format)
        self.time_data = []
        self.is_started = False

        return formatted_time
