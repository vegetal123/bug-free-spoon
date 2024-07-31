from tkinter import *

def calculate_fibonacci():
    try:
        num = int(entry.get())
        if num < 0:
            result_label.config(text="Please enter a positive number.")
            return
        a, b = 0, 1
        fib_series = [a]
        sum_fib = a
        for _ in range(1, num):
            a, b = b, a + b
            fib_series.append(a)
            sum_fib += a
        result_label.config(text="Fibonacci Series: " + str(fib_series))
        sum_label.config(text="Sum: " + str(sum_fib))
    except ValueError:
        result_label.config(text="Please enter a valid number.")

root = Tk()
root.title("Fibonacci Generator")
root.geometry("400x300")

entry = Entry(root, width=20)
entry.pack(pady=10)

calculate_button = Button(root, text="Calculate", command=calculate_fibonacci)
calculate_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack(pady=10)

sum_label = Label(root, text="")
sum_label.pack(pady=10)

root.mainloop()
