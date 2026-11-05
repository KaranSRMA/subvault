from rich.console import Console

from .Colors import PRIMARY, SECONDARY, INPUT, INFO, SUCCESS, WARNING, ERROR, TEXT, MUTED



class UI:
    def __init__(self):
        self.console = Console()

    def get_input(self, user_input):
        return self.console.input(f"[{INPUT}]{user_input}: [/]").strip()

    def primary(self, txt):
        self.console.print(f"[{PRIMARY}]{txt}")

    def secondary(self, txt):
        self.console.print(f"[{SECONDARY}]{txt}")

    def success(self, msg):
        self.console.print(f"[{SUCCESS}]{msg}[/]")

    def info(self, info):
        self.console.print(f"[{INFO}]{info}[/]")

    def text(self, txt):
        self.console.print(f"[{TEXT}]{txt}")

    def muted(self, txt):
        self.console.print(f"[{MUTED}]{txt}")

    def output(self, txt):
        self.console.print(txt)

    def err(self, err):
        print()
        self.console.print(f"[{ERROR}]{err}[/]")
        print()

    def warn(self, warn):
        print()
        self.console.print(f"[{WARNING}]{warn}[/]")
        print()

    def warn_err(self, warn, err):
        print()
        self.console.print(f"[{WARNING}]{warn}:[/] [{ERROR}]{err}[/]")
        print()