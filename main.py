import tkinter
from tkinter import ttk

root = tkinter.Tk()

main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0)

year_entry = ttk.Entry(main_frame,width=5)
year_entry.grid(row=0, column=0, padx=5, pady=5)
month_entry = ttk.Entry(main_frame,width=5)
month_entry.grid(row=0, column=2, padx=5, pady=5)
day_entry = ttk.Entry(main_frame ,width=5)
day_entry.grid(row=0, column=4, padx=5, pady=5)

year_label = ttk.Label(main_frame, text="년")
year_label.grid(row=0, column=1, padx=5, pady=5)

month_label = ttk.Label(main_frame, text="월")
month_label.grid(row=0, column=3, padx=5, pady=5)

day_label = ttk.Label(main_frame, text="일 까지")
day_label.grid(row=0, column=5, padx=5, pady=5)

left_label = ttk.Label(main_frame, text="남았습니다")
left_label.grid(row=1, column=5, padx=5, pady=5)

button = ttk.Button(main_frame, text="some text")
button.grid(row=2, column=5, padx=5, pady=5)


root.mainloop()