#IDEAS TO FIX STUFF IN FUTURE
#Create the heap, queue, bst upon opening technician / customer menu. select from just a normal list or queue all the elements with
#the technician id, then from that list create the data structures
#Maybe just have each customer put their listings with their desired price and contact information,
#and same with technicians, they upload their listing with their price and contact information, and then the communication
#can be facilitated elsewhere

#USERNAMES AND PASSWORDS ARE: admin1:apass, tech1:tpass, cust1:cpass

#tkinter is used for GUI
from pickle import FALSE, TRUE
import re
import tkinter as tk
#messagebox is currently unused but would be used for popup errors/warnings
from tkinter import messagebox
#ttk is used for 'combobox' which is a drop down menu, which we use for viewing available technicians or customer requests
from tkinter import ttk
#Custom data structures made in other files
from myQueue import myQueue
from myBST import myBST
from myHeap import myHeap
#Resources needed for the creation of the database
import sqlite3

#This function takes as an input an array that represent all the data fields inside the table example data=["Zaf", GFTYS9, Admin]
#and then insert the values into the table so that the data is stored and saved.
def Add_User_db(data): 
    
    #Connection to the dabase 
    PC_Repair_Connection=sqlite3.connect("PC_Repair.db")
    
    #Implementation of cursor
    cur=PC_Repair_Connection.cursor()
    
    #Insert statement to add the information of the user 
    cur.execute("""INSERT INTO user_t(username, password, class) VALUES (?, ?, ?)""", data)

    #Commiting all the changes done to the tables and the database
    PC_Repair_Connection.commit()
    
    #After all the changes are done, the database connection need to be closed. 
    PC_Repair_Connection.close()
#this function add
def Add_request_db(request_information):
    
    #Connection to the database
    PC_Repair_Connection=sqlite3.connect("PC_Repair.db")
    
    #Cursor Creation to navigate into the tuples of the table
    cur=PC_Repair_Connection.cursor()

    #Statement for the insertion of data inside the request table, taking argument as follows:
    #request_information("Severe, Hardware, 200.2, josemjgsg@gmail.com, My computer got fried")
    cur.execute("""INSERT INTO request_t(severity_degree, type_request, price, u_email, explanation) 
                                     VALUES (?, ?, ?, ?, ?)""", request_information)
    #Commiting all the changes into the database
    
    PC_Repair_Connection.commit()
    
    #After all the changes were done, the database connection is closed
    PC_Repair_Connection.close()
#This is to add a tuple to the technician table
def Add_technician_db(technician_info):
    
    #Connection to the database
    PC_Repair_Connection=sqlite3.connect("PC_Repair.db")
    
    #Cursor Creation to navigate into the tuples of the table
    cur=PC_Repair_Connection.cursor()
    
    #Statement to enter the information from the technician in such a way that 
    #Technician_info=[5, Novice, worker12@gmail, Operating system of Computer]
    cur.execute("""INSERT INTO technician_t(Service_type, price_aprox, rating, contact_info, description) 
                                      VALUES (?,?,?,?,?) """, technician_info)
    
    #Commiting all the changes into the database
    PC_Repair_Connection.commit()
    
    #After all the changes were done, the database connection is closed
    PC_Repair_Connection.close()
#this function is to add a tuple to the hardware table
def Add_hardware_db(hardware_info):
    
    #Connection to the database
    PC_Repair_Connection=sqlite3.connect("PC_Repair.db")
    
    #Cursor Creation to navigate into the tuples of the table
    cur=PC_Repair_Connection.cursor()

    #statemnet to enter the information for the hardware piece inside the datavase, in such a way that 
    #hardware_info=[Monitor, 130.1, New, arigatoEnt@gmail, Monitor to play any videogame in good quality]
    cur.execute("""INSERT INTO hardware_t(type, price, condition, contact_email, description) 
                                      VALUES (?,?,?,?,?)""", hardware_info)
    
    #Commiting all the changes into the database
    PC_Repair_Connection.commit()
    
    #After all the changes were done, the database connection is closed
    PC_Repair_Connection.close()
