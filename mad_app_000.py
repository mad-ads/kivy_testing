# Version 000 of MAD's advertising app. Associated .kv file is mad_app_000.kv

# Import statements
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('mad_app_000.kv')


class LoginScreen(Widget):
    # makes a basic login screen
    pass

class MainWidgets(Widget):
    pass



class MADApp(App):
    # creates the app
    def build(self):
        return LoginScreen()


# Run it
if __name__ == '__main__':
    MADApp().run()
