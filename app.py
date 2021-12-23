from tkinter import *
import json
from tkinter import messagebox
import tinder
import os
from time import sleep
# Constants
FONT_NAME = "Courier"


def check_data_from_json(location_term):
    with open("data.json", "r") as data_file:
        data = json.load(data_file)

        if location_term in data["locations"]:
            return True
        else:
            return False


def get_locations():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
    return data["locations"]


def start_bot():
    os.chdir("/Users/riccardofeingold")
    os.system('Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"')
    sleep(2)
    locations = get_locations()
    bot = tinder.TinderBot(locations=locations)
    bot.auto_swipe()


class SwipeBotApp:
    def __init__(self, master):
        self.master = master

        self.master.title("Tinder Swipe Bot")

        self.title_label = Label(self.master, text="Tinder Bot", font=(FONT_NAME, 25, "bold"))
        self.title_label.grid(row=0, column=1)

        self.before_you_start_label = Label(self.master, text="Before you start, enter the following command into the terminal to activate Google Chrome.", font=(FONT_NAME, 18, "bold"))
        self.before_you_start_label.grid(row=1, column=1)

        self.command_label = Label(self.master, text='Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"', font=(FONT_NAME, 18, "bold"))
        self.command_label.grid(row=2, column=1)

        self.input_locations = Entry(self.master, width=21)
        self.input_locations.grid(row=3, column=0)

        self.add_location_button = Button(self.master, text="Add", command=self.add_location, width=12)
        self.add_location_button.grid(row=3, column=1)

        self.start_button = Button(self.master, text="Start", command=start_bot, width=12)
        self.start_button.grid(row=4, column=1)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=5, column=1)

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


root = Tk()
app = SwipeBotApp(root)
root.mainloop()
