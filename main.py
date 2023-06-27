from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
root = Tk()
root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=700, height=426)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(350, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)


root.mainloop()
