import kivy
from kivy.app import App
from kivy.uix.label import Label


class Tetris(App):
    def build(self):
        return Label(text="Tetris")


if __name__ == "__main__":
    Tetris().run()
