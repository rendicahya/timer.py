from print_color import print as print_color


class Printer:
    def __init__(self, tag: str):
        self.tag = tag

    def error(self, text: str) -> None:
        print_color(text, tag=self.tag, tag_color='red', color='white')

    def info(self, text: str) -> None:
        print_color(text, tag=self.tag, tag_color='green', color='white')
