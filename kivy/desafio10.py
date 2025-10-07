from kivy.app import App
from kivy.uix.button import Button

class OutraApp(App):
    def build(self): #adcionei os dois pontos 
        return Button(text='Corrija o Retorno!') #Returnei o botao e tirei  o ".run()"
OutraApp().run()
