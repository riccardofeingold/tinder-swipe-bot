from tkinter import *
import json
from tkinter import messagebox
import tinder
# Constants
FONT_NAME = "Courier"


def check_data_from_json(location_term):
    with open("data.json", "r") as data_file:
        data = json.load(data_file)

        if location_term in data["locations"]:
            return True
        else:
            return False


def start_bot():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        bot = tinder.TinderBot(data["locations"])
        app.destroy()
        bot.auto_swipe()


class SwipeBotApp(Tk):
    def __init__(self):
        super(SwipeBotApp, self).__init__()
        print("hello")
        self.title("Tinder Swipe Bot")
        self.minsize(500, 400)

        self.title_label = Label(text="Tinder Bot", font=(FONT_NAME, 25, "bold"))
        self.title_label.grid(row=0, column=1)

        self.before_you_start_label = Label(text="Before you start, enter the following command into the terminal to activate Google Chrome.", font=(FONT_NAME, 18, "bold"))
        self.before_you_start_label.grid(row=1, column=1)

        self.command_label = Label(text='Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"', font=(FONT_NAME, 18, "bold"))
        self.command_label.grid(row=2, column=1)

        self.input_locations = Entry(width=21)
        self.input_locations.grid(row=3, column=0)

        self.add_location_button = Button(text="add", command=self.add_location, width=12)
        self.add_location_button.grid(row=3, column=1)

        self.start_button = Button(text="Start", command=start_bot, width=12)
        self.start_button.grid(row=4, column=1)

    def add_location(self):
        location_term = self.input_locations.get()
        new_data = {
            "locations": [
                location_term
            ]
        }
        if check_data_from_json(location_term=location_term):
            messagebox.showinfo(title="location already stored", message=f"{location_term} is already on your list!")
        else:
            try:
                data_file = open("data.json", "r")
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data = json.load(data_file)
                data["locations"].append(location_term)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                data_file.close()
                self.input_locations.delete(0, END)


app = SwipeBotApp()
app.mainloop()
