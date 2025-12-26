from tkinter import Tk, Label, Button, StringVar
from tkinter.font import Font
import time

class DigitalClock:
    def __init__(self, font=None):
        """Initialize the digital clock."""
        self.is_24_hour = True  # Feature: toggle 12/24 hour
        self.is_dark_mode = True  # Feature: dark/light theme
        self.quotes = [
            "Work like hell. – Elon Musk",
            "When something is important enough, you do it even if the odds are not in your favor. – Elon Musk",
            "Failure is an option here. – Elon Musk",
        ]
        self.create_window()
        self.configure_window()
        self.set_font(font)
        self.add_header()
        self.add_clock()
        self.add_date()
        self.add_day()
        self.add_quote()
        self.add_buttons()
        self.update_time_on_clock()

    def create_window(self):
        self.window = Tk()
        self.window.title("Digital Clock")
        self.window.geometry("800x500")

    def configure_window(self):
        self.update_theme()

    def set_font(self, customFont):
        DEFAULT_FONT = Font(family='Arial', size=90, weight='bold')
        self.font = customFont if customFont else DEFAULT_FONT

    def add_header(self):
        self.header = Label(self.window, text="Time Clock", font=('Arial', 30, 'bold'))
        self.header.pack(pady=10)

    def add_clock(self):
        self.clock = Label(self.window, font=self.font, bg='black', fg='white')
        self.clock.pack(pady=20)

    def add_date(self):
        self.date_label = Label(self.window, font=('Arial', 25, 'bold'))
        self.date_label.pack()
        self.update_date_on_clock()

    def add_day(self):
        self.day_label = Label(self.window, font=('Arial', 20, 'bold'))
        self.day_label.pack()
        self.update_day_on_clock()

    def add_quote(self):
        self.quote_var = StringVar()
        self.quote_var.set(self.quotes[0])
        self.quote_label = Label(self.window, textvariable=self.quote_var, font=('Arial', 15, 'italic'))
        self.quote_label.pack(pady=10)
        self.update_quote()

    def add_buttons(self):
        # Toggle 12/24 hour
        self.toggle_hour_btn = Button(self.window, text="Toggle 12/24 Hour", command=self.toggle_hour_format)
        self.toggle_hour_btn.pack(pady=5)
        # Toggle light/dark mode
        self.toggle_theme_btn = Button(self.window, text="Toggle Theme", command=self.toggle_theme)
        self.toggle_theme_btn.pack(pady=5)

    def toggle_hour_format(self):
        self.is_24_hour = not self.is_24_hour

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.update_theme()

    def update_theme(self):
        if self.is_dark_mode:
            bg, fg = 'black', 'white'
        else:
            bg, fg = 'white', 'black'
        self.window.config(bg=bg)
        self.clock.config(bg=bg, fg=fg)
        self.date_label.config(bg=bg, fg=fg)
        self.day_label.config(bg=bg, fg=fg)
        self.header.config(bg=bg, fg=fg)
        self.quote_label.config(bg=bg, fg=fg)

    def update_quote(self):
        import random
        self.quote_var.set(random.choice(self.quotes))
        self.quote_label.after(10000, self.update_quote)  # change quote every 10 seconds

    def update_date_on_clock(self):
        currentDate = time.strftime("%d-%b-%Y")
        self.date_label.config(text=currentDate)
        self.date_label.after(86400000, self.update_date_on_clock)  # update daily

    def update_day_on_clock(self):
        day = time.strftime("%A")
        self.day_label.config(text=day)
        self.day_label.after(86400000, self.update_day_on_clock)  # update daily

    def update_time_on_clock(self):
        if self.is_24_hour:
            currentTime = time.strftime("%H:%M:%S")
        else:
            currentTime = time.strftime("%I:%M:%S %p")
        self.clock.config(text=currentTime)
        self.clock.after(1000, self.update_time_on_clock)

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    clock = DigitalClock()
    clock.start()
