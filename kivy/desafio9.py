from kivy.app import App #Arrumei a importação do app, que estava Ap e não App
from kivy.uix.label import Label

class MeuApp(App): #Arrumei o App
    def build(self):
        return Label(text='Kivy App com Bug de Importação')
MeuApp().run()