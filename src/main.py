from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App
from mk import MainWindow
from kivy.uix.screenmanager import ScreenManager, Screen
from dataBase import DataBase


class LogIn(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def logInReq(self):
        if self.email!='':
            print('deu certo')

if __name__ == '__main__':
    app = MainWindow()
    app.run()

