from tkinter import *
import tkmacosx
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(main_image, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(main_image, image=back_image)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

front_image = PhotoImage(file="./images/card_front.png")
known_image = PhotoImage(file="./images/right.png")
unknown_image = PhotoImage(file="./images/wrong.png")
back_image = PhotoImage(file="./images/card_back.png")

canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
main_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, fill="black", text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 260, fill="black", text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

unknown_button = tkmacosx.Button(image=unknown_image, borderless=1, activebackground=BACKGROUND_COLOR,
                               activeforeground=BACKGROUND_COLOR, bg=BACKGROUND_COLOR, focuscolor='', command=next_card)
unknown_button.grid(column=0, row=1)
known_button = tkmacosx.Button(image=known_image, borderless=1, activebackground=BACKGROUND_COLOR,
                               activeforeground=BACKGROUND_COLOR, bg=BACKGROUND_COLOR, focuscolor='', command=next_card)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