#Function to eliminate a username from the database.
def eliminate_user_db(username):
   
   #Connection to the database
    PC_Repair_Connection=sqlite3.connect("PC_Repair.db")
    
    #Cursor Creation to navigate into the tuples of the table
    cur=PC_Repair_Connection.cursor()

    #Statement to eliminate the usename from the database
    cur.execute("""DELETE FROM user_t WHERE username=?""", (username,))
    
    #Commiting all the changes into the database
    PC_Repair_Connection.commit()
    
    #After all the changes were done, the database connection is closed
    PC_Repair_Connection.close()
#Function to get all user information from the database 
def User_Get_Values_from_db():
    #Connection with the database
    PC_Repair_Con=sqlite3.connect("PC_Repair.db")
    #Creation of the cursor
    cur=PC_Repair_Con.cursor()
    #Statement to execute
    statement=cur.execute("""SELECT * FROM user_t""")
    #Getting all the values from the query
    data_user=statement.fetchall()
    #Return all the tuples
    return data_user
#Function to get all hardware information from the database
def Hardware_Values_from_db():
    #Connection with the database
    PC_Repair_Con=sqlite3.connect("PC_Repair.db")
    #Creation of the cursor
    cur=PC_Repair_Con.cursor()
    #Statement to be executed
    statement=cur.execute("""SELECT * FROM hardware_t""")
    #Getting all the values from the query
    data_hardware=statement.fetchall()
    #Return all the tuples
    return data_hardware
#Function to get all tecnician services from the database
def Technician_Values_from_db():
     #Connection with the database
    PC_Repair_Con=sqlite3.connect("PC_Repair.db")
    #Creation of the cursor
    cur=PC_Repair_Con.cursor()
    #Statement to be executed
    statement=cur.execute("""SELECT * FROM technician_t""")
    #Getting all the values from the query
    data_technician=statement.fetchall()
    #Return all the tuples
    return data_technician
#Function to get all requests from the database
def Requests_Values_from_db():
    #Connection with the database
    PC_Repair_Con=sqlite3.connect("PC_Repair.db")
    #Creation of the cursor
    cur=PC_Repair_Con.cursor()
    #Statement to be executed
    statement=cur.execute("""SELECT * FROM request_t""")
    #Getting all the values from the query
    data_requests=statement.fetchall()
    #Return all the tuples
    return data_requests

def Build_Customer_request_format(data_request):
    #Array that will take all the strings with the data fields combined
    formated_data=[]
    for row in data_request:
        #row[1]=Severity, row[2]=requet_type, row[3]=Price_offered, row[4]=Contact_info and row[5]=Problem_Description
        new_row=row[1] + "|" + row[2] + "|" + str(row[3]) +"$ |" + row[4] + "|" + row[5]
        #Adding the new_row of the current iteration to the array
        formated_data.append(new_row)
    return formated_data

def Build_technician_data(data_technician):
    #Array that will store the data in the desired format
    formated_data=[]
    for row in data_technician:
        #row[3]=Rating, row[1]=service_type, row[2]=Price, row[4]=contact_info, row[5]=Field of expertise
        new_row=row[3] + "|" + row[1] +"|"+ str(row[2]) + "|"+row[4]+"|"+ row[5]
        formated_data.append(new_row)
    return formated_data

def Build_Hardware_data(data_hardware):
    #Array that will store the data in the desired format
    formated_data=[]
    for row in data_hardware:
        new_row=row[1]+"|"+str(row[2])+"|"+row[3]+"|"+row[4]+"|"+row[5]
        formated_data.append(new_row)
    return formated_data

#DATA STRUCTURES WITH SAMPLE DATA
#queue data structure used for chronological order of customer requests, and accounts created (in admin view)
q = myQueue()
#btree function class, used for manipulation of the data from the technician from customer view
btree = myBST()

#heap function class, used for manipulating the heapArr (heap array) (viewing highest priority customer request)
heap = myHeap()
# hardwareType + " | $" + price + " | " + condition + " | " + contact + " | " + description
#listings = ["Monitor | 180 | Like New | bob@gmail.com | acer 27 inch monitor fcfs",
            #"GPU | 220 | Good | redsam@gmail.com | nvidia gtx 970 runs well and cool",
            #"Motherboard | 100 | Used | joeyman21@gmail.com | acer motherboard. not sure what model",]

