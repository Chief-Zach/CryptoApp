import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen


yellow = [1,1,0,1]
grey = [1,1,1,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

ButtonNames = ["Bitcoin", "Ethereum", "Solana"]
ButtonColours = [yellow, grey, purple]
class HomeScreenLayout(App):
    def build(self):
        layout = BoxLayout(padding=10,orientation="vertical")
        btcBtn = Button(text=ButtonNames[0],
                     background_color=ButtonColours[0]
                     )
        btcBtn.bind(on_press=self.btcClicked)
        ethBtn = Button(text=ButtonNames[1],
                        background_color=ButtonColours[1]
                        )
        solBtn = Button(text=ButtonNames[2],
                        background_color=ButtonColours[2]
                        )
        layout.add_widget(btcBtn)
        layout.add_widget(ethBtn)
        layout.add_widget(solBtn)
        return layout
    def btcClicked(self, *args):
        app = CoinInterface()
        app.run()

class CoinInterface(App):
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        self.lbl1 = Label(text="test")
        layout.add_widget(self.lbl1)
        self.txt1 = TextInput(text='', multiline=False)
        layout.add_widget(self.txt1)
        return layout

    # button click function
    def buttonClicked(self):
        self.lbl1.text = "You wrote " + self.txt1.text


if __name__ == "__main__":
    app = HomeScreenLayout()
    app.run()
