import tkinter as tk
from tkinter import *
from tkinter import ttk
from Calc import *


class Window:
    '''GUI calculator'''

    def __init__(self, master):
        # The algebraic expression we wish to evaluate
        self.expression = ""
        # The calculator will find the value of the given expression
        self.calc = Calculator()
        # Disable the window maximize
        master.resizable(False, False)

        # Configuring ttk widgets style options
        self.style = ttk.Style(master)
        self.style.configure('TFrame', background='#219ebc',
                             font=('Helvetica', 12))
        self.style.configure('TLabel', background='#8ecae6')
        self.style.configure('TButton', foreground="#023047", background='#fb8500',
                             focuscolor="green", font=('Helvetica', 14), relief=GROOVE)
        self.style.map('TButton',
                       foreground=[('pressed', '#219ebc'),
                                   ('active', '#ffb703'),
                                   ('!disabled', '#023047')],
                       background=[('pressed', '#ffb703'),
                                   ('active', '#fb8500'),
                                   ('!disabled', '#fb8500')])
        # Setting window title and configure widgets options
        master.title("Calculator")

        master.columnconfigure(0, weight=7)
        master.rowconfigure(0, weight=5)

        # Creating the Frame widget in ttk
        self.frame = ttk.Frame(master, padding="5 3 5 5")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))

        # Creating calculator display variable and Entry widget in ttk
        self.display = StringVar()
        self.display_entry = ttk.Label(
            self.frame, textvariable=self.display, font=('Helvetica', 16))  # width=16
        self.display_entry.grid(column=0, row=0, columnspan=7, sticky=(
            W, E), padx=1, pady=1, ipadx=3, ipady=5)
        self.display_entry.columnconfigure(0, weight=1)

        # Creating calculator buttons in ttk and adding functionality to them
        self.arc = ttk.Button(self.frame, text="ARC",
                              command=lambda: self.add(self.display, "arc"))
        self.arc.grid(column=0, row=1, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.opar = ttk.Button(self.frame, text="(",
                               command=lambda: self.add(self.display, "( "))
        self.opar.grid(column=1, row=1, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.cpar = ttk.Button(self.frame, text=")",
                               command=lambda: self.add(self.display, " )"))
        self.cpar.grid(column=2, row=1, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.cl = ttk.Button(self.frame, text="C",
                             command=lambda: self.clear(self.display))
        self.cl.grid(column=3, row=1, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.bs = ttk.Button(self.frame, text="<-",
                             command=lambda: self.delete(self.display))
        self.bs.grid(column=4, row=1, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.div = ttk.Button(self.frame, text="DIV",
                              command=lambda: self.add(self.display, " div "))
        self.div.grid(column=5, row=1, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.mod = ttk.Button(self.frame, text="MOD",
                              command=lambda: self.add(self.display, " % "))
        self.mod.grid(column=6, row=1, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.degRadB = ttk.Button(self.frame, text="DEG -> RAD",
                                  command=lambda: self.toggle_deg_rad(self.degRadB, self.calc))
        self.degRadB.grid(column=0, row=2, columnspan=2,
                          sticky=(N, W, E, S), padx=1, pady=1, ipady=5)

        self.ctg = ttk.Button(self.frame, text="CTG",
                              command=lambda: self.add(self.display, "ctg "))
        self.ctg.grid(column=2, row=2, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.seven = ttk.Button(self.frame, text="7",
                                command=lambda: self.add(self.display, "7"))
        self.seven.grid(column=3, row=2, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.eight = ttk.Button(self.frame, text="8",
                                command=lambda: self.add(self.display, "8"))
        self.eight.grid(column=4, row=2, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.nine = ttk.Button(self.frame, text="9",
                               command=lambda: self.add(self.display, "9"))
        self.nine.grid(column=5, row=2, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.plus = ttk.Button(self.frame, text="+",
                               command=lambda: self.add(self.display, " + "))
        self.plus.grid(column=6, row=2, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.sin = ttk.Button(self.frame, text="SIN",
                              command=lambda: self.add(self.display, "sin "))
        self.sin.grid(column=0, row=3, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.cos = ttk.Button(self.frame, text="COS",
                              command=lambda: self.add(self.display, "cos "))
        self.cos.grid(column=1, row=3, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.tg = ttk.Button(self.frame, text="TG",
                             command=lambda: self.add(self.display, "tg "))
        self.tg.grid(column=2, row=3, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.four = ttk.Button(self.frame, text="4",
                               command=lambda: self.add(self.display, "4"))
        self.four.grid(column=3, row=3, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.five = ttk.Button(self.frame, text="5",
                               command=lambda: self.add(self.display, "5"))
        self.five.grid(column=4, row=3, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.six = ttk.Button(self.frame, text="6",
                              command=lambda: self.add(self.display, "6"))
        self.six.grid(column=5, row=3, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.minus = ttk.Button(self.frame, text="-",
                                command=lambda: self.add(self.display, " - "))
        self.minus.grid(column=6, row=3, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.log = ttk.Button(self.frame, text="LOG",
                              command=lambda: self.add(self.display, "log "))
        self.log.grid(column=0, row=4, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.pow = ttk.Button(self.frame, text="POWER",
                              command=lambda: self.add(self.display, " ^ "))
        self.pow.grid(column=1, row=4, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.pi = ttk.Button(self.frame, text="Pi", command=lambda: self.add(
            self.display, "3.1415926535897932"))
        self.pi.grid(column=2, row=4, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.one = ttk.Button(self.frame, text="1",
                              command=lambda: self.add(self.display, "1"))
        self.one.grid(column=3, row=4, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.two = ttk.Button(self.frame, text="2",
                              command=lambda: self.add(self.display, "2"))
        self.two.grid(column=4, row=4, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.three = ttk.Button(self.frame, text="3",
                                command=lambda: self.add(self.display, "3"))
        self.three.grid(column=5, row=4, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.mul = ttk.Button(self.frame, text="*",
                              command=lambda: self.add(self.display, " * "))
        self.mul.grid(column=6, row=4, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.fac = ttk.Button(self.frame, text="FACTORIAL",
                              command=lambda: self.add(self.display, "!"))
        self.fac.grid(column=0, row=5, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.choose = ttk.Button(self.frame, text="CHOOSE",
                                 command=lambda: self.add(self.display, " choose "))
        self.choose.grid(column=1, row=5, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.e = ttk.Button(self.frame, text="e", command=lambda: self.add(
            self.display, "2.7182818284590452"))
        self.e.grid(column=2, row=5, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.zero = ttk.Button(self.frame, text="0",
                               command=lambda: self.add(self.display, "0"))
        self.zero.grid(column=3, row=5, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.point = ttk.Button(self.frame, text=".",
                                command=lambda: self.add(self.display, "."))
        self.point.grid(column=4, row=5, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.eq = ttk.Button(self.frame, text="=",
                             command=lambda: self.evaluate(self.display, self.calc))
        self.eq.grid(column=5, row=5, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        self.divide = ttk.Button(self.frame, text="/",
                                 command=lambda: self.add(self.display, " / "))
        self.divide.grid(column=6, row=5, sticky=(
            N, W, E, S), padx=1, pady=1, ipady=5)

        # Binding methods to events
        self.bindings(master)

    def bindings(self, master):
        '''This method binding methods to events'''
        master.bind('<Return>', lambda e: self.evaluate(
            self.display, self.calc))
        master.bind('<KP_Enter>', lambda e: self.evaluate(
            self.display, self.calc))
        master.bind('<KP_0>', lambda e: self.add(self.display, "0"))
        master.bind('<KP_1>', lambda e: self.add(self.display, "1"))
        master.bind('<KP_2>', lambda e: self.add(self.display, "2"))
        master.bind('<KP_3>', lambda e: self.add(self.display, "3"))
        master.bind('<KP_4>', lambda e: self.add(self.display, "4"))
        master.bind('<KP_5>', lambda e: self.add(self.display, "5"))
        master.bind('<KP_6>', lambda e: self.add(self.display, "6"))
        master.bind('<KP_7>', lambda e: self.add(self.display, "7"))
        master.bind('<KP_8>', lambda e: self.add(self.display, "8"))
        master.bind('<KP_9>', lambda e: self.add(self.display, "9"))
        master.bind('<KP_Decimal>', lambda e: self.add(self.display, "."))
        master.bind('<KP_Add>', lambda e: self.add(self.display, " + "))
        master.bind('<KP_Subtract>', lambda e: self.add(self.display, " - "))
        master.bind('<KP_Multiply>', lambda e: self.add(self.display, " * "))
        master.bind('<KP_Divide>', lambda e: self.add(self.display, " / "))
        master.bind('<ampersand>', lambda e: self.add(self.display, " div "))
        master.bind('<percent>', lambda e: self.add(self.display, " % "))
        master.bind('<parenleft>', lambda e: self.add(self.display, "( "))
        master.bind('<parenright>', lambda e: self.add(self.display, " )"))
        master.bind('<Delete>', lambda e: self.clear(self.display))
        master.bind('<BackSpace>', lambda e: self.delete(self.display))
        master.bind('<Escape>', lambda e: master.destroy())
        master.bind('s', lambda e: self.add(self.display, "sin "))
        master.bind('c', lambda e: self.add(self.display, "cos "))
        master.bind('t', lambda e: self.add(self.display, "tg "))
        master.bind('g', lambda e: self.add(self.display, "ctg "))
        master.bind('a', lambda e: self.add(self.display, "arc"))
        master.bind('dr', lambda e: self.add(
            self.display, self.toggle_deg_rad(self.degRadB, self.calc)))
        master.bind('l', lambda e: self.add(self.display, "log "))
        master.bind('<asciicircum>', lambda e: self.add(self.display, " ^ "))
        master.bind('o', lambda e: self.add(self.display, " choose "))
        master.bind('f', lambda e: self.add(self.display, "!"))
        master.bind('p', lambda e: self.add(
            self.display, "3.1415926535897932"))
        master.bind('e', lambda e: self.add(
            self.display, "2.7182818284590452"))

    def evaluate(self, display, calc):
        '''This method evaluates expressions and sets the result to the calculator display'''
        calc.set_expr(display.get())
        res = calc.get_result()
        if res != 'Error!':
            if (float(res) - int(float(res)) == 0):
                display.set(str(int(float(res))))
            else:
                display.set(res)
        else:
            display.set('Error!')

    def clear(self, display):
        '''This method clears the calculator display.'''
        display.set('')

    def add(self, display, str):
        '''This method add string to display.'''
        if display.get() == 'Error!':
            display.set('')
        else:
            display.set(display.get()+str)

    def delete(self, display):
        '''This method deletes the last character on the calculator display.'''
        display.set(display.get()[0:-1])

    def toggle_deg_rad(self, button, calc):
        '''This method toggles the calculator to do all internal calculations in degrees or radians.'''
        if (button['text'] == 'DEG -> RAD'):
            button['text'] = 'RAD -> DEG'
            button['background'] = 'red'
            calc.set_deg(False)
        else:
            button['text'] = 'DEG -> RAD'
            calc.set_deg(True)


if __name__ == '__main__':
    root = tk.Tk()
    calculator = Window(root)
    root.mainloop()
