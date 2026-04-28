import tkinter as tk

# Variables:
step = 0
curr_num = 0
x = 0
x2 = 0
x3 = 0

#colors:
BG = "#ffeef3"
CARD = "#db82c6"
BTN = "#e194f1"
BTN_HOVER = "#500e3b"
TEXT = "#1a1a1a"


# Functions:
def continue_game():
    global step, curr_num, x, x2, x3

    step += 1

    try:
        # STEP 1
        if step == 1:
            label.config(text="Think of a number between 1-10")

        # STEP 2 (input phase)
        elif step == 2:
            label.config(text="Enter your number below 👇")
            entry.pack()
            button.config(text="Submit")

        # STEP 3
        elif step == 3:
            curr_num = int(entry.get())
            entry.pack_forget()

            label.config(text="Multiply the number by 2")

        # STEP 4
        elif step == 4:
            x = curr_num * 2
            label.config(text=f"You got {x}!")

        # STEP 5
        elif step == 5:
            label.config(text="Now add 8 to that number")

        # STEP 6
        elif step == 6:
            x2 = x + 8
            label.config(text=f"You got {x2}!")

        # STEP 7
        elif step == 7:
            label.config(text="Now divide the number by 2")

        # STEP 8
        elif step == 8:
            x3 = x2 // 2
            label.config(text=f"You got {x3}!")

        # STEP 9
        elif step == 9:
            label.config(text="Now subtract your original number from the number that you got...")

        # STEP 10
        elif step == 10:
            result = x3 - curr_num
            label.config(text=f"You got {result}!")

        # STEP 11
        elif step == 11:
            label.config(text="Turn your number into a letter (1-A, 2-B, 3-C, 4-D, 5-E and 6- F)")

        # STEP 12
        elif step == 12:
            label.config(text="Your letter is: D!!")

        # STEP 13
        elif step == 13:
            label.config(text="Think of a country starting with that letter")

        # STEP 14
        elif step == 14:
            label.config(text="Now think of an animal starting with the next letter, e.g: if you got B think of an animal with C and so on..")

        # STEP 15
        elif step == 15:
            label.config(text="Think of a color of that animal")

        # STEP 16
        elif step == 16:
            label.config(text="THERE'S NO GREY ELEPHANTS IN DENMARK ;) ")
            button.config(state="disabled")

    except ValueError:
        label.config(text="Please enter a valid number!")
        step = 1


# UI: 

root = tk.Tk()
root.title("Let's guess what's on your mind?")
root.geometry("520x350")
root.configure(bg=BG) 

# Center container:
frame = tk.Frame(root, bg=CARD, padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Label:
label = tk.Label(
    frame,
    text="Click Start",
    font=("Arial", 14, "bold"),
    fg=TEXT,
    bg=CARD,
    wraplength=400,
    justify="center"
)
label.pack(pady=20)

# Entry:
entry = tk.Entry(
    frame,
    font=("Arial", 12),
    bg="#3b3b55",
    fg="white",
    insertbackground="white",
    relief="flat",
    justify="center"
)

# Button hover effects:
def on_enter(e):
    button.config(bg=BTN_HOVER)

def on_leave(e):
    button.config(bg=BTN)

# Button
button = tk.Button(
    frame,
    text="Start",
    command=continue_game,
    font=("Arial", 12, "bold"),
    fg="white",
    bg=BTN,
    activebackground=BTN_HOVER,
    activeforeground="white",
    relief="flat",
    padx=15,
    pady=8
)
button.pack(pady=10)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()