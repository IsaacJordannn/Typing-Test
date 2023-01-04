from tkinter import *
from tkinter.ttk import *
import time


class TypingTest:

    def __init__(self, window):
        self.current_page = "home"
        self.difficulty = StringVar()
        self.length = IntVar()
        self.running = False
        self.window = window
        self.window.title("Typing Test")
        self.window.geometry("1200x900")
        self.window.configure(background="blue")
        self.home()

    # similar to HTML, correlates to lines of code
    def home(self):
        for i in self.window.winfo_children():
            i.destroy()
        frame_home = Frame(self.window).pack(side=TOP, fill=BOTH)
        Button(frame_home, text="FAQ", command=self.faq).pack(side=TOP, anchor=NW)
        Label(frame_home, text="*** New Difficulty Feature Allows You To Put Your Typing To The Test! ***", font=("Terminal", 12)).pack(padx=15, pady=15)
        Label(frame_home, text="Typing Test", font=("Terminal", 32)).pack()
        Label(frame_home, text="* Choose Length *", font=("Terminal", 24)).pack(padx=15, pady=15)
        Radiobutton(frame_home, text="30 Seconds", variable=self.length, value=30).pack(padx=5, pady=5)
        Radiobutton(frame_home, text="60 Seconds", variable=self.length, value=60).pack(padx=5, pady=5)
        Radiobutton(frame_home, text="90 Seconds", variable=self.length, value=90).pack(padx=5, pady=5)
        Radiobutton(frame_home, text="120 Seconds", variable=self.length, value=120).pack(padx=5, pady=5)
        Label(frame_home, text="* Choose Difficulty *", font=("Terminal", 24)).pack(padx=5, pady=5)
        Label(frame_home, text="~~~ Choosing Hard Will Restrict The Use Of Backspace On Your Test ~~~", font=("Terminal", 12)).pack(padx=5, pady=5)
        Radiobutton(frame_home, text="Normal", variable=self.difficulty, value="Normal").pack(padx=5, pady=5)
        Radiobutton(frame_home, text="Hard", variable=self.difficulty, value="Hard").pack(padx=5, pady=5)
        Button(frame_home, text="START", width=25, command=self.warn).pack()

    def warn(self):
        for i in self.window.winfo_children():
            i.destroy()
        frame_warn = Frame(self.window).pack(side=TOP, fill=BOTH)
        if self.difficulty.get() == "Hard":
            Label(frame_warn, text="Are you sure you want to take the hard test?", font=("Terminal", 24)).pack()
            Button(frame_warn, text="Yes", command=self.test).pack(padx=5, pady=5)
            Button(frame_warn, text="No", command=self.home).pack(padx=5, pady=5)
        else:
            self.home()

    def back(self):
        if self.current_page == "faq" or self.current_page == "test":
            self.home()
        else:
            self.test()

    def forward(self):
        if self.current_page == "test":
            self.results()
        else:
            self.home()
    
    # similar to HTML, correlates to lines of code
    def faq(self):
        for i in self.window.winfo_children():
            i.destroy()
        self.current_page = "faq"
        frame_faq = Frame(self.window).pack(side=TOP, fill=BOTH)
        Button(frame_faq, text="Back", command=self.back).pack(side=TOP, anchor=NW)
        Label(frame_faq, text="FAQ PAGE", font=("Terminal", 24)).pack()
        Label(frame_faq, text="Are there default values for the length and difficulty?", font=("Terminal", 20)).pack(padx=5, pady=5)
        Label(frame_faq, text="Yes, for difficulty it is Normal and length it 30 seconds.", font=("Terminal", 12)).pack(padx=5, pady=5)
        Label(frame_faq, text="Why are the navigation buttons different on each page?", font=("Terminal", 20)).pack(padx=5, pady=5)
        Label(frame_faq, text="The buttons at the top of each page follow the logic behind the pages.", font=("Terminal", 12)).pack(padx=5, pady=5)
        Label(frame_faq, text="How is my test scored?", font=("Terminal", 20)).pack(padx=5, pady=5)
        Label(frame_faq, text="The input is compared against the original text and scores are given.", font=("Terminal", 12)).pack(padx=5, pady=5)

    def wiki(self):
        f = open("random_wiki_service.txt", "r+", encoding="utf-8")
        f.write("run")
        f.close()
        time.sleep(3)
        f = open("random_wiki_service.txt", "r+", encoding="utf-8")
        txt = f.read()
        f.close()
        return txt

    # similar to HTML, correlates to lines of code
    def test(self):
        for i in self.window.winfo_children():
            i.destroy()
        self.current_page = "test"
        self.difficulty_val = self.difficulty.get()
        self.length_val = self.length.get()
        self.secs = self.length_val
        txt = self.wiki()
        frame_test = Frame(self.window).pack(side=TOP, fill=BOTH)
        Button(frame_test, text="Back", command=self.back).pack(side=TOP, anchor=NW)
        Button(frame_test, text="Forward", command=self.forward).pack(side=TOP, anchor=NW)
        Label(frame_test, text="* Start When Ready By Pressing Any Key! *", font=("Terminal", 28)).pack(padx=15, pady=15)
        text_wiki = Text(frame_test, wrap=WORD)
        text_wiki.insert(END, txt)
        text_wiki.configure(state="disabled")
        text_wiki.pack(fill=BOTH)
        text_input = Text(frame_test, wrap=WORD)
        text_input.pack(fill=BOTH)
        if self.difficulty_val == "Hard":
            text_input.bind("<BackSpace>", lambda _:"break")
        text_input.bind("<KeyPress>", self.start_test)

    def start_test(self, input):
        if not self.running:
            self.running = True
            self.window.after(self.length_val * 1000, self.results)
        f = open("user_input.txt", "a+", encoding="utf-8")
        f.write(input.char)
        f.close()

    # similar to HTML, correlates to lines of code
    def results(self):
        for i in self.window.winfo_children():
            i.destroy()
        self.current_page = "results"
        self.running = False
        stats = self.compare()
        frame_results = Frame(self.window).pack(side=TOP, fill=BOTH)
        Button(frame_results, text="Back", command=self.back).pack(side=TOP, anchor=NW)
        Button(frame_results, text="Forward", command=self.forward).pack(side=TOP, anchor=NW)
        Label(frame_results, text="Congratulations! Look at your stats below to see how you did.", font=("Terminal", 22)).pack(padx=15, pady=15)
        Label(frame_results, text="Characters Per Second: {}".format(stats[0]), font=("Terminal", 16)).pack(padx=5, pady=5)
        Label(frame_results, text="Characters Per Minute: {}".format(stats[1]), font=("Terminal", 16)).pack(padx=5, pady=5)
        Label(frame_results, text="Words Per Second: {}".format(stats[2]), font=("Terminal", 16)).pack(padx=5, pady=5)
        Label(frame_results, text="Words Per Minute: {}".format(stats[3]), font=("Terminal", 16)).pack(padx=5, pady=5)
        Label(frame_results, text="Accuracy: {}".format(stats[4]), font=("Terminal", 16)).pack(padx=5, pady=5)
        Button(frame_results, text="PLAY AGAIN", width=25, command=self.reset).pack()
        
    def compare(self):
        char_count = 0
        original = open("random_wiki_service.txt", "r+", encoding="utf-8")
        user_input = open("user_input.txt", "r+", encoding="utf-8")
        original_txt = original.read()
        user_txt = user_input.read()
        total_chars = len(user_txt)
        for i in range(total_chars):
            if original_txt[i] != user_txt[i]:
                char_count += 1
        word_count = len(user_txt.split())
        return self.stats(total_chars, word_count, char_count)
        
    def stats(self, total_chars, word_count, char_count):
        chars_sec = total_chars / self.secs
        chars_min = chars_sec * 60
        words_sec = word_count / self.secs
        words_min = words_sec * 60
        accuracy = ((total_chars - char_count) / total_chars ) * 100
        return chars_sec, chars_min, words_sec, words_min, accuracy

    def reset(self):
        f1 = open("random_wiki_service.txt", "r+", encoding="utf-8")
        f2 = open("user_input.txt", "r+", encoding="utf-8")
        f1.truncate(0)
        f2.truncate(0)
        f1.close()
        f2.close()
        self.home()

if __name__ == "__main__":
    window = Tk()
    TypingTest(window)
    window.mainloop()