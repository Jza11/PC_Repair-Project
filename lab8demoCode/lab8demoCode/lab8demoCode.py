#IDEAS TO FIX STUFF IN FUTURE
#Create the heap, queue, bst upon opening technician / customer menu. select from just a normal list or queue all the elements with
#the technician id, then from that list create the data structures
#Maybe just have each customer put their listings with their desired price and contact information,
#and same with technicians, they upload their listing with their price and contact information, and then the communication
#can be facilitated elsewhere

#USERNAMES AND PASSWORDS ARE: admin1:adminpass, technician1:technicianpass, customer1:customerpass

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

#queue data structure used for chronological order of customer requests, and accounts created (in admin view)
q = myQueue()
#binary tree data structure, used for sorting available technicians by their rating
btree = myBST()
#heap function class, used for manipulating the heapArr (heap array) (viewing highest priority customer request)
heap = myHeap()
#heap array, used to create a heap, and find the topmost element for the highest priority customer request
heapArr = []

#Customer view window. Has the customer requests where customers can add requests and view technicians
def customer_view():
    #tk.toplevel creates a new window on top of root window
    customer = tk.Toplevel(root)
    customer.title("Customer View")
    #geometry defines size of new window
    customer.geometry("300x300")

    #configure layout of window so there is just one column
    customer.grid_columnconfigure(0, weight=1)

    #create dropdown box with available technicians
    BST = ttk.Combobox(customer, height=1)
    BST.grid(row=2, column=0, sticky="ew", padx=40)

    #fetch ordered list from btree
    bstvalues = btree.getList()
    #update dropdown box with ordered elements
    BST['values'] = bstvalues

    #Create input field (text box) for adding new requests
    input = tk.Entry(customer)
    #order it in the window so it is topleft
    input.grid(row=0, column=0, sticky="ew", padx=40)

    
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
    button = tk.Button(customer, text="Add Request", command = addItem, height=1)
    button.grid(row=1, column=0, sticky="ew", padx=40)

#Admin window, where new accounts are created or deleted
def admin_view():
    #create new admin window on top of root (new window based on main window)
    admin = tk.Toplevel(root)
    #title, and size of window
    admin.title("Admin View")
    admin.geometry("300x300")
    
    #configure window so there is only one column
    admin.grid_columnconfigure(0, weight=1)

    #variables for dropdown boxes. Allows you to fetch whatever option the user chooses. Initialized as tk string object,
    #and set to "" by default
    selected_account = tk.StringVar()
    selected_account.set("")
    selected_role = tk.StringVar()
    selected_role.set("")

    #username label above input box
    usernameLabel = tk.Label(admin, text="Username", height=1)
    usernameLabel.grid(row=0,column=0)
    #username input box
    usernameInput = tk.Entry(admin)
    usernameInput.grid(row=1, column=0, sticky="ew", padx=40)

    #password label above password box
    passwordLabel = tk.Label(admin, text="Password", height=1)
    passwordLabel.grid(row=2,column=0)
    #password input box
    passwordInput = tk.Entry(admin)
    passwordInput.grid(row=3, column=0, sticky="ew", padx=40)

    #role label above role box
    roleLabel = tk.Label(admin, text="Role", height=1)
    roleLabel.grid(row=4,column=0)
    #role selection box
    roleInput = ttk.Combobox(admin, textvariable=selected_role)
    roleInput.grid(row=5, column=0, sticky="ew", padx=40)
    #Set default values for the role dropdown box
    roleInput['values'] = ['Admin', 'Technician', 'Customer']
    
    
    #add item function to add new accounts
    def addItem():
        #get username, pasword, role from the input boxes above
        username = usernameInput.get()
        password = passwordInput.get()
        role = roleInput.get()

        #put collected values into the username,password,and role lists (defined below by the root window)
        usernames.append(username)
        passwords.append(password)
        roles.append(role)
        #update the drop down of all accounts to reflect the new account
        updateList()

    #delete accounts
    def deleteItem():
        #get the selected account from the dropdown box (in format of 'username password role')
        username = selected_account.get()
        #split the string into a list based on where the spaces are (in format of username = ['username', 'password', 'role']),
        #and then get the first index of this list (username[0]) (which will just be the username component)
        username = username.split(" ")[0]
        #find the index of the username in the usernames list
        index = usernames.index(username)
        #remove the username from the usernames list
        usernames.pop(index)
        #remove the associated password from the passwords array
        passwords.pop(index)
        #remove the associated role from the roles array
        roles.pop(index)
        #update the dropdown box to reflect these changes
        updateList()
        #reset the dropdown box so the deleted account is no longer selected
        selected_account.set("")

    #update the list
    def updateList():
        #create a new queue object
        dropdownQ = myQueue()
        #loop through all usernames, add to the new queue a string which contains username and associated password and role
        for i in range(len(usernames)):
            dropdownQ.push(usernames[i] + " " + passwords[i] + " " + roles[i])
        #update accounts dropdown box with queue contents
        accounts['values'] = dropdownQ.contents()

    #button to create accounts. when it is pressed then run the 'addItem' function
    createButton = tk.Button(admin, text="Create Account", command=addItem, height=1)
    createButton.grid(row=6,column=0, sticky="ew", padx=40)


    accountsLabel = tk.Label(admin, text="Accounts", height=1)
    accountsLabel.grid(row=7,column=0)
    #accounts dropdown box (existing accounts). If one is selected, then can be deleted with delete button below
    accounts = ttk.Combobox(admin, textvariable=selected_account, height=1)
    accounts.grid(row=8, column=0, sticky="ew", padx=40)

   
    #update the list upon first opening the window
    updateList()

    #delete button to delete accounts. runs 'deleteItem' function when pressed
    deleteButton = tk.Button(admin, text="Delete Account", command=deleteItem, height=1)
    deleteButton.grid(row=9,column=0, sticky="ew", padx=40)
    
