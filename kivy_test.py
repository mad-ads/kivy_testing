# kivy_test.py - Test app with kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class Widgets(Widget):
    pass

class LoginScreen(GridLayout):
    # makes a basic login screen
    def __init__(self,**kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols = 2
        # now make username line
        self.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        # now make password
        self.add_widget(Label(text='Password:'))
        self.password = TextInput(multiline=False,password=True)
        self.add_widget(self.password)
        return

class SimpleKivy(App):
    # creates a simple App
    def build(self):
        return LoginScreen()

class SimpleKivy2(App):
    def build(self):
        return Widgets()

# Run it
if __name__ == '__main__':
    SimpleKivy2().run()
