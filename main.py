# Project: Typing speed test
# TODO 4: Define a typing function that will have the timing functionality and the spelling check
# TODO 5: Add a typing detection functionality to start the test
# TODO 6: Define a function to calculate CPM and WPM
# TODO 7: Create a restart button and function
# TODO 8: Have a box to type the person's name and a function and database to save the record

import tkinter as tk
import pandas as pd
from random import choice

# Setting up database of words
data = pd.read_csv('Most common words')
list_of_words = data['1000 words'].tolist()


class TypingTest:
    def __init__(self, root):
        self.random_words = [choice(list_of_words) for __ in range(300)]  # List of random words

        self.typed = None  # Variable to carry the text from the typed box

        # Text box with the text that will be typed
        self.sample_text = tk.Text(root, wrap='word', padx=10, pady=10, font=20)
        self.sample_text.grid(row=0, column=1)
        self.sample_text.insert(tk.END, ' '.join(self.random_words))

        # Box for the user to type in
        self.typing_box = tk.Text(root, wrap='word', padx=10, pady=10, font=20)
        self.typing_box.grid(row=1, column=1)
        self.typing_box.bind_all("<space>", lambda event: self.type_test())

        # Button to start the typing test
        self.start_button = tk.Button(root, height=1, width=10, command=self.timer, text='Start', bg='blue')
        self.start_button.grid(row=1, column=2)

        # The score board variables
        self.var = tk.StringVar()
        label = tk.Label(root, textvariable=self.var)

        self.var.set("0")
        label.grid(row=0, column=2)

    # Timer function
    def timer(self):
        return window.after(10000, lambda: self.typing_box.config(state=tk.DISABLED))

    # Comparing sample text with the typed text
    def type_test(self):
        self.typed = self.typing_box.get(1.0, "end-1c")
        last_word = self.typed.split(' ')[-2]

        typed = self.random_words
        if last_word in typed:
            self.random_words.remove(last_word)  # Removes the most recent word that was typed by the user
            # Updates the entire text by removing the last word the user typed correctly
            self.sample_text.delete('1.0', tk.END)
            self.sample_text.insert(tk.END, ' '.join(self.random_words))
            self.sample_text.update()
        self.score()

    def score(self):
        all_typed_words = self.typed.split(' ')[:-1]

        # Characters per minute
        score = sum([len(all_typed_words[n]) for n in range(len(all_typed_words))
                    if all_typed_words[n] == self.random_words[n]])
        self.var.set(f'{score}')
        print(score)
        # Words per minute
        wpm = score // 5


# Setting up Tkinter
window = tk.Tk()
window.title('Typing Speed Test')
window.state('zoomed')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
app = TypingTest(window)

window.mainloop()
