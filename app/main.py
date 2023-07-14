import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Board(GridLayout):
    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        print("Boop!")


class Tetris(App):
    def build(self):
        return Board()


if __name__ == "__main__":
    Tetris().run()
