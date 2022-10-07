import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__(**kwargs)

        self.cols = 2
        self.add_widget(Label(text = "Patient name",))
        self.p_name = TextInput()
        self.add_widget(self.p_name)

        self.add_widget(Label(text = "Patient number",))
        self.p_number = TextInput()
        self.add_widget(self.p_number)

        
        self.add_widget(Label(text = "Patient gender",))
        self.p_gender = TextInput()
        self.add_widget(self.p_gender)

        self.add_widget(Label(text = "appointment date",))
        self.a_date = TextInput()
        self.add_widget(self.a_date)

        self.add_widget(Label(text = "Doctor",))
        self.doctor = TextInput()
        self.add_widget(self.doctor)

        self.add_widget(Label(text = "Emergency contact",))
        self.e_contact = TextInput()
        self.add_widget(self.e_contact)

        self.add_widget(Label(text = "Phone number",))
        self.ph_number = TextInput()
        self.add_widget(self.ph_number)

class parentApp(App):
    def build(self):
        return super(childApp).build()

if __name__=='__main__':
    parentApp().run()

