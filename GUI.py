import main

from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper = """
ScreenManager:
    HomeScreen:
    ResultScreen:
    
<HomeScreen>:
    name: 'home'
    Image: 
        source: "image.png"
        pos_hint: {'x':0,'y':0.5}
        size_hint: (1,0.5)
    Label:
        text: "Enter the equation"
        font_size: 18
        pos_hint: {'center_x':0.5,'center_y':0.4}
        color : "#000000"
    TextInput:
        id: input
        multiline: False
        padding_y: (20,20)
        pos_hint: {'center_x':0.5,'center_y':0.3}
        size_hint: (0.5,0.1)   
        on_text: app.data = self.text
    MDRectangleFlatButton:
        id: button
        text: "Find root"
        pos_hint: {'center_x':0.5,'center_y':0.2}
        color: "00FFCE" 
        on_press:  root.callback()
        on_release: root.manager.current = 'result'
                    
        
<ResultScreen>:
    label: label
    name: 'result'   
    Label:
        id: label
        text: app.data 
        font_size: 18
        pos_hint: {'center_x':0.5,'center_y':0.4}
        color : "#000000" 
        
"""

class HomeScreen(Screen):

    def callback(self):
        xl = -2
        xu = 4
        es = 0.00001
        imax = 50
        main.bisection(xl, xu, es, imax)
        print(self.ids.input.text)


class ResultScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(ResultScreen(name='result'))


class RootFinder(MDApp):

    data = StringProperty('')

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

        # self.window = GridLayout()
        # self.window.cols = 1
        # self.window.size_hint = (0.6, 0.7)
        # self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        # # add widgets to window
        # self.window.add_widget(Image(source="image.png"))
        # self.greeting = Label(
        #     text="Enter the equation",
        #     font_size= 18,
        #     color = "#00FFCE")
        # self.window.add_widget(self.greeting)
        # self.user = TextInput(
        #     multiline=False,
        #     padding_y = (20,20),
        #     size_hint = (1,0.5),)
        # self.window.add_widget(self.user)
        # self.button = Button(
        #     text="Find root",
        #     size_hint = (1,0.5 ),
        #     bold = True,
        #     background_color = "00FFCE")
        # self.button.bind(on_press = self.callback)
        # self.window.add_widget(self.button)
        # return self.window


    #    self.greeting.text = "Zby ya khawal"+ self.user.text

if __name__ == "__main__":

    RootFinder().run()
#root.manager.get_screen('result').label.text = str(self.text)