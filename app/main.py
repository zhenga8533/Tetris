import random

import numpy
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.core.window import Window

# Kivy Game PogO
Window.size = (Window.size[1] / 2, Window.size[1])


class TetrisBlock(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Block Variables
        self.size = (Window.size[0] / 10, Window.size[1] / 20)

        self.pos = (Window.size[0] / 2, Window.size[1])
        self.vel_x = NumericProperty(0)
        self.vel_y = NumericProperty(-5)
        self.velocity = ReferenceListProperty(self.vel_x, self.vel_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class TetrisGame(Widget):
    block = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.board = numpy.zeros((20, 10))
        self.delay = 1

        # Load Music
        self.sound = SoundLoader.load("assets/bgm.wav")
        self.sound.play()

    def get_block(self, vel=(0, -30)):
        self.block.velocity = vel

    def play_tick(self, _):
        self.block.move()


class TetrisApp(App):
    def build(self):
        game = TetrisGame()
        game.get_block()
        Clock.schedule_interval(game.play_tick, 1)
        return game


if __name__ == "__main__":
    TetrisApp().run()
