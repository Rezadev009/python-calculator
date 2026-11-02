from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def make_button(parent, text, row, column, command,
                bg="#252b3b", fg="white", hover="#343c50",
                colspan=1):
    button = Button(
        parent,
        text=text,
        font=("Arial", 17, "bold"),
        bg=bg,
        fg=fg,
        activebackground=hover,
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=command
    )

    button.grid(
        row=row,
        column=column,
        columnspan=colspan,
        sticky="nsew",
        padx=5,
        pady=5
    )

    button.bind("<Enter>", lambda event: button.config(bg=hover))
    button.bind("<Leave>", lambda event: button.config(bg=bg))

    return button


if __name__ == "__main__":

    gui = Tk()
    gui.title("Calculator")
    gui.geometry("360x500")
    gui.minsize(320, 440)
    gui.configure(bg="#151923")

    for i in range(4):
        gui.grid_columnconfigure(i, weight=1)

    gui.grid_rowconfigure(1, weight=1)

    # عنوان برنامه
    title = Label(
        gui,
        text="CALCULATOR",
        font=("Arial", 15, "bold"),
        bg="#151923",
        fg="#94a3b8"
    )
    title.grid(row=0, column=0, columnspan=4, pady=15)

    # پنل نمایشگر
    display_frame = Frame(gui, bg="#202635")
    display_frame.grid(
        row=1, column=0, columnspan=4,
        sticky="nsew", padx=12, pady=8
    )

    equation = StringVar()

    expression_field = Entry(
        display_frame,
        textvariable=equation,
        font=("Arial", 28, "bold"),
        bg="#202635",
        fg="white",
        insertbackground="white",
        justify="right",
        relief="flat",
        bd=0
    )
    expression_field.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=20
    )

    # پنل دکمه‌ها
    button_frame = Frame(gui, bg="#151923")
    button_frame.grid(
        row=2, column=0, columnspan=4,
        sticky="nsew", padx=8, pady=8
    )

    for i in range(4):
        button_frame.grid_columnconfigure(i, weight=1)

    for i in range(5):
        button_frame.grid_rowconfigure(i, weight=1)

    # ردیف اول
    make_button(button_frame, "7", 0, 0, lambda: press(7))
    make_button(button_frame, "8", 0, 1, lambda: press(8))
    make_button(button_frame, "9", 0, 2, lambda: press(9))
    make_button(button_frame, "÷", 0, 3, lambda: press("/"),
                bg="#e58b36", hover="#f3a34f")

    # ردیف دوم
    make_button(button_frame, "4", 1, 0, lambda: press(4))
    make_button(button_frame, "5", 1, 1, lambda: press(5))
    make_button(button_frame, "6", 1, 2, lambda: press(6))
    make_button(button_frame, "×", 1, 3, lambda: press("*"),
                bg="#e58b36", hover="#f3a34f")

    # ردیف سوم
    make_button(button_frame, "1", 2, 0, lambda: press(1))
    make_button(button_frame, "2", 2, 1, lambda: press(2))
    make_button(button_frame, "3", 2, 2, lambda: press(3))
    make_button(button_frame, "−", 2, 3, lambda: press("-"),
                bg="#e58b36", hover="#f3a34f")

    # ردیف چهارم
    make_button(button_frame, "0", 3, 0, lambda: press(0))
    make_button(button_frame, ".", 3, 1, lambda: press("."))
    make_button(button_frame, "=", 3, 2, equalpress,
                bg="#16a36a", hover="#20bd7c")
    make_button(button_frame, "+", 3, 3, lambda: press("+"),
                bg="#e58b36", hover="#f3a34f")

    # دکمه پاک کردن
    make_button(button_frame, "CLEAR", 4, 0, clear,
                bg="#c94350", hover="#e05260",
                colspan=4)

    gui.mainloop()

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')


