from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

Builder.load_file("PreDevNoChord.kv")

# Declare both screens
class StartScreen(Screen):
    pass
class PlayModeScreen(Screen):
    pass
class EditModeScreen(Screen):
    pass

# Create the screen manager

sm = ScreenManager()
sm.add_widget(StartScreen())
sm.add_widget(PlayModeScreen())
sm.add_widget(EditModeScreen())

C2 = "wav/C2.wav"
E2 = "wav/E2.wav"
G2 = "wav/G2.wav"

class PreDevNoChordApp(App):
    def play_sound(self):
        if self.current_button_id != self.pressed_button_id:
            self.i += 1
            self.current_button_id = self.pressed_button_id
        try:
            self.sounds[self.i].play()
        except IndexError:
            print("finish")

    def load_sound(self,soundfiles):
        self.sounds = [SoundLoader.load(sf) for sf in soundfiles]
    def build(self):
        #for dev
        self.i  = -1 
        self.current_button_id = -1
        self.pressed_button_id = -1
        
        self.load_sound([C2,E2,G2])
        self.sound_index = 0
        

        
        return sm


if __name__ == '__main__':
    PreDevNoChordApp().run()