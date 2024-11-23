#tkinter is used for GUI
import tkinter as tk
#messagebox is currently unused but would be used for popup errors/warnings
from tkinter import messagebox
#ttk is used for 'combobox' which is a drop down menu, which we use for viewing available technicians or customer requests
from tkinter import ttk
#Custom data structures made in other files
from myQueue import myQueue
from myBST import myBST
from myHeap import myHeap

#queue data structure used for chronological order of customer requests
q = myQueue()
#binary tree data structure, used for sorting available technicians by their rating
btree = myBST()
#heap function class, used for manipulating the heapArr (heap array)
heap = myHeap()
#heap array, used to create a heap, and find the topmost element for the highest priority customer request
heapArr = []

#create techinician dictionary. each key is the technician name or id. Each item is an array

#Customer view window. Has the customer requests where customers can add requests and technicans can view them (in final project, these functionalities will be separated)
def customer_view():
    #tk.toplevel creates a new window on top of root window
    customer = tk.Toplevel(root)
    customer.title("Customer View")
    #geometry defines size of new window
    customer.geometry("300x300")

    customer.grid_columnconfigure(0, weight=1)

    #create dropdown box with available technicians
    BST = ttk.Combobox(customer, width=16, height=1)
    BST.grid(row=2, column=0)

    bstvalues = btree.getList()
    #update dropdown box with ordered elements
    BST['values'] = bstvalues

    #Create input field (text box) for adding new requests
    input = tk.Entry(customer, width=16)
    #order it in the window so it is topleft
    input.grid(row=0, column=0)

    
    #function to add new customer request after button press
    def addItem():
        #get item from string in textbox
        item = input.get()
        #push the item to the queue
        q.push(item);
        #push the item to the heap
        heapArr.append(item)    
        #Update the drop down list


    #button for adding new customer requests
    button = tk.Button(customer, text="Add Request", command = addItem, width=16, height=1)
    button.grid(row=1, column=0)


def admin_view():
    admin = tk.Toplevel(root)
    admin.title("Admin View")
    admin.geometry("300x300")
    
    selected_account = tk.StringVar()
    selected_account.set("")

    accounts = ttk.Combobox(admin, textvariable=selected_account, width=25, height=1)
    accounts.grid(row=0, column=0)

    def deleteItem():
        username = selected_account.get()
        username = username.split(" ")[0]
        index = usernames.index(username)
        usernames.pop(index)
        passwords.pop(index)
        roles.pop(index)
        updateList()
        selected_account.set("")

    def updateList():
        dropdown_q = myQueue()
        for i in range(len(usernames)):
            dropdown_q.push(usernames[i] + " " + passwords[i] + " " + roles[i])
        accounts['values'] = dropdown_q.contents()

    updateList()


    deleteButton = tk.Button(admin, text="Delete Account", command=deleteItem, width=25, height=1)
    deleteButton.grid(row=1,column=0)


        
#technician window. Customers can view available technicians, and technicians can add themselves (would be separated functionalities in final product)
def technician_view():
    #create new window
    technician = tk.Toplevel(root)
    technician.title("Technician View")
    technician.geometry("300x300")

    #Will display highest priority customer request upon buttom press. priorityText is a variable that stores the highest priority request
    priorityText = tk.StringVar()
    priorityText.set("")

    technician.grid_columnconfigure(0, weight=1)
    #create text box for input
    input = tk.Entry(technician, width=16)
    input.grid(row=0, column=0)

    #create a dropdown box with all the requests, ordered chronologically
    queue = ttk.Combobox(technician, width=16, height=1)
    queue.grid(row=3, column=0)
    #Text label to output the highest priority customer request
    priorityLabel = tk.Label(technician,textvariable = priorityText, width=16, height=1)
    priorityLabel.grid(row=4, column=0)

    #fetch items in the queue into queuevalues variable
    queuevalues = q.contents()
    #update the dropdown box contents with the queue contents
    queue['values'] = queuevalues

    #function to add item
    def addItem():
        #get text from textbox
        item = input.get()
        #clear the old list (NOT clearing binary tree, just the list) before reappending all elements in the sort
        btree.clearList()
        #add new element to binary tree
        btree.insert(item)
        #order elements and put them in the cleared list
        btree.inOrder(btree.getRoot())
        
        #get the highest priority customer request (upon button press)
    def getPriority():
        #build the heap from the array
        heap.buildHeap(heapArr)
        #Get the top most element and update the label
        priorityText.set(str(heapArr[0]))

    #Button to add new technicians
    button = tk.Button(technician, text="Add Technician", command = addItem, width=16, height=1)
    button.grid(row=1, column=0)

    #button for getting highest priority requests
    priorityButton = tk.Button(technician, text="Get Priority", command=getPriority, width=16, height=1)
    priorityButton.grid(row=2, column=0)

    
"""
root = tk.Tk();
root.title("Start Window")
root.geometry("300x300")

root.grid_columnconfigure(0, weight=1)

customer_label = tk.Label(root, text="Open Customer View",width=16, height=1)
customer_label.grid(row=0, column=0)
customer_button = tk.Button(root, command=customer_view, width=16, height=1)
customer_button.grid(row=1, column=0)

technician_label = tk.Label(root, text="Open Technician View",width=16, height=1)
technician_label.grid(row=2, column=0)
technician_button = tk.Button(root, command=technician_view, width=16, height=1)
technician_button.grid(row=3, column=0)
"""

def login():
    u = username_input.get()
    p = password_input.get()

    if u in usernames:
        i = usernames.index(u)
        print(i)

        if p == passwords[i]:
            print(roles[i])
            openWindow(roles[i])
            
def openWindow(role):
    if role == 'Admin':
        admin_view()
    elif role == 'Technician':
        technician_view()
    elif role == 'Customer':
        customer_view()

usernames = ['admin1', 'technician1', 'customer1']
passwords = ['adminpass', 'technicianpass', 'customerpass']
roles = ['Admin', 'Technician', 'Customer']

root = tk.Tk()
root.title("Login Window")
root.geometry("300x300")

root.grid_columnconfigure(0, weight=1)

username_label = tk.Label(root, text="Username", width=16, height=1)
username_label.grid(row=0, column=0)
username_input = tk.Entry(root, width=16)
username_input.grid(row=1, column=0)

password_label = tk.Label(root, text="Password", width=16, height=1)
password_label.grid(row=2, column=0)
password_input = tk.Entry(root, show="*", width=16)
password_input.grid(row=3, column=0)

login_button = tk.Button(root, text="Login", command = login, width = 16, height=1)
login_button.grid(row=4, column=0)



root.mainloop()