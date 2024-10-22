<h1>Typing Speed Test Application </h1>

<p>This is a simple Typing Speed Test built with Python’s Tkinter library. It helps you practice typing by giving you random words to type and measuring your speed in terms of Characters Per Minute (CPM) and Words Per Minute (WPM).</p>

<h2>Features</h2>

  - Random Words: The app displays a list of random words for you to type.
  - Typing Box: You type into a text box, and the app tracks what you've typed.
  - Real-Time Feedback: Correctly typed words are highlighted in blue, while mistakes are marked in red.
  - Speed Metrics: The app calculates and displays your CPM and WPM as you type.
  - Restart Option: You can restart the test at any time with the click of a button.
  - Timer: After 60 seconds, the typing box is disabled, marking the end of the test.

<h2>How It Works</h2>

  1. When you start the app, you'll see a list of random words on the screen.
  2. Type the words into the typing box below the list.
  3. As you type, the app will highlight correct words in blue and incorrect ones in red.
  4. Your typing speed (CPM and WPM) will be shown on the right-hand side.
  5. When the timer runs out, the typing box is disabled, and you can see your final score.
  6. You can press the Restart button to try again.

<h2>Getting Started</h2>

<h3>Prerequisites</h3>

  - Python 3.x installed on your system.
  - You'll need the following Python libraries:
    - Tkinter (standard Python GUI library)
    - Pandas (for loading the word list from a CSV file)

<h3>Installation</h3>

  1. Download the project files to your computer.
  2. Install the Pandas library (if you don't have it already) by running:

    pip install pandas

  3. Make sure you have a CSV file called Most common words in the same folder as the Python script. This file should have a column called 1000 words that lists the words you'll use in the typing test.
  4. Run the script:

    python TypingTest.py
    
<h2>CSV File Format</h2>

The program expects a CSV file with a list of common words. The file should look something like this:

    python
    Copiar código
    1000 words
    the
    and
    hello
    world
    ...

<h3>Code Overview</h3>

  - TypingTest Class: This is the core of the application. It handles the user interface and typing logic.
    - __init__: Sets up the UI, including the text boxes for the random words and user input.
    - timer: Starts a 60-second countdown after you begin typing.
    - type_test: Compares what you type with the list of random words and highlights them.
    - score: Calculates and updates the CPM and WPM based on correct words.
    - restart: Resets everything so you can start a new test.

<h3>Customization</h3>

- If you'd like to change the number of words displayed, modify this line in the code:

      self.random_words = [choice(list_of_words) for __ in range(300)]

- You can also adjust the test duration by tweaking the timer in the timer function:

      return window.after(60000, lambda: self.typing_box.config(state=tk.DISABLED))
  
<h2>Future Improvements</h2>

Here are a few features that could be added in the future:

  - Accuracy percentage (to show how many words were typed correctly).
  - A results screen that shows your final score after the test ends.
  - Word difficulty levels or adjustable word lists.

<h2>License</h2>

This project is open-source and licensed under the MIT License. Feel free to modify and share!
