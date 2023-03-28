from print_color import print as print_color


class Printer:
    def error(self, text: str, tag: str = None) -> None:
        print_color(
            text, tag=tag, tag_color="red", color="white", background="black"
        )

    def info(self, text: str, tag: str = None) -> None:
        print_color(
            text, tag=tag, tag_color="green", color="white", background="black"
        )
