import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.config(bg="#7B3F00") # Set the background color of the calculator
        
        # Create a frame to hold the display and buttons
        self.main_frame = tk.Frame(self.master, padx=10, pady=10, bg="#7B3F00")
        self.main_frame.pack(expand=True, fill=tk.BOTH)
        
        # Create a variable to hold the result
        self.result_var = tk.StringVar(value="")
        
        # Create a label to display the result
        self.result_label = tk.Label(self.main_frame, textvariable=self.result_var, font=("Arial", 24), bg="#7B3F00", fg="white")
        self.result_label.pack(expand=True, fill=tk.BOTH)
        
        # Create a frame to hold the buttons
        self.buttons_frame = tk.Frame(self.main_frame, bg="#7B3F00")
        self.buttons_frame.pack(expand=True, fill=tk.BOTH)
        
        # Create a list of buttons
        buttons = [
            "(", ")", "AC", "DEL",
            "sin", "cos", "tan", "^",
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            ".", "0", "=", "+"
        ]
        
        # Create a function to handle button clicks
        def button_click(button):
            if button == "AC":
                self.result_var.set("")
            elif button == "DEL":
                self.result_var.set(self.result_var.get()[:-1])
            elif button == "=":
                try:
                    self.result_var.set(str(eval(self.result_var.get())))
                except:
                    self.result_var.set("Error")
            elif button == "sin":
                try:
                    self.result_var.set(str(math.sin(float(self.result_var.get()))))
                except:
                    self.result_var.set("Error")
            elif button == "cos":
                try:
                    self.result_var.set(str(math.cos(float(self.result_var.get()))))
                except:
                    self.result_var.set("Error")
            elif button == "tan":
                try:
                    self.result_var.set(str(math.tan(float(self.result_var.get()))))
                except:
                    self.result_var.set("Error")
            elif button == "^":
                self.result_var.set(self.result_var.get() + "**")
            else:
                self.result_var.set(self.result_var.get() + button)
        
        # Create the buttons and add them to the frame
        for button in buttons:
            if button == "":
                tk.Label(self.buttons_frame, text=" ", font=("Arial", 12), width=5, height=2, bg="#7B3F00").grid(row=6, column=3)
            else:
                tk.Button(self.buttons_frame, text=button, font=("Arial", 12), width=5, height=2, command=lambda button=button: button_click(button), bg="#FFFDD0", fg="#7B3F00").grid(row=buttons.index(button)//4, column=buttons.index(button)%4)
        
# Create the application
root = tk.Tk()
calc = Calculator(root)

# Run the application
root.mainloop()
