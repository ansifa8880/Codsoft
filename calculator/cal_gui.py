import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Ansi's Calculator")
        master.geometry("400x300")  # Set the size of the window
        master.configure(bg='light pink')  # Set the background color

        # Create entry fields for numbers
        self.num1_label = tk.Label(master, text="Number 1:", bg='light pink', fg="white")
        self.num1_label.grid(row=0, column=0, padx=10, pady=10)
        self.num1_entry = tk.Entry(master, width=20, bg="#FFDAB9", fg="black")
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)

        self.num2_label = tk.Label(master, text="Number 2:", bg='light pink', fg="white")
        self.num2_label.grid(row=1, column=0, padx=10, pady=10)
        self.num2_entry = tk.Entry(master, width=20, bg="#FFDAB9", fg="black")
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create operation buttons
        self.operation_frame = tk.Frame(master, bg='light pink')
        self.operation_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.operations = {
            1: lambda x, y: x + y,
            2: lambda x, y: x - y,
            3: lambda x, y: x * y,
            4: lambda x, y: x / y if y != 0 else "Error: Division by zero is not allowed"
        }

        self.add_button = tk.Button(self.operation_frame, text="+", command=lambda: self.calculate(1), width=5, height=2, bg="#F0F0F0", fg="black")
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.sub_button = tk.Button(self.operation_frame, text="-", command=lambda: self.calculate(2), width=5, height=2, bg="#F0F0F0", fg="black")
        self.sub_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.mul_button = tk.Button(self.operation_frame, text="*", command=lambda: self.calculate(3), width=5, height=2, bg="#F0F0F0", fg="black")
        self.mul_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.div_button = tk.Button(self.operation_frame, text="/", command=lambda: self.calculate(4), width=5, height=2, bg="#F0F0F0", fg="black")
        self.div_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.clear_button = tk.Button(self.operation_frame, text="Clear", command=self.clear, width=10, height=2, bg="#F0F0F0", fg="black")
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create result label
        self.result_label = tk.Label(master, text="Result:", bg='light pink', fg="white")
        self.result_label.grid(row=3, column=0, padx=10, pady=10)
        self.result_entry = tk.Entry(master, width=20, bg="#FFDAB9", fg="black")
        self.result_entry.grid(row=3, column=1, padx=10, pady=10)

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = self.operations[operation](num1, num2)
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, str(result))
        except ValueError:
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, "Error: Invalid input")

    def clear(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result_entry.delete(0, tk.END)

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()
