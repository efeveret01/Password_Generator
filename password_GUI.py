import tkinter as tk
from pass_gen import passwordGen


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('Password Generator App')
        self.geometry('320x500')

        self.T = tk.Text(self, height=2, width=35)
        self.T.pack()
        self.T.insert(tk.END, "*At LEAST one box ticked below!")

        # label
        self.label = tk.Label(self, text='*At LEAST one box ticked below!')
        
        self.label.pack()

        self.label.configure(state="active")

        self.var1 = tk.IntVar()
        self.checkCap = tk.Checkbutton(self, text="lower Case", variable=self.var1)
        self.checkCap.pack()

        self.var2 = tk.IntVar()
        self.checkCap = tk.Checkbutton(self, text="Numbers", variable=self.var2)
        self.checkCap.pack()

        self.var3 = tk.IntVar()
        self.checkCap = tk.Checkbutton(self, text="Special Charaters", variable=self.var3)
        self.checkCap.pack()

        self.var4 = tk.IntVar()
        self.checkCap = tk.Checkbutton(self, text="Capital Letter", variable=self.var4)
        self.checkCap.pack()

        self.slider = tk.Scale(self, from_=5, to=20, orient='horizontal')
        self.slider.pack()


        # button
        self.button = tk.Button(self, text='Generate')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        arr = [int(self.var1.get()), int(self.var2.get()), int(self.var3.get()), int(self.var4.get())]
        posit = int(self.slider.get())
        passDragged = passwordGen(arr, posit)
        self.T.delete("1.0",tk.END)
        self.T.insert(tk.END, passDragged)


if __name__ == "__main__":
    app = App()
    app.mainloop()