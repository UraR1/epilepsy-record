from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from backend.hello import HelloScreen
from backend.sign_in import InScreen
from backend.sign_up import UpScreen
Builder.load_file('frontend/hello.kv')
Builder.load_file('frontend/sign_in.kv')
Builder.load_file('frontend/sign_up.kv')
class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HelloScreen(name='hello'))
        sm.add_widget(InScreen(name='sign_in'))
        sm.add_widget(UpScreen(name='sign_up'))
        return sm
if __name__ == '__main__':
    MainApp().run()
