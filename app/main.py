import random
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
from kivy.clock import Clock
from block import Block


class TetrisWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.board = [[(255, 255, 255) for i in range(10)] for j in range(20)]
        self.block = Block(random.randint(0, 6))
        self.delay = 1

        # Load Music
        self.sound = SoundLoader.load("assets/bgm.wav")
        self.sound.play()

        # Set Clock
        Clock.schedule_interval(self.play_tick, self.delay)

    def play_tick(self, _):
        self.block.move([0, -1], self.board)
        print(self.board)


class TetrisApp(App):
    def build(self):
        return TetrisWidget()


if __name__ == "__main__":
    TetrisApp().run()
