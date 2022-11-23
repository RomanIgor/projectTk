
import tkinter
from tkinter import *
import csv
from datetime import datetime as dt
from tkinter import ttk

time_now = dt.now().strftime('%H:%M')
date_now = dt.now().strftime('%Y-%m-%d %H:%M')
root = tkinter.Tk()
root.title(f'Exchange Rates - {date_now}')
frame_color = '#4ca8ff'  # палитра или рал цвета
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)
# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")


# open file
with open("meintest.csv", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)

    # r and c tell us where to grid the labels/r и c указывают нам место расположения меток
    r = 0
    for col in reader:
        c = 0
        for row in col:
            # добавил стиль в меню и цвет
            label = tkinter.Label(second_frame, width=20, height=2,
                                  text=row, relief=tkinter.RIDGE, bg=frame_color)
            label.grid(row=r, column=c)

            c += 1
        r += 1


root.mainloop()
