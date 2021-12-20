from tkinter import *
import tinder

class SwipeBotApp(Tk):
    def __init__(self):
        super(SwipeBotApp, self).__init__()

        self.title("Tinder Swipe Bot")
        self.minsize(500, 400)

    def view(self):


app = SwipeBotApp()
app.mainloop()
