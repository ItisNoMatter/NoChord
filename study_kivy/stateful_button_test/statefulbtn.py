import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader

C2 = "C2.wav"
G2 = "G2.wav"
SOUNDS = [C2,G2]

class NoChord(Widget):
    def __init__(self):
        super(NoChord, self).__init__()
        self.sound = SoundLoader.load(C2)
        self.sounds = [SoundLoader.load(i) for i in SOUNDS]
    def play_sound(self):
        self.sound.play()
    def play_sounds(self,i):
        self.sounds[i].play()

class MyStatefulBtn(App):
    def build(self):
        return NoChord()
if __name__ == "__main__":
    MyStatefulBtn().run()