#Customer view window. Has the customer requests where customers can add requests and view technicians
def customer_view():
    technician_data=Technician_Values_from_db()
    tech_data_format=Build_technician_data(technician_data)
    
    for i in range(len(tech_data_format)):
        btree.insert(tech_data_format[i])
    btree.inOrder(btree.getRoot())
    
    
    #tk.toplevel creates a new window on top of root window
    customer = tk.Toplevel(root)
    customer.title("Customer View")
    #geometry defines size of new window
    customer.geometry("800x600")

    #configure layout of window so there is just one column
    customer.grid_columnconfigure(0, weight=1)

    #create variables for dropdown menus so that you can access what ever option the user selects
    selected_request = tk.StringVar()
    selected_request.set("")
    selected_condition = tk.StringVar()
    selected_condition.set("")
    selected_listing = tk.StringVar()
    selected_listing.set("")

    #request label for field to input the type
    requestLabel = tk.Label(customer, text="Type of Request", height=1)
    requestLabel.grid(row=0,column=0)
    #request input box
    requestInput = ttk.Combobox(customer, textvariable=selected_request, width=13)
    requestInput.grid(row=1, column=0, sticky="ew", padx=40)
    #request input box default values
    requestInput['values'] = ['Software', 'Hardware']

    #price label and input box
    priceLabel = tk.Label(customer, text="Max Price Range ($)", height=1)
    priceLabel.grid(row=2,column=0)
    priceInput = tk.Entry(customer, width=13)
    priceInput.grid(row=3, column=0, sticky="ew", padx=40)

    #condition label and input box
    conditionLabel = tk.Label(customer, text="Severity", height=1)
    conditionLabel.grid(row=4,column=0)
    conditionInput = ttk.Combobox(customer, textvariable=selected_condition, width=13)
    conditionInput.grid(row=5, column=0, sticky="ew", padx=40)
    #condition input box default values
    conditionInput['values'] = ['1-Minor', '2-Unsure', '3-Medium', '4-Severe']

    #contact label and contact input box
    contactLabel = tk.Label(customer, text="Contact Information", height=1)
    contactLabel.grid(row=6,column=0)
    contactInput = tk.Entry(customer)
    contactInput.grid(row=7, column=0, sticky="ew", padx=40)

    #description label and input box
    descriptionLabel = tk.Label(customer, text="Description", height=1)
    descriptionLabel.grid(row=8,column=0)
    descriptionInput = tk.Entry(customer)
    descriptionInput.grid(row=9, column=0, sticky="ew", padx=40)
    
    #function to add new customer request after button press
    def addItem():
        #get request, price, condition, etc from above input boxes
        requestType = requestInput.get()
        price= priceInput.get()
        condition = conditionInput.get()
        contact = contactInput.get()
        description = descriptionInput.get()
        
        #Array storing the info of the customer request
        item_info=[condition, requestType, price, contact, description]

        #Add the element to the database
        Add_request_db(item_info)
        Update_Client_input()

    def Update_Client_input():
        selected_request.set("")
        priceInput.delete(0, tk.END)
        contactInput.delete(0, tk.END)
        descriptionInput.delete(0, tk.END)
        selected_condition.set("")




    
    #button for adding new customer requests
    button = tk.Button(customer, text="Add Request", command = addItem, height=1)
    button.grid(row=10, column=0, sticky="ew", padx=40)

    BSTLabel = tk.Label(customer, text="Available Technicians", height=1)
    BSTLabel.grid(row=11,column=0, pady=(10,0))
    #create dropdown box with available technicians
    BST = tk.Listbox(customer)
    BST.grid(row=12, column=0, sticky="sew", padx=40, pady=(0,20))

    #fetch ordered list from btree
    bstvalues = btree.getList()
    #update dropdown box with ordered elements
    for i in range(len(bstvalues)):
        BST.insert(tk.END, bstvalues[i])

    #button to open hardware view inside customer view 
    hardware_button = tk.Button(customer, text="Hardware Marketplace", command = hardware_view, width = 16, height=1)
    hardware_button.grid(row=13, column=0, sticky="ew", padx=40)

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
        
        #info from the username is stored in a array
        username_info=[username, password, role]
        #user info is stored into the database
        Add_User_db(username_info)

        #update the drop down of all accounts to reflect the new account
        updateList()
        #Function to update the input boxes so that they reset everytime the button is pressed
        Update_input()



    #delete accounts
    def deleteItem():
        #get the selected account from the dropdown box (in format of 'username role')
        username = selected_account.get()
        #split the string into a list based on where the spaces are (in format of username = ['username', 'role']),
        #and then get the first index of this list (username[0]) (which will just be the username component)
        username = username.split(" ")[0]

        #Eliminate user from the database
        eliminate_user_db(username)
        #Update for the Combobox.
        updateList()
        #reset the dropdown box so the deleted account is no longer selected
        selected_account.set("")

    #update the list
    def updateList():
        
        #create a new queue object
        dropdownQ = myQueue()
        #Update the values into tge Users_info variable
        Users_Info=User_Get_Values_from_db()
        #loop through all usernames, add to the new queue a string which contains username and role associated with it.
        for row in Users_Info:
            dropdownQ.push(row[1] + " " + row[3])
        #update accounts dropdown box with queue contents
        accounts['values'] = dropdownQ.contents()

    def Update_input():
        selected_role.set("")
        passwordInput.delete(0, tk.END)
        usernameInput.delete(0, tk.END)


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
    #Everytime the window opens, it gets the values from the database, build the heap for the customer request
    #And get the queue to see all the request by FIFO
    customer_requests=Requests_Values_from_db()
    heapArr=Build_Customer_request_format(customer_requests)
    for i in range(len(heapArr)):
         q.push(heapArr[i])
    heap.buildHeap(heapArr)

    #create new window
    technician = tk.Toplevel(root)
    technician.title("Technician View")
    technician.geometry("800x600")

    #Will display highest priority customer request upon buttom press. 
    #priorityText is a variable that stores the highest priority request
    priorityText = tk.StringVar()
    priorityText.set("")

    technician.grid_columnconfigure(0, weight=1)

    #create variables for dropdown menus so that you can access what ever option the user selects
    selected_request = tk.StringVar()
    selected_request.set("")
    selected_condition = tk.StringVar()
    selected_condition.set("")
    selected_listing = tk.StringVar()
    selected_listing.set("")

    #service label for field to input the type
    serviceLabel = tk.Label(technician, text="Type of Service", height=1)
    serviceLabel.grid(row=0,column=0)
    #service input box
    serviceInput = ttk.Combobox(technician, textvariable=selected_request, width=13)
    serviceInput.grid(row=1, column=0, sticky="ew", padx=40)
    #service input box default values
    serviceInput['values'] = ['Software', 'Hardware']

    #price label and input box
    priceLabel = tk.Label(technician, text="Approx. Service Price ($)", height=1)
    priceLabel.grid(row=2,column=0)
    priceInput = tk.Entry(technician)
    priceInput.grid(row=3, column=0, sticky="ew", padx=40)

    #condition label and input box
    conditionLabel = tk.Label(technician, text="Rating", height=1)
    conditionLabel.grid(row=4,column=0)
    conditionInput = ttk.Combobox(technician, textvariable=selected_condition, width=13)
    conditionInput.grid(row=5, column=0, sticky="ew", padx=40)
    #condition input box default values
    conditionInput['values'] = ['1-Learning', '2-Intermediate', '3-Experienced', '4-Novice', '5-Professional']

    #contact label and contact input box
    contactLabel = tk.Label(technician, text="Contact Information", height=1)
    contactLabel.grid(row=6,column=0)
    contactInput = tk.Entry(technician)
    contactInput.grid(row=7, column=0, sticky="ew", padx=40)

    #description label and input box
    descriptionLabel = tk.Label(technician, text="Description", height=1)
    descriptionLabel.grid(row=8,column=0)
    descriptionInput = tk.Entry(technician)
    descriptionInput.grid(row=9, column=0, sticky="ew", padx=40)
    
    #function to add new customer request after button press
    def addItem():
        #get service, price, condition, etc from above input boxes
        serviceType = serviceInput.get()
        price= priceInput.get()
        condition = conditionInput.get()
        contact = contactInput.get()
        description = descriptionInput.get()
        item = condition + " | " + serviceType + " | $" + price + " | " + contact + " | " + description
        
        #Array to store the values of the desired datafields 
        technician_info=[serviceType, price, condition ,contact, description]
        #Add user to the database
        Add_technician_db(technician_info)

        btree.clearList()
        btree.insert(item)
        btree.inOrder(btree.getRoot())

        Update_Input_Tech()

    def Update_Input_Tech():
        selected_request.set("")
        priceInput.delete(0, tk.END)
        selected_condition.set("")
        contactInput.delete(0, tk.END)
        descriptionInput.delete(0, tk.END)


    #get the highest priority customer request (upon button press)
    def getPriority():
        #build the heap from the array
        heap.buildHeap(heapArr)
        #Get the top most element and update the label
        priorityText.set(str(heapArr[0]))

    #Button to add new technicians
    button = tk.Button(technician, text="Add Service", command = addItem, height=1)
    button.grid(row=10, column=0, sticky="ew", padx=40)

    queueLabel = tk.Label(technician,text="Customer Requests", height=1)
    queueLabel.grid(row=11, column=0)
    #create a dropdown box with all the requests, ordered chronologically
    queue = tk.Listbox(technician)
    queue.grid(row=12, column=0, sticky="ew", padx=40)

    #Text label to output the highest priority customer request
    priorityLabel = tk.Label(technician,textvariable = priorityText, height=1)
    priorityLabel.grid(row=13, column=0)

    #fetch items in the queue into queuevalues variable
    queuevalues = q.contents()
    #update the dropdown box contents with the queue contents
    for i in range(len(queuevalues)):
        queue.insert(tk.END, queuevalues[i])

    #button for getting highest priority requests
    priorityButton = tk.Button(technician, text="Get Priority", command=getPriority, height=1)
    priorityButton.grid(row=14, column=0, sticky="ew", padx=40)

    hardware_button = tk.Button(technician, text="Hardware Marketplace", command = hardware_view, width = 16, height=1)
    hardware_button.grid(row=15, column=0, sticky="ew", padx=40)

