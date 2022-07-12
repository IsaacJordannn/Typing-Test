from tkinter import *
import time
import sys

class Game:
    """"""

    def __init__(self):
        """"""
        self.window = Tk()
        self.window.title("Typing Test")
        self.window.geometry("1280x960")
        self.window.resizable(False, False)
        self.time = 1
        self.main_page()
        self.window.mainloop()

    def main_page(self):
        """"""
        frame = Frame(self.window)
        frame.pack()
        undo = Button(frame, text="Undo", font="courier 12")
        undo.pack()
        redo = Button(frame, text="Redo", font="courier 12")
        redo.pack()
        refresh = Button(frame, text="Refresh", font="courier 12")
        refresh.pack()
        faq = Button(frame, text="Frequently Asked Questions", font="courier 12")
        faq.pack()
        title = Label(frame, text="Typing Test", font="courier 36 bold")
        title.pack()
        length = Label(frame, text="Length (in minutes):", font="courier 20")
        length.pack()
        length_choice = StringVar(frame)
        length_choice.set("1")
        length_options = OptionMenu(frame, length_choice, "1", "2", "3")
        length_options.pack()
        difficulty = Label(frame, text="Difficulty:", font="courier 20")
        difficulty.pack()
        difficulty_choice = StringVar(frame)
        difficulty_choice.set("Easy")
        difficulty_options = OptionMenu(frame, difficulty_choice, "Easy", "Medium", "Hard")
        difficulty_options.pack()
        topic = Label(frame, text="~Optional~ Topic:", font="courier 20")
        topic.pack()
        topic_choice = Text(frame, height=1, width=20)
        topic_choice.pack()
        informative_box = Label(frame, text="***You can now choose your own typing topic to make the tests even more fun!***", font="courier 16")
        informative_box.pack()
        start_button = Button(frame, text="START", command=self.test_page, font="courier 32 bold")
        start_button.pack(side = BOTTOM)
        advanced_options = Button(frame, text="Advanced Options", font="courier 18 bold")
        advanced_options.pack()

    def test_page(self):
        """"""
        mins, secs = divmod(self.time * 60, 60)
        frame = Frame(self.window)
        frame.pack()
        start_text = Label(frame, text="Start When Ready By Pressing Key", font="courier 20")
        start_text.pack()
        timer = Label(frame, text="{:02d}:{:02d}".format(mins, secs), font="courier 20")
        timer.pack()
        given_text = Text(frame, height=6, width=80)
        given_text.configure(state="disabled")
        given_text.pack()
        user_input = Text(frame, height=6, width=80)
        user_input.pack()

    def start_test(self):
        """"""

    def results_page(self):
        """"""

    def faq_page(self):
        """"""

    def get_text(self):
        """"""


if __name__ == "__main__":
    Game()