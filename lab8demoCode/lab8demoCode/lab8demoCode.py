import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from myQueue import myQueue

q = myQueue()

def customer_view():
    customer = tk.Toplevel(root)
    customer.title("Customer View")
    customer.geometry("300x300")
    input = tk.Entry(customer)
    input.grid(row=0, column=0)
    queue = ttk.Combobox(customer)
    queue.grid(row=2, column=0)

    def addItem():
        item = input.get()
        q.push(item);
        updateQueue();

    def updateQueue():
        print("")
        queuevalues = q.contents()
        queue['values'] = queuevalues

    button = tk.Button(customer, text="Add Request", command = addItem).grid(row=1, column=0)

    


root = tk.Tk();
root.title("Start Window")
root.geometry("600x700")

customer_label = tk.Label(root, text="Open Customer View")
customer_label.grid(row=0, column=0)
customer_button = tk.Button(root, command=customer_view)
customer_button.grid(row=1, column=0)

root.mainloop()