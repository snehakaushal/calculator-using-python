import tkinter as tk
from math import sqrt

def click(text):
    try:
        if text == "=":
            expression = entry.get()
            if "%" in expression:
                expression = expression.replace("%", "/100")
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        elif text == "C":
            entry.delete(0, tk.END)
        elif text == "⌫":  # Backspace
            current = entry.get()
            entry.delete(0, tk.END)
            entry.insert(0, current[:-1])
        elif text == "√":
            result = str(sqrt(float(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        elif text == "x²":
            result = str(float(entry.get())**2)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        else:
            entry.insert(tk.END, text)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("360x500")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

entry = tk.Entry(root, font=("Arial", 24), justify="right", bd=5, relief="sunken")
entry.pack(fill="both", padx=10, pady=20, ipady=10)

buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["x²", "0", ".", "="],
    ["√"]  # This will be a special wider button
]

main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(expand=True, fill="both")

# Create the first 5 rows with 4 buttons each
for i, row in enumerate(buttons[:-1]):  # All rows except the last one
    frame = tk.Frame(main_frame, bg="#f0f0f0")
    frame.pack(expand=True, fill="both")
    for b in row:
        btn = tk.Button(frame, text=b, font=("Arial", 20), fg="#333", bg="#e0e0e0", 
                       activebackground="#d0d0d0", command=lambda x=b: click(x))
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

# Create the last row with just the square root button that spans the full width
last_frame = tk.Frame(main_frame, bg="#f0f0f0")
last_frame.pack(expand=True, fill="both")
btn = tk.Button(last_frame, text="√", font=("Arial", 20), fg="#333", bg="#e0e0e0",
               activebackground="#d0d0d0", command=lambda: click("√"))
btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

root.mainloop()