
#Name - Jay Nitin Chaphekar
#Student ID - 1001763932

import time
import os
from watchdog.observers import Observer  #watcher
from watchdog.events import PatternMatchingEventHandler #watcher
import socket          #header for socket programming
import shutil          #header for comparing  files
import filecmp         #header for copying data from one file to other
from _thread import *  #header for threading
import tkinter         #header for GUI
import sys
import random
from threading import Timer
#defining variables used for the program
flag_inv = True
flag_update = ''
flag_GUI = ''
invalidation = ''
global h
global n
global vote
global y
global no
global ya
global cou
cou = 0
y = 0
no = 0
n = 0
h = 0
ya = 0
vote = ''
global de
de = 0

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
    global vote
    vote = l1.cget("text")
    vs(vote)
    l1.pack()

    
#function to check incoming votes at the co-ordinator
#increasing vote variable value based on yes and no
def vs(vote):
    global y
    global no
    global clientname
    a = 0
    b = 0
    c = 0
    if vote == "Client A has been connected":
        a = 1
        print("A")
    if vote == "Client B has been connected":
        b = 1
        print("B")
    if vote == "Client C has been connected":
        c = 1
        print("C")
    if vote == 'YB':
        print("In A")
        y = y+1
        
        if a == 1:
            print("B ala")
            y = y+1
            print(y)
        if c == 1:
            print("C ala")
            y =y+1
    if vote == 'YC':
        y = y+1
    if vote == 'YA':
        y = y+1
    if vote == 'NA':
        no = no+1
        
    if vote == 'NB':
        no = no+1
    if vote == 'NC':
        no = no+1
    
        
            
            
        
        
    
    
    print(vote)
#label to print values
def inp():
    global frame
    l2 = tkinter.Label(frame, text=val)
    l1.pack()
    inpu = l2.cget("text")
    return inpu

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

#To check the counts
def co():
    print(h)
    print(n)

# Function to check the update
# https://stackabuse.com/how-to-copy-a-file-in-python/
def Res(s):
    print("Started")
    update = str(s.recv(1024), "utf-8")
    print("This is Update"+update)
    
#Accepting Request, increasing the yes counter
# https://stackabuse.com/how-to-copy-a-file-in-python/
def Yes(s):
    global flag_inv
    global c
    global h
    global n
    global de
    c = 0
    if clientname == 'A':
        global y
        global ya
        de = 1
        
        y = y+1
        s.send(str.encode('YA'))
        print_label("Yes from A")
        
        
        h = h+1
        
        print("Message Received")
        
       
                
        flag_inv = False
        
        co()
        s.send(str.encode('Yes From A'))
        
        

    elif clientname == 'C':
        
        
        de = 1
        
        y = y+1
        h = h+1
        
        s.send(str.encode('YC'))
        print_label("Yes From C")
        
        
        print('Receiving msg')
        
        flag_inv = False
        
        co()
        s.send(str.encode('Yes From C'))
        
        

    else:
        de = 1
        
        h = h+1
        y = y+1
        
        
        s.send(str.encode('YB'))
        
        print_label("Yes from B")
        
        y = y+1
        

        
        print('Receiving msg')
        
        flag_inv = False
        
        co()
        s.send(str.encode('Yes From B'))
        

# Function to Reject the Update
#Rejecting the request, updating the no counter
# https://stackabuse.com/how-to-copy-a-file-in-python/
def No(s):
    global flag_inv
    global n
    if clientname == 'A':
        de = 1
        n = n+1
        s.send(str.encode('NA'))
        
        co()
        s.send(str.encode('No From A'))
        print_label("No From A")
    elif clientname == 'C':
        de = 1
        n = n+1
        s.send(str.encode('NC'))
        
        co()
        s.send(str.encode('No From C'))
        print_label("No From C")
    else:
        de = 1
        n = n+1
        s.send(str.encode('NB'))
        
        co()
        s.send(str.encode('No From B'))
        print_label("No From B")

# Client validation and assigning threads and the GUI implementation of accepting the clients
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


def coun():
    global cou
    cou = 1
