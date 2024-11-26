import sqlite3
#Generation of Database with the tables needed for the current project.
def Database_Creation():
    try:
        PC_Repair_Connection=sqlite3.connect("PC_Repair.db")
        #Creation of Cursor to use SQL statements and fetch from the table.  
        cur=PC_Repair_Connection.cursor()
        #First Table is the User one. First, check if there was already a user table built
        #if that is the case, drop the table. Not optimal to have two tables with the same name. 
        cur.execute("DROP TABLE IF EXISTS user_t")
        #After checking if there was an old table, create the new version
        cur.execute("""CREATE TABLE IF NOT EXISTS user_t(u_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                        username TEXT,                  
                                                        password TEXT, 
                                                        Class TEXT CHECK(Class IN('Admin', 'Technician', 'Customer')));""")
        #Initial values for the user_t
        user_examples=[("admin1", "apass", "Admin"), 
                       ("tech1", "tpass", "Technician"),
                       ("cust1", "cpass", "Customer")]

        #Initial values into the users table
        cur.executemany("""INSERT INTO user_t(username, password, Class) VALUES (?, ?, ?)""", user_examples)




        #Second table is the Request one. Repeat the same process as the previous one.
        cur.execute("DROP TABLE IF EXISTS request_t")
        cur.execute("""CREATE TABLE IF NOT EXISTS request_t(r_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                           severity_degree TEXT CHECK (severity_degree IN ('1-Minor', 
                                                           '2-Unsure', '3-Medium', '4-Severe')),
                                                           type_request TEXT CHECK(type_request IN('Hardware', 'Software')),
                                                           price Numeric(4,1), 
                                                           u_email TEXT,
                                                           explanation TEXT
                                                           );""")
        #Initial Values for requests_t
        requests_examples=[("1-Minor", "Software", 80, "bobbybobby@gmail.com", "My computer screen is blue and it doesnt turn on after that"),
                           ("2-Unsure", "Hardware", 120, "joesmithy@gmail.com", "My computers fans arent running and it is very hot"),
                           ("4-Severe", "Software", 85, "janedoe@gmail.com", "My Computer is on fire. HELP ASAP")]
        
        #Entering the values into the request table
        cur.executemany(""" INSERT INTO request_t(severity_degree, type_request, price, u_email, explanation) 
                                    VALUES (?,?,?,?,?)""", requests_examples)

        #Third Table is for the technicians. Repeat the same process as the previous table.
        cur.execute("DROP TABLE IF EXISTS technician_t")
        cur.execute(""" CREATE TABLE IF NOT EXISTS technician_t(t_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                Service_Type TEXT CHECK (Service_Type IN ('Hardware', 'Software')),
                                                                price_aprox Numeric(4,1),
                                                                rating TEXT CHECK(rating IN ('1-Learning', '2-Intermediate', '3-Experienced', 
                                                                '4-Novice', '5-Professional')), 
                                                                contact_info TEXT,
                                                                Description TEXT);""")
        #Initial Values for technician table 
        technician_examples=[("Software",200, "1-Learning", "tomj@gmail.com", "Operating system installations or troubleshooting"), 
                             ("Software",120, "3-Experienced", "bobsmith@gmail.com", "BIOS configuration or troubleshooting"), 
                             ("Hardware", 150, "4-Novice", "juniorsmith@gmail.com", "GPU/CPU intallation, hardware troubleshooting")]
        
        #Initial values entered into the databse
        cur.executemany(""" INSERT INTO technician_t(Service_Type, price_aprox, rating, contact_info, Description) 
                                        VALUES (?,?,?,?,?)""", technician_examples)


    
        #Fourth table is for the hardware. Repeat the same process as the previous table.
        cur.execute("DROP TABLE IF EXISTS hardware_t")
        cur.execute(""" CREATE TABLE IF NOT EXISTS hardware_t(hardware_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                              type TEXT CHECK (type IN ('Monitor', 'Mouse', 'Keyboard', 
                                                              'GPU', 'CPU', 'RAM', 'Motherboard')), 
                                                              price NUMERIC(4,1), 
                                                              condition TEXT CHECK(condition IN('Like New', 'Good', 'Used', 'Functional', 
                                                              'Poor', 'For Parts')), 
                                                              contact_email TEXT, 
                                                              description TEXT);""")
        #Initial Values for the hardware table
        hardware_examples=[("Monitor", 180, "Like New", "bob@gmail.com", "acer 27 inch fcfs"),
                           ("GPU", 200, "Good", "redsam@gmail.com", "Nvidia gtx 970 runs well and cool"), 
                           ("Motherboard", 100,"Used", "joeyman21@gmail.com", "Acer motherboard. Not sure what model is" )] 
        
        #Putting data inside the table
        cur.executemany("""INSERT INTO hardware_t(type, price, condition, contact_email, description)
                                           VALUES(?, ?, ?, ?, ?)""", hardware_examples)
    
        #To apply the changes into the database, it is needed to commit them.
        PC_Repair_Connection.commit()
        print("Tables were created correctly")
    except sqlite3.OperationalError as e:
        print("Unexpected Error: The tables were not created. ", e)
    
    #After all the changes are done, the connection with the database should be close. 
    PC_Repair_Connection.close()

Database_Creation()