#technician window. Technicians can add themselves and view customer requests
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
    inputLabel = tk.Label(technician,text="Add New Service", height=1)
    inputLabel.grid(row=0, column=0)
    input = tk.Entry(technician)
    input.grid(row=1, column=0, sticky="ew", padx=40)



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
    button = tk.Button(technician, text="Add Service", command = addItem, height=1)
    button.grid(row=2, column=0, sticky="ew", padx=40)

    queueLabel = tk.Label(technician,text="Customer Requests", height=1)
    queueLabel.grid(row=3, column=0)
    #create a dropdown box with all the requests, ordered chronologically
    queue = ttk.Combobox(technician, height=1)
    queue.grid(row=4, column=0, sticky="ew", padx=40)

    #Text label to output the highest priority customer request
    priorityLabel = tk.Label(technician,textvariable = priorityText, height=1)
    priorityLabel.grid(row=5, column=0)

    #fetch items in the queue into queuevalues variable
    queuevalues = q.contents()
    #update the dropdown box contents with the queue contents
    queue['values'] = queuevalues

    #button for getting highest priority requests
    priorityButton = tk.Button(technician, text="Get Priority", command=getPriority, height=1)
    priorityButton.grid(row=6, column=0, sticky="ew", padx=40)

#hardware menu to buy and sell hardware (view hardware and contact seller outside the app)
def hardware_view():
    #create hardware window on top of root (main window)
    hardware = tk.Toplevel(root)
    #title and size of new window
    hardware.title("Hardware View")
    hardware.geometry("600x600")
    
    #configure window so it is just one column
    hardware.grid_columnconfigure(0, weight=1)

    #create variables for dropdown menus so that you can access what ever option the user selects
    selected_hardware = tk.StringVar()
    selected_hardware.set("")
    selected_condition = tk.StringVar()
    selected_condition.set("")
    selected_listing = tk.StringVar()
    selected_listing.set("")

    #list to store created listings
    listings = []

    #hardware label for field to input the type
    hardwareLabel = tk.Label(hardware, text="Type of Hardware", height=1)
    hardwareLabel.grid(row=0,column=0)
    #hardware input box
    hardwareInput = ttk.Combobox(hardware, textvariable=selected_hardware, width=13)
    hardwareInput.grid(row=1, column=0, sticky="ew", padx=40)
    #hardware input box default values
    hardwareInput['values'] = ['Monitor', 'Mouse', 'Keyboard', 'GPU', 'CPU', 'RAM', 'Motherboard']

    #price label and input box
    priceLabel = tk.Label(hardware, text="Price ($)", height=1)
    priceLabel.grid(row=2,column=0)
    priceInput = tk.Entry(hardware, width=13)
    priceInput.grid(row=3, column=0, sticky="ew", padx=40)

    #condition label and input box
    conditionLabel = tk.Label(hardware, text="Condition", height=1)
    conditionLabel.grid(row=4,column=0)
    conditionInput = ttk.Combobox(hardware, textvariable=selected_condition, width=13)
    conditionInput.grid(row=5, column=0, sticky="ew", padx=40)
    #condition input box default values
    conditionInput['values'] = ['Like New', 'Good', 'Used', 'Functional', 'Poor', 'For Parts']

    #contact label and contact input box
    contactLabel = tk.Label(hardware, text="Contact Information", height=1)
    contactLabel.grid(row=6,column=0)
    contactInput = tk.Entry(hardware)
    contactInput.grid(row=7, column=0, sticky="ew", padx=40)

    #description label and input box
    descriptionLabel = tk.Label(hardware, text="Description", height=1)
    descriptionLabel.grid(row=8,column=0)
    descriptionInput = tk.Entry(hardware)
    descriptionInput.grid(row=9, column=0, sticky="ew", padx=40)

    #listingsDropdown = ttk.Combobox(hardware, textvariable=selected_listing, width=26, height=1)

    #function to add new listings
    def addItem():
        #get hardware, price, condition, etc from above input boxes
        hardwareType = hardwareInput.get()
        price= priceInput.get()
        condition = conditionInput.get()
        contact = contactInput.get()
        description = descriptionInput.get()

        #add the new listing to the listings list
        listings.append(hardwareType + " | $" + price + " | " + condition + " | " + contact + " | " + description)
        #update the listingbox(defined below) to reflect changes
        updateList()

    #update the listing box with new list values
    def updateList():
        #dropdownQ = myQueue()
        #clear the old listingbox (delete elements from 0 to the end)
        listingsDropdown.delete(0, tk.END)
        for i in range(len(listings)):
            #dropdownQ.push(listings[i])
            #loop through and insert new listings starting at the end of the listingbox
            listingsDropdown.insert(tk.END, listings[i])
        #listingsDropdown['values'] = dropdownQ.contents()

    #button to create listings
    createButton = tk.Button(hardware, text="Add Listing", command=addItem, height=1)
    createButton.grid(row=10,column=0, sticky="ew", padx=40)

    #label for listingbox
    listingsLabel = tk.Label(hardware, text="Listings", height=1)
    listingsLabel.grid(row=11,column=0)
    #listingbox
    listingsDropdown = tk.Listbox(hardware)
    listingsDropdown.grid(row=12, column=0, sticky="ews", padx=40, pady=(10,20))

    updateList()

    
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

