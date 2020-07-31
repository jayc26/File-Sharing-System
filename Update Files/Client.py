
#Name - Jay Nitin Chaphekar
#Student ID - 1001763932


import socket          #header for socket programming
import shutil          #header for comparing  files
import filecmp         #header for copying data from one file to other
from _thread import *  #header for threading
import tkinter         #header for GUI
import sys

flag_inv = True
flag_update = ''
flag_GUI = ''
invalidation = ''

# Function to connect to the Server
# https://docs.python.org/3/howto/sockets.html
def connect_server():
    s = socket.socket()
    host = '127.0.0.1'
    port = 1710
    s.connect((host, port))
    return s, host, port


# A function to print on the GUI
# https://www.tutorialspoint.com/python/python_gui_programming.htm
def print_label(val):
    global frame
    l1 = tkinter.Label(frame, text=val)
    l1.pack()

# A function to give input to GUI
# https://www.tutorialspoint.com/python/python_gui_programming.htm
def GUI_Input(b1, var):
    b1.wait_variable(var)
    Input = E1.get()
    E1.delete(0, 'end')
    return Input



#Function to Exit the Client
def quit(top):
    top.destroy()
    sys.exit()




# Function to accept the Update
# https://stackabuse.com/how-to-copy-a-file-in-python/
def Yes(s):
    global flag_inv
    global c
    c = 0
    if clientname == 'A':
        
        shutil.copyfile('B/Client_B_file.txt', "A/Compare_B.txt")
        shutil.copyfile('C/Client_C_file.txt', "A/Compare_C.txt")    
        flag_inv = False
        s.send(str.encode('Update Successful at A'))
        print_label("Update Successful at A")
        

    elif clientname == 'C':
        shutil.copyfile('B/Client_B_file.txt', "C/Compare_B.txt")
        shutil.copyfile('A/Client_A_file.txt', "C/Compare_A.txt")
        flag_inv = False
        s.send(str.encode('Update Successful at C'))
        print_label("Update Successful at C")
        

    else:
      
            shutil.copyfile('A/Client_A_file.txt', "B/Compare_A.txt")
            shutil.copyfile('C/Client_C_file.txt', "B/Compare_C.txt")
            flag_inv = False
            s.send(str.encode('Update Successful at B'))
            print_label("Update Successful at B")

# Function to Reject the Update
# https://stackabuse.com/how-to-copy-a-file-in-python/
def No(s):
    global flag_inv
    if clientname == 'A':
        s.send(str.encode('Update Unsuccessful at A'))
        print_label("Update Unsuccessful at A")
    elif clientname == 'C':
        s.send(str.encode('Update Unsuccessful at C'))
        print_label("Update Unsuccessful at C")
    else:
        s.send(str.encode('Update Unsuccessful at B'))
        print_label("Update Unsuccessful at B")

# Client validation and assigning threads
# https://www.tutorialspoint.com/python/python_gui_programming.htm
# https://docs.python.org/2/library/thread.html
# https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
# https://www.tutorialspoint.com/python/python_gui_programming.htm
def main():
    global top
    top = tkinter.Tk()
    global flag_inv
    global flag_update
    global clientname
    global frame
    global E1
    global flag_GUI
    global invalidation
    global b1
    global var
    var = tkinter.IntVar()
    main = tkinter.Canvas(top, height=500, width=600)
    main.pack()
    frame = tkinter.Frame(main)
    frame.place(relwidth=1, relheight=0.9)
    s, host, port = connect_server()
    E1 = tkinter.Entry(frame)
    E1.pack()
    b1 = tkinter.Button(frame, text="Enter", command=lambda: var.set(1))
    b1.pack()
    b2 = tkinter.Button(frame, text='Quit', command=lambda: quit(top))
    b2.pack()
    print_label("Enter Client name 'A', 'B', 'C'")
    clientname = GUI_Input(b1, var)
    s.send(str.encode(clientname))
    response = str(s.recv(1024), "utf-8")
    if response == "Undone":
        print_label("Client Name taken")
    elif response == "invalid":
        print_label("Invalid Input")
    else:
        print_label("Client " + clientname + " has been connected")
        start_new_thread(invalidatiion, (s,))
        start_new_thread(update, (s,))
        Gui()

    top.mainloop()


def Gui():
    if flag_update == False and flag_inv:
        print_label("There is an update")
    if flag_GUI:
        print_label(invalidation)

#Function for receiving invalidation notices
def invalidatiion(s):
    global clientname
    global flag_inv
    global flag_GUI
    global invalidation
    global b1
    global var
    global top
    flag_GUI = False
    while True:
        invalidation = str(s.recv(1024), "utf-8")
        flag_GUI = True
        print_label(invalidation)
        if invalidation == "Update Successful" or "Update Unsuccessful":
            flag_inv = True
        if invalidation == "There is an update":
            flag_inv = False
            updated_file = str(s.recv(1024), "utf-8")
            print_label(updated_file)
            print_label("Do you accept the update 'Yes' or 'No'")
            b3 = tkinter.Button(frame, text='Yes', command=lambda: Yes(s))
            b3.pack()
            b4 = tkinter.Button(frame, text='No', command=lambda: No(s))
            b4.pack()

# Function for checking the updates to the desired text File
# https://docs.python.org/2/library/filecmp.html
# https://stackabuse.com/how-to-copy-a-file-in-python/
def update(s):
    global clientname
    global flag_inv
    
    while True:
        flag_update = True
        if clientname == 'A':
            if flag_inv:
                while flag_update and flag_inv:
                    flag_update = filecmp.cmp("A/Client_A_file.txt", "B/Compare_A.txt")
                    flag_update = filecmp.cmp("A/Client_A_file.txt", "C/Compare_A.txt")#Checking for update
                
                if flag_update == False and flag_inv:
                    notice = "There is an update"
                    s.send(str.encode(notice))
                    print_label(notice)
                    ufa = open("A/Client_A_file.txt").read()
                    s.send(str.encode("The update version is \n" + ufa))
                    flag_inv = False
                    flag_update = False
                    break
        elif clientname == 'B':
           if flag_inv:
                while flag_update and flag_inv:
                    flag_update = filecmp.cmp("B/Client_B_file.txt", "A/Compare_B.txt")
                    flag_update = filecmp.cmp("B/Client_B_file.txt", "C/Compare_B.txt")#Checking for update
                if flag_update == False and flag_inv:
                    notice = "There is an update"
                    s.send(str.encode(notice))
                    print_label(notice)
                    ufb = open("B/Client_B_file.txt").read()
                    s.send(str.encode("The updated version is \n " + ufb))
                    flag_inv = False
                    flag_update = False
                    break

        elif clientname == 'C':
            if flag_inv:
                while flag_update and flag_inv:
                    flag_update = filecmp.cmp("C/Client_C_file.txt", "A/Compare_C.txt")
                    flag_update = filecmp.cmp("C/Client_C_file.txt", "B/Compare_C.txt")#Checking for update
                
                if flag_update == False and flag_inv:
                    notice = "There is an update"
                    s.send(str.encode(notice))
                    print_label(notice)
                    ufc = open("C/Client_C_file.txt").read()
                    s.send(str.encode("The updated version is \n " + ufc))
                    flag_inv = False
                    flag_update = False
                    break


main()
