import tkinter as tk
'''Imports Tkinter module, tk is an alias for easy access'''


def press(v):
    entry.insert(tk.END, v)


'''Called when a number or operator button is clicked inserts the pressed value at the end of the Entry widget'''


def clear():
    entry.delete(0, tk.END)
    '''Clears the calculator screen deletes all characters from index 0 to the End'''


def calc():
    try:
        result = eval(entry.get())
        '''entry.get() retrieves the expression (e.g 5+3), eval() evaluates the string as a python expression'''

        entry.delete(0, tk.END)  # Clears the screen
        entry.insert(0, result)  # displays the result

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Expression")
        '''Handles invalid expressions(e.g 5++), Display appropriate message instead of crashing'''

# backspace Button Creation


def backspace():
    current = entry.get()
    if current:
        entry.delete(len(current)-1, tk.END)
    '''Deletes the last character from the Entry widget'''


# Main Window Creation
root = tk.Tk()  # creates the main application window

root.title("Calculator")  # Sets window title

root.resizable(False, False)  # Prevents window resizing

root.configure(bg="lightgray")  # sets background color '#1e1e1e'

# Entry Widget Creation(Display Screen)
entry = tk.Entry(
    root,
    width=20,
    font=('Arial', 24),
    bd=0,
    fg='black',
    justify='right'
)
'''Text input field acts as the calculator display screen right-aligned for better calculator aesthetics'''

entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

'''Places entry at top, columnspan=4 makes it stretch across 4 columns'''
# Button Creation
buttons = [

    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
'''Represents calculator buttons stored in a list to reduce repetitive code'''
r = 1
c = 0

'''rows and column counters for grid layout'''
for b in buttons:
    cmd = calc if b == "=" else lambda x=b: press(x)
    '''if button is '=', otherwise call press() with button value lambda x=b prevents late binding issue'''

    tk.Button(
        root,
        text=b,
        width=5,
        height=2,
        font=('Arial', 18),
        command=cmd,
        bg="#DA73F3" if b in '+-*?/' else "#373B34",
        fg='white',
        bd=0,

    ).grid(row=r, column=c, padx=6, pady=6)

    c += 1
    if c == 4:
        c = 0
        r += 1

    '''Moves to the next row after 4 buttons '''

# Clear Button Creation
tk.Button(
    root,
    text='C',
    width=20,
    height=2,
    font=('Arial', 18),
    command=clear,
    bg="#53A4EF",
    fg='white',
    bd=0,
).grid(row=r, column=0, columnspan=3, pady=8)
'''Creates Clear button that spans 2 columns'''

# Backspace Button Creation
tk.Button(
    root,
    text='⌫',
    width=5,
    height=2,
    font=('Arial', 18),
    command=backspace,
    bg="#F05454",
    fg='white',
    bd=0,
).grid(row=r, column=3, pady=8)


# Start the main event loop
root.mainloop()
