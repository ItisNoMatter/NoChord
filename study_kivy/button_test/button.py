import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

def my_print():
    print("myprint")
class ButtonWidgets(Widget):
    def my_print(self):
        print("myprint")
    pass
class MyButtonApp(App):
    def build(self):
        return ButtonWidgets()
if __name__ == "__main__":
    MyButtonApp().run()