#Main root window & functions

#login function. run when login button is pressed. checks if username and password match existing one
def login():
    #get username and password from username and password input (both defined below)
    u = username_input.get()
    p = password_input.get()

    #check if username exists in the usernames list (also defined below)
    if u in usernames:
        #if it exists, find the index
        i = usernames.index(u)
        print(i)
        # if the password matches the same index that the username was found at, then open the corresponding role
        if p == passwords[i]:
            print(roles[i])
            openWindow(roles[i])
#check the role of hte user, and open the corresponding window
def openWindow(role):
    if role == 'Admin':
        admin_view()
    elif role == 'Technician':
        technician_view()
    elif role == 'Customer':
        customer_view()

#username, password, and roles array. index based, so username[0]'s password is password[0] and has role[0]
usernames = ['admin1', 'technician1', 'customer1']
passwords = ['adminpass', 'technicianpass', 'customerpass']
roles = ['Admin', 'Technician', 'Customer']

#root window
root = tk.Tk()
root.title("Login Window")
root.geometry("300x300")

#configure root window so it has one column
root.grid_columnconfigure(0, weight=1)

#username label and input box
username_label = tk.Label(root, text="Username", width=16, height=1)
username_label.grid(row=0, column=0)
username_input = tk.Entry(root, width=16)
username_input.grid(row=1, column=0, sticky="ew", padx=40)

#password label and input box
password_label = tk.Label(root, text="Password", width=16, height=1)
password_label.grid(row=2, column=0)
password_input = tk.Entry(root, show="*", width=16)
password_input.grid(row=3, column=0, sticky="ew", padx=40)

#login button
login_button = tk.Button(root, text="Login", command = login, width = 16, height=1)
login_button.grid(row=4, column=0, sticky="ew", padx=40)

hardware_button = tk.Button(root, text="Hardware", command = hardware_view, width = 16, height=1)
hardware_button.grid(row=5, column=0, sticky="ew", padx=40)


root.mainloop()