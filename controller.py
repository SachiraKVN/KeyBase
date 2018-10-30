import config
import model as md
import libs.nucrypt as nc


def add_data(*args, **kwargs):
    """ Add a connection to Database 
        notes: name and connection type save in lowercaase letters
    """    
    conn = md.create_connection("%s/connection.db"%(config.root))
    if conn is not None:
        md.create_table(conn)
        md.insert_data(conn, args[0])
        #  Refresh the connection list
        args[1].delete(0, 'end')
        listInsert(args[1])
    clearField(args[0])
    conn.close()

def get_data(view, name):
    """ 
        Get data from the Database & output to display
        @view : textbox to output
        @name : name query to get data
    """
    cp = nc.NuCrypt()
    conn = md.create_connection("%s/connection.db"%(config.root)) 
    if conn is not None:
        result = md.select_from(conn, name)

        if  result:
            for row in result:
                output = "Id : {id} \nName : {name} \nURL : {url}\nType : {type}\nUser name : {user} \nPassword : {passw}\n\n".format(name=row[1], url=row[5], user=row[3], passw=cp.decrypt(row[4]), type=row[2], id=row[0] )   

                view.insert('end', output)
        else:
            view.insert('end','No recoard found for: "{q}"\n'.format(q=name))
    conn.close()

def update_data(*args, **kwargs):
    """
        Connection update
    """
    cp = nc.NuCrypt()
    data = args[0]
    query = "update credential set name='{name}', type='{type}', user='{user}', password='{password}', url='{url}' where id={id};".format(name=data['name'].get().lower(), type=data['type'].get().lower(), user=data['user'].get(), password=cp.encrypt(data['password'].get()), url=data['url'].get(),id=data['id'].get())
    con = md.create_connection("%s/connection.db"%(config.root))
    if con is not None:
        try:
            result = md.execute_query(con,  query)
            con.commit()
        except Error as e:
            pass            
            # print(e)
    
    clearField(data)
    con.close()


def listInsert(element):
    """ 
        Get Available connection and insert into given listbox
    """
    conn = md.create_connection("%s/connection.db"%(config.root)) 

    result = md.execute_query(conn, "select distinct name from credential")
    if result:
        i=0
        for row in result:
            element.insert(i, row[0].capitalize())
            i+1
    else:
        element.insert('end', "You don\'t have any connection yet :)" )
    conn.close()


def onSelect(event, output):
    """
         Add connection detils to the display on item select on listbox
         @event : listbox select event
         @output : text box to output
    """

    element = event.widget
    selection = element.curselection()
    value = event.widget.get(selection[0])
    
    get_data(output, value)

def entryInsert(event, fields):
    """
        Add Data to fields on after enter id on update tab
        @event : focusout event
        @field : filed dictionry to particular data
    """

    element = event.widget
    val = event.widget.get()
    conn = md.create_connection("%s/connection.db"%(config.root))
    cp = nc.NuCrypt()

    # Get data from the database
    results = md.execute_query(conn, "select * from credential where id='{ID}'".format(ID=val))
    if results[0] is not None:
        fields['name'].delete(0, 'end')
        fields['name'].insert(0, results[0][1])

        fields['type'].delete(0, 'end')                
        fields['type'].insert(0, results[0][2])

        fields['username'].delete(0, 'end')        
        fields['username'].insert(0, results[0][3])

        fields['password'].delete(0, 'end')        
        fields['password'].insert(0, cp.decrypt(results[0][4]))

        fields['url'].delete(0, 'end')        
        fields['url'].insert(0, results[0][5])

def clearField(elements):
    """
    Reset form fields
    """
    for element in elements:
        elements[element].set('')
        


    


