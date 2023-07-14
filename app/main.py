import kivy
from kivy.app import App
from kivy.uix.widget import Widget


class Grid(Widget):
    pass


class Tetris(App):
    def build(self):
        return Grid()


if __name__ == "__main__":
    Tetris().run()
