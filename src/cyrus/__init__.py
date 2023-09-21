"""A TUI based Markdown editor."""

__VERSION__ = "0.1.0"

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static


class Cyrus(App[None]):
    """A TUI based Markdown editor."""

    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Hello, World")
        yield Footer()


def main() -> None:
    app = Cyrus()
    app.run()
