from consolecolors.fg import Fg


class PrintColor:
    @staticmethod
    def log(text: str):
        print(text + Fg.RESET.value)
