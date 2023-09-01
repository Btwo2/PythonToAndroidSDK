"""
My first BeeWare App
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from functools import partial

class Example(toga.App):

    async def checkbox_update(self, widget, **kwargs):
        self.main_box.remove(self.button)
        self.clicks += 1
        self.text = 'Example button clicked: ' + str(self.clicks) + ' times'
        self.button = toga.Button(self.text, on_press=self.checkbox_update, style=self.btn_style)
        self.main_box.add(self.button)
    
    def startup(self):
        self.main_box = toga.Box(self)
        self.btn_style = Pack(padding=20, flex=1)
        
        self.clicks = 0
        self.text = 'Example button clicked: 0 times'
        
        self.button = toga.Button(self.text, on_press=self.checkbox_update, style=self.btn_style)
        self.main_box.add(self.button)
        
        self.main_window= toga.MainWindow (title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()
        
        
    

def main():
    return Example()
