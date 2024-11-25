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
                                                        Class TEXT);""")
        #Second table is the Request one. Repeat the same process as the previous one.
        cur.execute("DROP TABLE IF EXISTS request_t")
        cur.execute("""CREATE TABLE IF NOT EXISTS request_t(r_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                           severity_degree TEXT,
                                                           type_request TEXT,
                                                           price Numeric(4,1), 
                                                           u_email TEXT,
                                                           explanation TEXT
                                                           );""")
        #Third Table is for the technicians. Repeat the same process as the previous table.
        cur.execute("DROP TABLE IF EXISTS technician_t")
        cur.execute(""" CREATE TABLE IF NOT EXISTS technician_t(t_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                                rating INTEGER, 
                                                                exp_lvl TEXT, 
                                                                t_email TEXT,
                                                               Work_Field TEXT);""")
    
        #Fourth table is for the hardware. Repeat the same process as the previous table.
        cur.execute("DROP TABLE IF EXISTS hardware_t")
        cur.execute(""" CREATE TABLE IF NOT EXISTS hardware_t(hardware_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                              type TEXT, 
                                                              price NUMERIC(4,1), 
                                                              condition TEXT, 
                                                              contact_email TEXT, 
                                                              description TEXT);""")
    
        #To apply the changes into the database, it is needed to commit them.
        PC_Repair_Connection.commit()
        print("Tables were created correctly")
    except sqlite3.OperationalError as e:
        print("Unexpected Error: The tables were not created. ", e)
    
    #After all the changes are done, the connection with the database should be close. 
    PC_Repair_Connection.close()

Database_Creation()
