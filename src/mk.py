from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]
black = [0, 0, 0, 0]
grey = [1, 1, 1, 1]

class MainWindow(App):
    def build(self):
        color = [red, green, blue, purple, black, grey]
        
        mainLayout = FloatLayout()
        backgroundImage = Image(source='background.jpg',
                                allow_stretch=True,
                                keep_ratio=False,
                                size_hint=(1, 1),
                                pos_hint={'center_x':.5, 'center_y':.5})
        mainLayout.add_widget(backgroundImage)
        
        emailLayout = BoxLayout(spacing =15, orientation='horizontal', size_hint=(.8, .1),
                                pos_hint={'center_x':.5, 'center_y':.6})
        emailLabel = Label(text='Email:', size_hint=(.2, 1), color=grey, font_size=65)
        self.email = TextInput(multiline=False, 
                               readonly=False, halign='left', font_size=50, 
                               size_hint=(.63, .65),
                               pos_hint={'center_x':.5, 'center_y':.6},
                               background_color=grey)
        emailLayout.add_widget(emailLabel)
        emailLayout.add_widget(self.email)

        passwordLayout = BoxLayout(spacing=75, orientation='horizontal', size_hint=(.8, .1),
                                   pos_hint={'center_x':.5, 'center_y':.515})
        passwordLabel = Label(text='Password:', size_hint=(.2, 1), color=grey, font_size =65)
        self.password = TextInput(multiline=False, 
                                  readonly=False, halign='left', font_size=50, 
                                  size_hint=(.8, .65),
                                  pos_hint={'center_x':.5, 'center_y':.53},
                                  background_color=grey)
        passwordLayout.add_widget(passwordLabel)
        passwordLayout.add_widget(self.password)
        
        mainLayout.add_widget(emailLayout)
        signInButton = Button(text='Sign In', opacity=.7,
                              size_hint=(0.25, 0.075),
                              pos_hint={'center_x':.5, 'center_y':.415},
                              background_color=grey, 
                              font_size=60)
        loginButton = Button(text='Login', opacity=.7,
                             size_hint=(0.25, 0.075),
                             pos_hint={'center_x':.5, 'center_y':.30},
                             background_color=grey,
                             font_size=60)
        mainLayout.add_widget(signInButton)
        mainLayout.add_widget(loginButton)
        signInButton.bind(on_press = self.onSignInButton)
        loginButton.bind(on_press = self.onLogInButton)

        return mainLayout
    
    def onSignInButton(self, instance):
        CreateAccount().run()

    def onLogInButton(self,instance):
        pass

    def create_account(self, instance):
        pass
    
class CreateAccount(App):
    def build(self):
        color = [red, green, blue, purple, black, grey]

        userNameMessage = 'Enter your name'
        userEmailMessage = 'Enter your email'
        userPasswordMessage = 'Define a password'

        createAccountLayout = FloatLayout()
        createAccountBackgroundImage = Image(source='background.jpg',
                                allow_stretch=True,
                                keep_ratio=False,
                                size_hint=(1, 1),
                                pos_hint={'center_x':.5, 'center_y':.5})
        createAccountLayout.add_widget(createAccountBackgroundImage)
        
        userNameLayout = BoxLayout(spacing=5, orientation='horizontal', size_hint=(.8, .1),
                                pos_hint={'center_x':.5, 'center_y':.6})
        userNameLabel = Label(text='Name:', size_hint=(.2, 1), color=grey, font_size=65)
        self.newUserName = TextInput(text=userNameMessage, multiline=False,
                              readonly=False, halign='left', font_size=50, 
                              size_hint=(.8, .65),
                              pos_hint={'center_x':.5, 'center_y':.6},
                              background_color=grey)
        userNameLayout.add_widget(userNameLabel)
        userNameLayout.add_widget(self.newUserName)
        createAccountLayout.add_widget(userNameLayout)

        userEmailLayout = BoxLayout(spacing=5, orientation='horizontal', size_hint=(.8, .1),
                                pos_hint={'center_x':.5, 'center_y':.5})
        userEmailLabel = Label(text='Email:', size_hint=(.2, 1), color=grey, font_size=65)
        self.newUserEmail = TextInput(text=userEmailMessage, multiline=False,
                              readonly=False, halign='left', font_size=50, 
                              size_hint=(.8, .65),
                              pos_hint={'center_x':.5, 'center_y':.6},
                              background_color=grey)
        userEmailLayout.add_widget(userEmailLabel)
        userEmailLayout.add_widget(self.newUserEmail)
        createAccountLayout.add_widget(userEmailLayout)

        userPasswordLayout = BoxLayout(spacing=5, orientation='horizontal', size_hint=(.805, .1),
                                pos_hint={'center_x':.5, 'center_y':.4})
        userPasswordLabel = Label(text='Password:', size_hint=(.025, 1), color=grey, font_size=65)
        self.newUserPassword = TextInput(text=userPasswordMessage, multiline=False,
                              readonly=False, halign='left', font_size=50, 
                              size_hint=(.0975, .65),
                              pos_hint={'center_x':.5, 'center_y':.6},
                              background_color=grey)
        userPasswordLayout.add_widget(userPasswordLabel)
        userPasswordLayout.add_widget(self.newUserPassword)
        createAccountLayout.add_widget(userPasswordLayout)

        buttonsLayer = BoxLayout(spacing=50, orientation='horizontal', size_hint=(.8, .1),
                                pos_hint={'center_x':.5, 'center_y':.25})
        saveButton = Button(text='Save', opacity=.7,
                             size_hint=(0.25, 0.75),
                             pos_hint={'center_x':.5, 'center_y':.30},
                             background_color=grey,
                             font_size=60)
        cancelButton = Button(text='Cancel', opacity=.7,
                             size_hint=(0.25, 0.75),
                             pos_hint={'center_x':.5, 'center_y':.30},
                             background_color=grey,
                             font_size=60)
        buttonsLayer.add_widget(saveButton)
        buttonsLayer.add_widget(cancelButton)
        createAccountLayout.add_widget(buttonsLayer)
        saveButton.bind(on_press = self.onSaveButton)
        cancelButton.bind(on_press = self.onCancelButton)

        return createAccountLayout
    
    def onCancelButton(self, instance):
        MainWindow().run()
    
    def onSaveButton(self, instance):
        return None

    def accountCreationConfirmation(self, instance):
        popupAccountCreatedMessage = Popup(title='Account Created',
                    content=Label(text='Account successfully created!'),
                    size_hint=(None, None), size=(400, 400),
                    auto_dismiss=False)
        popupAccountCreatedMessage.open()

class LogedIn(App):
    def build(self):
        pass
        
    def accountLogInConfirmation(self, instance):
        popupLoggedIn = Popup(title='LogIn Success',
                    content=Label(text='You will be redirected to the page!'),
                    size_hint=(None, None), size=(400, 400),
                    auto_dismiss=False)
        popupLoggedIn.open()
        
