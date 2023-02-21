from print_color import print as print_color


class Printer:
    def __init__(self, tag: str):
        self.tag = tag

    def set_tag(self, tag: str) -> None:
        self.__init__(tag)

    def error(self, text: str, tag: str = None) -> None:
        print_color(
            text, tag=self.tag if tag is None else tag, tag_color="red", color="white"
        )

    def info(self, text: str, tag: str = None) -> None:
        print_color(
            text, tag=self.tag if tag is None else tag, tag_color="green", color="white"
        )
