import tkinter as tk
def factorial(num):return num * factorial(num - 1) if num > 0 else 1
root = tk.Tk()
root.geometry("250x180")
root.title("Find factorial")
tk.Label(master=root, text="Type here", fg="#34f",  font=("Arial", 16)).pack(pady=(20, 10))
ent = tk.Entry(width=30)
ent.pack()
result_lbl = tk.Label(text="The result will be shown here")
def Calc():
    input = int(ent.get())
    result = str(factorial(input)) if input >= 0 else "Are you crazy?"
    result_lbl.config(text=result)
btn = tk.Button(text="Calculate", fg="red", bg="#34f", command=Calc)
btn.pack(pady=(20, 20))
result_lbl.pack()
root.mainloop()