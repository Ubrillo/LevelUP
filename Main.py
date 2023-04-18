from kivy.app import App
from kivy.core import window
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation

#Builder.load_file('Main.kv')

class WelcomeWindow(Screen):
    pass
class MainWindow(Screen):
    pass
class SelectWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

class QuizWindow(Screen):
    def option_test(self, button, data):
        correct = "{3,4}"
        if data == correct:
            button.background_normal = ''
            button.background_color = '#29d62d'
            #button.background_color: (1, 1, 1, .2)
        else:
            button.background_normal = ''
            button.background_color = (1, 0, 0, 1)
            #button.background_color: (1, 1, 1, .2)

    def next_question(self):
        with open('ipds/ipds_question/questions.txt', 'r') as ipds_file:
            options = ipds_file.readline()
            contents = ipds_file.readline()
            option_array = options.split(' ')
            option_id = ['op1', 'op2', 'op3', 'op4']

            self.ids.op1.text = option_array[1]
            self.ids.op2.text = option_array[2]
            self.ids.op3.text = option_array[3]
            self.ids.op4.text = option_array[4]
            self.ids.question_display.text = contents

class Summary(Screen):
    pass
class Main(App):
    def build(self):
        pass
        #window.size_hint = (0.1, 0.7)
        #Window.clearcolor = (1, 1, 1, 0.5)
        #QuizWindow.clearcolor = (133/255, 31/255, 140/255, 1)

Main().run()
