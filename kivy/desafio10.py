from kivy.app import App
from kivy.uix.button import Button

class OutraApp(App):
    def build(self):
        return Button(text='Corrija o Retorno!')
OutraApp().run()
