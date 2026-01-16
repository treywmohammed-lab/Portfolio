import tkinter as tk
import random

num_guesses = 0

guess_history = []

def update_guess_number():
    guess = int(user_input.get())
    guess_history.append(str(guess))
    

    if guess == computer_guess:
        label.config(text=f'{guess} is correct!')
        history_label.config(text=f'You got it in {len(guess_history)} guesses.')
        computer_label.config(text=f'Computer Guess: {computer_guess}')
        user_input.delete(0, tk.END)

        user_submit.config(text='Reset', command=reset_game)
        
    elif guess > computer_guess:
        label.config(text=f'{guess} is to HIGH')
        computer_label.config(text=f'Computer Guess: ?')
        history_label.config(text="Your Guesses: " + ", ".join(guess_history))
        user_input.delete(0, tk.END) # clear the entry box
    elif guess < computer_guess:
        label.config(text=f'{guess} is to LOW')
        computer_label.config(text=f'Computer Guess: ?')
        history_label.config(text="Your Guesses: " + ", ".join(guess_history))
        user_input.delete(0, tk.END) # clear the entry box

def reset_game():
    global computer_guess, guess_history
    computer_guess = random.randint(0,25)
    guess_history = []

    label.config(text="Guess a number between 1 and 25")
    history_label.config(text='Your Guesses: ')
    computer_label.config(text='Computer Guess: ')
    user_input.delete(0, tk.END)

    user_submit.config(text='Submit', command=update_guess_number)


root = tk.Tk()

# config settings

root.title('My First Tkinter Progam')
root.geometry('400x400')

# game poriton




label = tk.Label(root, text="Guess a number between 1 and 25")
label.pack(pady=20, padx=60)


user_input = tk.Entry(root)
user_input.pack(pady=30, padx=50)

user_submit = tk.Button(text='Submit', command=update_guess_number)
user_submit.pack()

history_label = tk.Label(root, text="Your Guesses: ")
history_label.pack(pady=20)

computer_label = tk.Label(root, text='Computer Guess: ')
computer_label.pack(pady=20)

computer_guess = random.randint(0, 25)






root.mainloop()