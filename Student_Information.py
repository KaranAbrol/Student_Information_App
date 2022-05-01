import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childapp(GridLayout):
    def  __init__(self,**kwargs):
        super(childapp,self).__init__()
        self.cols = 3
        self.add.widget(Label(text = 'student name'))
        self.s_name =TextInput()
        self.add.widger(self.s_name)

        self.add.widget(Label(text = 'student marks'))
        self.s_marks =TextInput()
        self.add.widger(self.s_marks)

        self.add.widget(Label(text = 'student gender'))
        self.s_gender =TextInput()
        self.add.widger(self.s_gender)

        self.press = Button(text='Click Me')
        self.press.bind(on_click = self.click_me)
        self .add_widget(self.press)

    def click_me(self,instances):
        print("NAME OF STUDENT IS"+self.s_name.text)
        print("MARKSOF STUDENT IS"+self.s_marks.text)
        print("GENDER OF STUDENT IS"+self.s_gender.text)
        print()


class parentapp(App):
    def build(self):
        return childapp()

if __name__ == "__main":
    parentapp().run()
