from kivy.app import App
from kivy.uix.label import Label

class MeuApp(App):
    def build(self):
        return Label(text='Kivy App com Bug de Importação')
MeuApp().run()