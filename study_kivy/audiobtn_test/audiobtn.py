import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader

soundfile = "pianoC4.wav"

class AudioBtnWidget(Widget):
    def __init__(self):
        super(AudioBtnWidget, self).__init__()
        self.sound = SoundLoader.load(soundfile)

    def play_sounds(self):
        self.sound.play()
    pass

class MyAudioBtn(App):
    def build(self):
        return AudioBtnWidget()
if __name__ == "__main__":
    MyAudioBtn().run()