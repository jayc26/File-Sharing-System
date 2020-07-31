
#Name - Jay Nitin Chaphekar
#Student ID - 1001763932


import socket              #header for socket programming
from queue import Queue    #header for building a Queue
from _thread import *      #header for creating threads
import tkinter             #header for GUI

A_invalidation = Queue()
B_invalidation = Queue()
C_invalidation = Queue()
A_update = Queue()
B_update = Queue()
C_update = Queue()

# Creating Socket
# https://docs.python.org/2/howto/sockets.html
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 1710
        s = socket.socket()
    except socket.error as msg:
        print("Socket Error " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Error in Binding")
        bind_socket()
def print_label(val):
    global frame
    l1 = tkinter.Label(frame, text=val)
    l1.pack()
# Accepting the connections and assigning new thread
# https://www.tutorialspoint.com/python3/string_encode.htm
def accept():
    global flag_A
    global flag_B
    global flag_C
    global  clientname
    flag_A = False
    flag_B = False
    flag_C = False
    while True:
        conn, address = s.accept()
        clientname = str(conn.recv(1024), "utf-8")
        if clientname == "A":
            try:
                if flag_A == False:
                    print("Client A connected")
                    start_new_thread(handle_client, (conn,))
                    flag_A = True
                    conn.send(str.encode("Done"))
                else:
                    print("This user name already taken")
                    conn.send(str.encode("Undone"))
            except:
                print("This user name already taken")
        elif clientname == "B":
            try:
                if flag_B == False:
                    print("Client B connected")
                    start_new_thread(handle_client, (conn,))
                    flag_B = True
                    conn.send(str.encode("Done"))
                else:
                    print("This user name already taken")
                    
                    conn.send(str.encode("Undone"))
            except:
                print("This user name already taken")

        elif clientname == "C":
            try:
                if flag_C == False:
                    print("Client C connected")
                    start_new_thread(handle_client, (conn,))
                    flag_C = True
                    conn.send(str.encode("Done"))
                else:
                    print("This user name already taken")
                    
                    conn.send(str.encode("Undone"))
            except:
                print("This user name already taken")
        else:
            conn.send(str.encode("invalid"))
            print("Invalid Input")

# Thread function for handling the Client
# https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
def handle_client(conn):
    global clientname
    temp = clientname
    start_new_thread(invalidation_notice, (conn,))
    
    check_update(conn)
    
    res(conn)
    
    

#Check for updates from the Client
#checking by username and votes
def check_update(conn):
    global clientname
    temp = clientname
    global flag_A
    global flag_B
    global flag_C
    try:
        
        while True:
            
            update = str(conn.recv(1024), "utf-8")
            print_label(update)
            if temp == 'A':
                if update == 'YB':
                    print_label("B")
                    conn.send(str.encode("YesB"))
                if update == 'YC':
                    print_label("C")
                    conn.send(str.encode("YesC"))
            if temp == 'B':
                if update == 'YA':
                    print_label("A")
                    conn.send(str.encode("YesA"))
                if update == 'YC':
                    print_label("C")
                    conn.send(str.encode("YesC"))
            if temp == 'C':
                if update == 'YB':
                    print_label("B")
                    conn.send(str.encode("YesB"))
                if update == 'YA':
                    print_label("A")
                    conn.send(str.encode("YesA"))
            if temp == 'A':
                B_invalidation.put(update)
                C_invalidation.put(update)
                
                

            elif temp == 'B':
                A_invalidation.put(update)
                C_invalidation.put(update)
                
                
            elif temp == 'C':
                A_invalidation.put(update)
                B_invalidation.put(update)
                
        
            
    except:
        print("Connection disconnected")
        if temp == 'A':
            flag_A = False
        if temp == 'B':
            flag_B = False
        if temp == 'C':
            flag_C = False

#Function for sending deletion notice to other Clients
#https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing
def invalidation_notice(conn):
    global clientname
    temp = clientname
    flag_inva = True
    while True:
        if temp == 'A':
            if A_invalidation.qsize() > 0:
                flag_inva = False
            else:
                flag_inva = True

        if temp == 'C':
            if C_invalidation.qsize() > 0:
                flag_inva = False
            else:
                flag_inva = True

        if temp == 'B':
            if B_invalidation.qsize() > 0:
                flag_inva = False
            else:
                flag_inva = True
        if flag_inva == False:
            if temp == 'A':
                conn.send(str.encode(A_invalidation.get()))
                

            elif temp == 'B':
                conn.send(str.encode(B_invalidation.get()))
                
                
            elif temp == 'C':
                conn.send(str.encode(C_invalidation.get()))
                
        else:
            continue

 #To check responses   
def res(conn):
    print("In")
    global clientname
    temp = clientname
    resp = str(conn.recv(1024), "utf-8")
    print_label(resp)
    resp2 = str(conn.recv(1024), "utf-8")
    print_label(resp2)
    y = 0
    n = 0
    if temp == 'A':
        print("A is"+resp)
        conn.send(str.encode("YesA"))
    if temp == 'B':
        print("B is"+resp)
        conn.send(str.encode("YesB"))
    if temp == 'C':
        print("C is  "+resp)
        conn.send(str.encode("YesC"))
        
    

def main():
    null = ''
    start_new_thread(disp, (null,))
    create_socket()
    bind_socket()
    accept()


#Displaying the Status of the Clients on the GUI
# https://www.tutorialspoint.com/python/python_gui_programming.htm
def disp(null):
    global frame
    top = tkinter.Tk()
    main = tkinter.Canvas(top, height=500, width=600)
    main.pack()
    frame = tkinter.Frame(main)
    frame.place(relwidth=1, relheight=0.9)
    l1 = tkinter.Label(frame)
    l1.pack()
    l2 = tkinter.Label(frame)
    l2.pack()
    l4 = tkinter.Label(frame)
    l4.pack()
    l3 = tkinter.Label(frame)
    l3.pack()
    update(l1, top, l2, l4, l3)
    top.mainloop()

#Function for updating the Client Status
#https://stackoverflow.com/questions/24849265/how-do-i-create-an-automatically-updating-gui-using-tkinter
def update(l1, top, l2, l4, l3):
    if flag_A:
        l1.config(text = "Client A : Connected")
    else:
        l1.config(text="Client A : Disconnected")
    if flag_C:
        l4.config(text = "Client C : Connected")
    else:
        l4.config(text="Client C : Disconnected")
    if flag_B:
        l2.config(text="Client B : Connected")
    else:
        l2.config(text="Client B : Disconnected")
    top.after(1000, lambda : update(l1, top, l2, l4, l3))  # runs itself again after 1000 ms


main()
