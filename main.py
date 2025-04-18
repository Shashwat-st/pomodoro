from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_time():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    tick_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
# # ---------------------------- TIMER PAUSE ------------------------------- #
#
# def pause_time():
#     window.after_idle(timer)
#     title_label.config(text="Pause")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    window.focus_force()
    global reps
    reps += 1
    work_sec = 60 * WORK_MIN
    short_break_sec = 60 * SHORT_BREAK_MIN
    long_break_sec = 60 * LONG_BREAK_MIN

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps
    global timer
    count_min = math.floor(count/60)
    if count_min == 0:
        count_min = '00'
    elif count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        ticks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            ticks += "✔"
        tick_label.config(text=ticks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_time)
reset_button.grid(column=2, row=2)

tick_label = Label(font=(FONT_NAME, 15, 'normal'), fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)

# pause_button = Button(text="Pause", command=pause_time)
# pause_button.grid(column=1, row=2)

window.mainloop()