def Gui():
    if flag_update == False and flag_inv:
        print_label("There is an update")
    if flag_GUI:
        print_label(invalidation)

#Function for receiving deletion notices
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
            #funtion to decide based on random probability
            def f1():
                global cou
                if cou == 0:
                    
                    n = random.randint(0, 1)
                    print(n)
                    if n == 1:
                        Yes(s)
                    if n == 0:
                        No(s)
                cou = 0
    
    
    
            
            print_label("Vote for Yes or No'")
            
            b3 = tkinter.Button(frame, text='Yes', command=lambda: [Yes(s), coun()])
            #b3.pack()
            b4 = tkinter.Button(frame, text='No', command=lambda: [No(s),coun()])
            #b4.pack()
            #top.after(17000,b3.destroy)
            #top.after(17000,b4.destroy)
            
            
            print_label("Generating Random Vote")
                
            top.after(3000,f1)
            


# Function for checking the updates for the deletion of the file
# https://docs.python.org/2/library/filecmp.html
# https://stackabuse.com/how-to-copy-a-file-in-python/
#https://pythonhosted.org/watchdog/
#watcher code for each client
def update(s):
    global clientname
    global flag_inv
    global de
    while True:
        flag_update = True
        if clientname == 'A':
            
                
                if flag_inv :
                    while flag_update and flag_inv:
                    
                        if __name__ == "__main__":
                            patterns = "*"
                            ignore_patterns = ""
                            ignore_directories = False
                            case_sensitive = True
                            my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
                            #deletion based on votes
                            def on_deleted(event):
                                print("File deleted {event.src_path}!")
                                global y
                                global no
                                y = 0
                                no = 0
                                filename = os.path.basename(event.src_path)
                                
                                flag_update = False
                                flag_inv = True
                                global de
                                if flag_update == False and flag_inv:
                                    
                                        
                                        notice = "There is an update"
                                        s.send(str.encode(notice))
                                        print_label(notice)
                                        
                                        
                                        de = 0
                                        
                                        
                                        s.send(str.encode("File Deletion Request \n"))
                                        
                                    
                                
                                        up = str(s.recv(1024), "utf-8")
                                        
                                        print('Pl'+ up)
                                
                                
                                    
                                        print_label(up)
                                        if up == 'YB':
                                            print('Yes From B')
                                        if up == 'YC':
                                            print('Yes From C')
                                        print('')
                                        
                                        if up == 'YA':
                                            print('')
                                        time.sleep(5)
                                        if y == 2:
                                            
                                                
                                                
                                                print_label("Proceed to deletion")
                                                
                                                os.remove("B/Receive/"+filename)
                                                os.remove("C/Receive/"+filename)
                                                print_label("Operation Completed")
                                                de = 0
                                            
                                    
                                            
                                        elif y == 1 and no == 0:
                                            print_label("Unable to receive vote")
                                            shutil.copy("Shared/"+filename, "A/Send/"+filename)
                                            print_label("Operation Cancelled")
                                        
                                        elif y == 0 and no == 1:
                                            print_label("Unable to receive vote")
                                            shutil.copy("Shared/"+filename, "A/Send/"+filename)
                                            print_label("Operation Cancelled")
                                        
                                        elif y == 1 and no == 1:
                                            print_label("Cancelling Deletion")
                                            shutil.copy("Shared/"+filename, "A/Send/"+filename)
                                            print_label("Operation Cancelled")
                                        else:
                                            print_label("Cancelling Deletion")
                                            shutil.copy("Shared/"+filename, "A/Send/"+filename)
                                            print_label("Operation Cancelled")
                                
                                        flag_inv = False
                                        flag_update = False
                                
                                        up = 0
                                        y = 0
                                        no = 0
                            
                            
                        
                                
                                
                            def on_modified(event):
                                #send files upon arrival
                                print("File Modified {event.src_path}!")
                                filename = os.path.basename(event.src_path)
                                filen = os.path.basename(event.src_path)
                                if((os.path.exists('B/Receive/'+filen) == False) and (os.path.exists('C/Receive/'+filen) == False)):
                                    shutil.copy("A/Send/"+filen, "Shared/"+filen)
                                    shutil.copy("A/Send/"+filen, "B/Receive/"+filen)
                                    shutil.copy("A/Send/"+filen, "C/Receive/"+filen)
                                else:
                                    print("File Already Exist")
                                
                                
                        
                            my_event_handler.on_deleted = on_deleted
                            my_event_handler.on_modified = on_modified
                        
                            path = "A/Send"
                            go_recursively = True
                            my_observer = Observer()
                            my_observer.schedule(my_event_handler, path, recursive=go_recursively)
                            my_observer.start()
                        
                            try:
                                 while True:
                                     time.sleep(1)
                            except KeyboardInterrupt:
                            
                                my_observer.stop()
                                my_observer.join()
                            
                    
                        
                
                    if flag_update == False and flag_inv:
                        notice = "There is an update"
                        
                        print_label(notice)
                        
                        flag_inv = False
                        flag_update = False
                        break
                        
        elif clientname == 'B':
           if flag_inv:
                while flag_update and flag_inv:
                    if __name__ == "__main__":
                        patterns = "*"
                        ignore_patterns = ""
                        ignore_directories = False
                        case_sensitive = True
                        my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
                        #deletion based on votes
                        def on_deleted(event):
                            print("File deleted {event.src_path}!")
                            filename = os.path.basename(event.src_path)
                            global y
                            global no
                            y = 0
                            no = 0
                            
                            flag_update = False
                            flag_inv = True
                            global de
                            if flag_update == False and flag_inv:
                                
                                    notice = "There is an update"
                                    s.send(str.encode(notice))
                                    
                                
                                
                                    s.send(str.encode("File Deletion Request \n"))
                                
                                
                                    up = str(s.recv(1024), "utf-8")
                                    
                                
                                
                                
                                    print_label(up)
                                    if up == 'YB':
                                        print('')
                                    if up == 'YC':
                                        print('')
                                    print('')
                                    
                                    if up == 'YA':
                                        print('')
                                
                                    time.sleep(5)
                                    if y == 2:
                                        print_label("Proceed to deletion")
                                        
                                        os.remove("A/Receive/"+filename)
                                        os.remove("C/Receive/"+filename)
                                        print_label("Operation Completed")
                                        de=0
                                    
                                        flag_inv = False
                                        flag_update = False
                                    elif y == 1 and no == 0:
                                        print_label("Unable to receive vote")
                                        shutil.copy("Shared/"+filename, "B/Send/"+filename)
                                        print_label("Operation Cancelled")
                                        
                                    elif y == 0 and no == 1:
                                        print_label("Unable to receive vote")
                                        shutil.copy("Shared/"+filename, "B/Send/"+filename)
                                        print_label("Operation Cancelled")
                                        
                                    elif y == 1 and no == 1:
                                        print_label("Cancelling Deletion")
                                        shutil.copy("Shared/"+filename, "B/Send/"+filename)
                                        print_label("Operation Cancelled")
                                        
                                    
                                    
                                
                                    else:
                                        print_label("Cancelling Deletion")
                                        shutil.copy("Shared/"+filename, "B/Send/"+filename)
                                        print_label("Operation Cancelled")
                                    flag_inv = False
                                    flag_update = False
                                    up = 0
                                    y = 0
                                    no = 0
                            
                                
                             
                        def on_modified(event):
                            #sending files upon arrival
                            print("File Modified {event.src_path}!")
                            filen = os.path.basename(event.src_path)
                            if((os.path.exists('A/Receive/'+filen) == False) and (os.path.exists('C/Receive/'+filen) == False)):
                                shutil.copy("B/Send/"+filen, "Shared/"+filen)
                                shutil.copy("B/Send/"+filen, "A/Receive/"+filen)
                                shutil.copy("B/Send/"+filen, "C/Receive/"+filen)
                            else:
                                print_label("File Already Exist")
                               
                               
                            filename = os.path.basename(event.src_path)
                            
                        my_event_handler.on_deleted = on_deleted
                        my_event_handler.on_modified = on_modified
                        
                        path = "B/Send/"
                        go_recursively = True
                        my_observer = Observer()
                        my_observer.schedule(my_event_handler, path, recursive=go_recursively)
                        my_observer.start()
                        try:
                            while True:
                                time.sleep(1)
                        except KeyboardInterrupt:
                            my_observer.stop()
                            my_observer.join()
                    
                    
                if flag_update == False and flag_inv:
                    notice = "There is an update"
                    s.send(str.encode(notice))
                    print_label(notice)
                    
                    s.send(str.encode("File Deletion Request \n "))
                    flag_inv = False
                    flag_update = False
                    break

        elif clientname == 'C':
            if flag_inv:
                while flag_update and flag_inv:
                    if __name__ == "__main__":
                        patterns = "*"
                        ignore_patterns = ""
                        ignore_directories = False
                        case_sensitive = True
                        my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
                        #deletion based on votes
                        def on_deleted(event):
                            print("File Deleted")
                            global y
                            global no
                            y = 0
                            no = 0
                            filename = os.path.basename(event.src_path)
                            
                            flag_update = False
                            flag_inv = True
                            global de
                            if flag_update == False and flag_inv:
                                
                                    
                                    notice = "There is an update"
                                    s.send(str.encode(notice))
                                    print_label(notice)
                                
                                    
                                    s.send(str.encode("File Deletion Request \n"))
                                
                                
                                    up = str(s.recv(1024), "utf-8")
                                    
                                
                                    if up == 'YB':
                                        print('Bala')
                                    if up == 'YC':
                                        print('Cala')
                                        print('Yes2')
                                    print_label(up)
                                    if up == 'YA':
                                        print('Yes3')

                                    
                                    time.sleep(5)
                                    if y == 2:
                                        
                                        print_label("Proceed to deletion")
                                        
                                        os.remove("B/Receive/"+filename)
                                        os.remove("A/Receive/"+filename)
                                        print_label("Operation Completed")
                                        de = 0
                                        flag_inv = False
                                        flag_update = False
                                        
                                        
                                    elif y == 1 and no == 0:
                                        print_label("Unable to receive vote")
                                        shutil.copy("Shared/"+filename, "C/Send/"+filename)
                                        print_label("Operation Cancelled")
                                        
                                    elif y == 0 and no == 1:
                                        print_label("Unable to receive vote")
                                        shutil.copy("Shared/"+filename, "C/Send/"+filename)
                                        print_label("Operation Cancelled")
                                        
                                    elif y == 1 and no == 1:
                                        print_label("Cancelling Deletion")
                                        shutil.copy("Shared/"+filename, "C/Send/"+filename)
                                        print_label("Operation Cancelled")
                                    else:
                                        print_label("Cancelling Deletion")
                                        shutil.copy("Shared/"+filename, "C/Send/"+filename)
                                        print_label("Operation Cancelled")
                                    flag_inv = False
                                    flag_update = False
                                    up = 0
                                
                            
                                    y = 0
                                    no = 0
                        
                                
                        def on_modified(event):
                            #sending files upon arrival
                            print(" File Modified {event.src_path}!")
                            filename = os.path.basename(event.src_path)
                            filen = os.path.basename(event.src_path)
                            if((os.path.exists('B/Receive/'+filen) == False) and (os.path.exists('A/Receive/'+filen) == False)):
                                shutil.copy("C/Send/"+filen, "Shared/"+filen)
                                shutil.copy("C/Send/"+filen, "B/Receive/"+filen)
                                shutil.copy("C/Send/"+filen, "A/Receive/"+filen)
                            else:
                                print_label("")
                            
                        my_event_handler.on_deleted = on_deleted
                        my_event_handler.on_modified = on_modified
                        
                        path = "C/Send/"
                        go_recursively = True
                        my_observer = Observer()
                        my_observer.schedule(my_event_handler, path, recursive=go_recursively)
                        my_observer.start()
                        try:
                            while True:
                                time.sleep(1)
                        except KeyboardInterrupt:
                            my_observer.stop()
                            my_observer.join()
                       
                    
                    
                
                if flag_update == False and flag_inv:
                    
                        
                        
                        flag_inv = False
                        flag_update = False

                        break


main()
