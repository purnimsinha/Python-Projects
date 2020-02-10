#library files import**********************************************************************************************
#***************************************************************************************************************************
import tkinter
from tkinter import filedialog
from tkinter import *
import os
from tkinter.filedialog import askopenfile
from tkcolorpicker  import askcolor
from tkinter.filedialog import askdirectory
import os


#main window UI********************************************************************************************************
#*********************************************************************************************************************
window = Tk()
window.title("Supremology build ")
window.geometry('500x400')
window.configure(background = "lightgray")
#window.grid(padx=20, pady=20)
MyText= StringVar()

feedback=""


#function for all operations*********************************************************************************************
#**********************************************************************************************************************

#to create sub window******************************************************************************************************
def create():
    window = tkinter.Tk()
    window.title("new window ")
    window.geometry('900x900')
    window.configure(background = "navyblue")
    
#function to select file**************************************************************
def callback():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)
    

#function to get path*********************************************************************
def DisplayDir(Var):
    feedback = askdirectory()
    Var.set(feedback)


#function to get the colour window**********************************************************
def color():
    result = askcolor(color="#6A9662", title = "Bernd's Colour Chooser") 
    print (result)


#simple function**************************************************************************
def function():
    pass

# creating a root menu to insert all the sub menus****************************************************************
##***********************************#######################*************************************************************
root_menu = tkinter.Menu(window)
window.config(menu = root_menu)


# creating #file# sub menus in the root menu
file_menu = tkinter.Menu(root_menu) # it intializes a new sub menu in the root menu
root_menu.add_cascade(label = "File", menu = file_menu) # it creates the name of the sub menu
file_menu.add_command(label = "New file.....", command = function ) # it adds a option to the sub menu 'command' parameter is used to do some action
file_menu.add_command(label = "Open files", command = function)
file_menu.add_separator() # it adds a line after the 'Open files' option
file_menu.add_command(label = "Exit", command = window.quit)

# creting another #edit# sub menu
edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", accelerator="Ctrl+z",command = function)
edit_menu.add_command(label = "Redo", accelerator="Ctrl+y", command = function)
edit_menu.add_command(label = "Cut", accelerator="Ctrl+x", command = function)
edit_menu.add_command(label = "Copy", accelerator="Ctrl+c", command = function)
edit_menu.add_command(label = "Paste", accelerator="Ctrl+v", command = function)
edit_menu.add_command(label = "colour", accelerator="Ctrl+v", command = color)

#creating another #view# sub menu
View_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = "View", menu = View_menu)
View_menu.add_command(label = "Reload", accelerator="Ctrl+R", command = function)
View_menu.add_command(label = "Toggle Developer Tool", accelerator="Ctrl+Shift+I", command = function)
View_menu.add_command(label = "Zoom in", accelerator="Ctrl+Shift+=", command = function)
View_menu.add_command(label = "Zoom out", accelerator="Ctrl+Shift-", command = function)

#creating another #project# sub menu
Project_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = "Project", menu = Project_menu)
Project_menu.add_command(label = "new                ",  command=create)
Project_menu.add_command(label = "Open          ",  command = function)
Project_menu.add_command(label = "close      ",  command = function)
Project_menu.add_command(label = "Save project",  command = function)
Project_menu.add_command(label = "Save project as",  command = function)
Project_menu.add_command(label = "import file",  command = function)
Project_menu.add_command(label = "Export file",  command = function)
Project_menu.add_command(label = "remove files from project",  command = function)
Project_menu.add_command(label = "version control ",  command = function)



#creating another #window# sub menu
Window_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = "Window", menu = Window_menu)
Window_menu.add_command(label = "Minimise", accelerator="Ctrl+M", command = function)
Window_menu.add_command(label = "Close", accelerator="Ctrl+W", command = function)


#creating another #help# sub menu
Help_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = "Help", menu = Help_menu)
Help_menu.add_command(label = "Learn more", command = function)
Help_menu.add_command(label = "Documentation", command = function)
Help_menu.add_command(label = "Community Discussion", command = function)
Help_menu.add_command(label = "Search Issue", command = function)

#form function to get the values of path and prroject name**********************************************************************************
#*******************************************************************************************************************************************

def retrieve_input():
    global project_name
    global project_path
    
    project_name = entry_1.get()
    project_path = entry_2.get()
    
    
    #number_checker()
    command="python cmder.py "+project_path+" "+project_name
    os.system(command)
    os.system("git init "+project_path+"/"+project_name+"/")
    
    demoCopy= project_path+"/"+project_name+"/"
    demoCopy=demoCopy.replace("/","\\")
                     
    os.system("xcopy /F main.c "+demoCopy)
    

def build_function():
    global project_path
    global project_name

    project_path = entry_2.get()
    project_name = entry_1.get()

 
    os.system("cd " + project_path+ "/ & gcc main.c")




#form********************************************************************************************************************************************
    #******************####################************************************########################******************************************
label_1 = Label(window, text="Project name",width=20,font=("bold", 10))
label_1.place(x=70,y=130)
entry_1 = Entry(window, width=30)
entry_1.place(x=250,y=130)

label_2 = Label(window, text="Project Path",width=20,font=("bold", 10))
label_2.place(x=70,y=180)
    


Button(window, text='Browse', command=lambda : DisplayDir(MyText),width=25).place(x=250,y=203)
entry_2 = Entry(window, textvariable = MyText, width=30)
entry_2.place(x=250,y=180)


    
Button(window, text='create', command=retrieve_input, width=25,bg='gray',fg='white').place(x=250,y=280)
Button(window, text='build', width=25,bg='navyblue',fg='white',command=build_function).place(x=65,y=280)
    
# window.destroy


#creating toolbar*************************************************************************************************************
#*************************************************************************************************************************
toolbar = Frame(window)

b = Button(toolbar, text="new", width=6, command=function)
b.pack(side=LEFT, padx=12, pady=2)

b = Button(toolbar, text="open", width=6, command=function)
b.pack(side=LEFT, padx=12, pady=2)
toolbar.pack(side=TOP, fill=X)



#end of window********************************************************************************************************
window.mainloop()
