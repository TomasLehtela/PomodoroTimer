import tkinter as tk
import math
import winsound

# Constants
PINK = "#e2979c"
RED = "#B83B56"
ORANGE = "#FF7F3F"
YELLOW = "#F2D880"
GREEN = "#408758"
BROWN = "#B3A394"
LIGHT_GREY = "#CDD7D6"
FONT_NAME = "Georgia"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
after_timer = None


def reset_timer():
    global reps
    window.after_cancel(after_timer)
    canvas.itemconfig(timer_text, text="00:00")
    header_text.config(text="TIMER", fg=BROWN)
    reps = 0
    winsound.PlaySound("stop.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        countdown(work_sec)
        header_text.config(text="WORK!", fg=GREEN)
        winsound.PlaySound("start.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif reps == 2 or reps == 4 or reps == 6:
        countdown(short_sec)
        header_text.config(text="BREAK!")
        winsound.PlaySound("stop.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif reps == 8:
        countdown(long_sec)
        header_text.config(text="BREAK!")
        winsound.PlaySound("stop.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)


def countdown(count):

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    clock_text = f"{minutes}:{seconds}"

    canvas.itemconfig(timer_text, text=clock_text)
    if count > 0:
        global after_timer
        after_timer = window.after(1000, countdown, count - 1)
    else:
        countdown()
        global reps
        mark = ""
        reps_checker = math.floor(reps / 2)
        for _ in range(reps_checker):
            mark += "✔"
        checkmarks.config(text=mark)


# Window
window = tk.Tk()
window.title("25min Work/Break Time")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20, bg=LIGHT_GREY)


# Header text
header_text = tk.Label(
    text="TIMER", font=(FONT_NAME, 34, "bold"), fg=BROWN, bg=LIGHT_GREY
)
header_text.grid(column=2, row=1)

# BG IMG
canvas = tk.Canvas(width=200, height=224, bg=LIGHT_GREY, highlightthickness=0)
BG_IMG = tk.PhotoImage(file="beachh.png")
canvas.create_image(100, 112, image=BG_IMG)
timer_text = canvas.create_text(
    100, 110, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white"
)
canvas.grid(column=2, row=2)

# Buttons
start_button = tk.Button(
    text="START", command=start_timer, bg=BROWN, fg=LIGHT_GREY, width=7
)
start_button.grid(column=1, row=3)
start_button.config(padx=8, pady=8)

reset_button = tk.Button(
    text="RESET", command=reset_timer, bg=BROWN, fg=LIGHT_GREY, width=7
)
reset_button.grid(column=3, row=3)
reset_button.config(padx=8, pady=8)

# Checkmark
checkmarks = tk.Label(font=(FONT_NAME, 16, "normal"), fg=GREEN, bg=LIGHT_GREY)
checkmarks.grid(column=2, row=3)

window.mainloop()
