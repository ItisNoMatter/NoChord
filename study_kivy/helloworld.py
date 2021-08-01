import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label

class HelloApp(App):

    def build(self):
        return Label(text='Hello World')

if __name__ == '__main__':
    HelloApp().run()
