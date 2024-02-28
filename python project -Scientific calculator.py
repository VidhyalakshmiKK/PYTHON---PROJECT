import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        master.geometry("680x486+100+100")

        self.total = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.total, font=("century gothic", 20))
        self.entry.grid(row=0, column=0, columnspan=6, pady=6)

        self.create_buttons()

    def create_buttons(self):
        button_list = [
            ['sinθ', 'cosθ', 'tanθ', '^2', '10^x','sinh'],
            ['7', '8', '9', '/', 'log(x)','cosh'],
            ['4', '5', '6', '*', '1/x','tanh'],
            ['1', '2', '3', '-', 'x!','π'],
            ['0', 'C', '=', '+', 'sqrt','2π']
        ]

        for i, row in enumerate(button_list):
            for j, button_text in enumerate(row):
                button = tk.Button(
                    self.master, text=button_text,bg='black',fg='white',width=2, height=1, font=("century gothic", 14),
                    command=lambda text=button_text: self.click(text)
                )
                button.grid(row=i + 1, column=j, sticky="nsew")
            self.master.rowconfigure(i + 1, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.columnconfigure(3, weight=1)
        self.master.columnconfigure(4, weight=1)
        self.master.columnconfigure(5, weight=1)

    def click(self, button_text):
        if button_text == '=':
            try:
                result = eval(self.entry.get())
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'C':
            self.total.set("")
        elif button_text == 'sinθ':
            try:
                result = math.sin(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'cosθ':
            try:
                result = math.cos(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'tanθ':
            try:
                result = math.tan(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == '^2':
            try:

                result = float(self.entry.get()) ** 2
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'log(x)':
            try:
                result = math.log(float(self.entry.get()))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == '1/x':
            try:
                result = 1 / float(self.entry.get())
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'x!':
            try:
                result = math.factorial(int(self.entry.get()))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == '10^x':
            try:
                result = 10 ** float(self.entry.get())
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'sqrt':
            try:
                result = math.sqrt(float(self.entry.get()))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'sinh':
            try:
                result = math.sinh(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'cosh':
            try:
                result = math.cosh(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'tanh':
            try:
                result = math.tanh(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'π':
            try:
                result = math.pi
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == '2π':
            try:
                result = math.pi*2
                self.total.set(result)
            except:
                self.total.set("Error")

        else:
            self.total.set(self.entry.get() + button_text)


if __name__ == '__main__':
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()