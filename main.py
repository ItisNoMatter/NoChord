from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


Builder.load_file("nochord.kv")
C2 = "C2.wav"

class NoChordApp(App):
    def load_sound(self,soundfiles):
        self.sounds = [SoundLoader.load(sf) for sf in soundfiles]
    def on_start(self):
        #for dev
        self.i  = -1 
        self.current_button_id = -1
        self.pressed_button_id = -1
        
        self.load_sound([C2])
        self.sound_index = 0
    def play_sound(self):
        if self.current_button_id != self.pressed_button_id:
            self.i += 1
            self.current_button_id = self.pressed_button_id
        try:
            self.sounds[self.i].play()
        except IndexError:
            print("finish")

if __name__ == '__main__':
    NoChordApp().run()