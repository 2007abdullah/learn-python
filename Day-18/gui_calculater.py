import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except:
        result_label.config(text="Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("500x450")

entry1 = tk.Entry(root, width=70)
entry1.pack()

entry2 = tk.Entry(root, width=70)
entry2.pack()

btn = tk.Button(root, text="Add", command=calculate)
btn.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()






