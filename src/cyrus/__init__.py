"""A TUI based Markdown editor."""

__VERSION__ = "0.1.0"

from textual.app import App, ComposeResult
from textual.widgets import Header, Static, Footer


class Cyrus(App[None]):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Hello, World")
        yield Footer()


def main() -> None:
    app = Cyrus()
    app.run()