#hardware menu to buy and sell hardware (view hardware and contact seller outside the app)
def hardware_view():
    Current_request=Hardware_Values_from_db()
    listings=Build_Hardware_data(Current_request)
    #create hardware window on top of root (main window)

    hardware = tk.Toplevel(root)
    #title and size of new window
    hardware.title("Hardware View")
    hardware.geometry("800x600")
    
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
    #listings = []

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

    #function to add new listings
    def addItem():
        #get hardware, price, condition, etc from above input boxes
        hardwareType = hardwareInput.get()
        price= priceInput.get()
        condition = conditionInput.get()
        contact = contactInput.get()
        description = descriptionInput.get()

        #Array with all the desired datafields
        hardware_info=[hardwareType, price, condition, contact, description]

        #Call function to store the array inside the database
        Add_hardware_db(hardware_info)
        updateList()
        Update_Input_Hardware()

    #update the listing box with new list values
    def updateList():
        #clear the old listingbox (delete elements from 0 to the end)
        listingsListBox.delete(0, tk.END)
        for i in range(len(listings)):
            #loop through and insert new listings starting at the end of the listingbox
            listingsListBox.insert(tk.END, listings[i])
    
    def Update_Input_Hardware():
        selected_hardware.set("")
        priceInput.delete(0, tk.END)
        selected_condition.set("")
        contactInput.delete(0, tk.END)
        descriptionInput.delete(0, tk.END)




    #button to create listings
    createButton = tk.Button(hardware, text="Add Listing", command=addItem, height=1)
    createButton.grid(row=10,column=0, sticky="ew", padx=40)

    #label for listingbox
    listingsLabel = tk.Label(hardware, text="Listings", height=1)
    listingsLabel.grid(row=11,column=0)
    #listingbox
    listingsListBox = tk.Listbox(hardware)
    listingsListBox.grid(row=12, column=0, sticky="ews", padx=40, pady=(10,20))

    updateList()
    


#Main root window & functions
#login function. run when login button is pressed. checks if username and password match existing one
def login():
    #get username and password from username and password input (both defined below)
    u = username_input.get()
    p = password_input.get()
    
    checking_login=FALSE
    
    for row in Users_Info:
        if row[1]==u:
            if row[2]==p:
                checking_login=TRUE
                role=row[3]


    if checking_login==TRUE:
        print(role)
        openWindow(role)
    else:
        print("Incorrect Information. Please verify it")

def openWindow(role):
    if role == 'Admin':
        admin_view()
    elif role == 'Technician':
        technician_view()
    elif role == 'Customer':
        customer_view()

Users_Info=User_Get_Values_from_db()

usernames = ['admin1', 'tech1', 'cust1']
passwords = ['apass', 'tpass', 'cpass']
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


root.mainloop()