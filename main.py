import tkinter as tk
import pandas as pd
from random import choice

# Setting up database of words
data = pd.read_csv('Most common words')
list_of_words = data['1000 words'].tolist()


class TypingTest:
    def __init__(self, root):
        self.random_words = [choice(list_of_words) for __ in range(300)]  # List of random words

        self.typed = ''  # Variable to carry the text from the typed box

        # Text box with the text that will be typed
        self.sample_text = tk.Text(root, wrap='word', padx=10, pady=10, font=20)
        self.sample_text.grid(row=0, column=1)
        self.sample_text.insert(tk.END, ' '.join(self.random_words))

        # Box for the user to type in
        self.typing_box = tk.Text(root, wrap='word', padx=10, pady=10, font=20)
        self.typing_box.focus()
        self.typing_box.grid(row=1, column=1)
        self.typing_box.bind_all("<space>", lambda event: self.type_test())
        self.typing_box.bind_all("<Key>", lambda event: self.timer())

        # Button to start the typing test
        self.start_button = tk.Button(root, height=1, width=10, command=self.restart, text='Restart', bg='blue')
        self.start_button.grid(row=1, column=2)

        # The score board variables
        self.var = tk.StringVar()
        label = tk.Label(root, textvariable=self.var)

        self.var.set('CPM: 0\nWPM: 0')
        label.grid(row=0, column=2)

    # Timer function
    def timer(self):
        # This function will set a timer of 60 seconds after any key is typed in the text box
        return window.after(60000, lambda: self.typing_box.config(state=tk.DISABLED))

    # Comparing sample text with the typed text
    def type_test(self):
        self.typed = self.typing_box.get(1.0, "end-1c").split(' ')
        index = self.typed.index(self.typed[-2])

        start_pos = 0
        for i, word in enumerate(self.random_words):  # Taking the index and items of the list
            end_pos = start_pos + len(word)  # Establishing the end position for the tag

            if i == index:
                self.sample_text.tag_add(f"tag{index}", f"1.{start_pos}",
                                         f"1.{end_pos}")
                if self.typed[-2] == self.random_words[index]:
                    # configuring the tag for correct word
                    self.sample_text.tag_config(f"tag{index}", foreground="blue")
                else:
                    self.sample_text.tag_config(f"tag{index}", foreground="red")
                break
            start_pos = end_pos + 1  # Calculating the starting position
            # for the next word accounting for the whitespace
        self.score()

    def score(self):
        all_typed_words = self.typed[:-1]
        # Characters per minute
        score = sum([len(all_typed_words[n]) for n in range(len(all_typed_words))
                    if all_typed_words[n] == self.random_words[n]])

        # Words per minute
        wpm = score // 5

        self.var.set(f'CPM: {score}\nWPM:{wpm}')

    def restart(self):
        self.typing_box.config(state=tk.NORMAL)
        self.typing_box.delete(1.0, tk.END)
        return self.typing_box.focus()


# Setting up Tkinter
window = tk.Tk()
window.title('Typing Speed Test')
window.state('zoomed')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
app = TypingTest(window)

window.mainloop()
