import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
import json
file= open("data.json", "r")
x=file.read()
finaldata=json.loads(x)

# ---------------------------------
# GUI Implementation

root = tk.Tk()
root.geometry("800x600")
root.title("To-do app")

button_frame= tk.Frame(root)
button_frame.pack(pady=10)

msg_frame = tk.Frame(root)
msg_frame.pack()

search_frame = tk.Frame(root)
search_frame.pack()

search_label= tk.Label(search_frame, text="Search your task: ")
search_label.pack(side="left", padx=5)

search_input = tk.Entry(search_frame, width= 20)
search_input.pack(side="left", padx=5)

tree_frame = tk.Frame(root)
tree_frame.pack(fill="both", expand=True) 

# listbox = tk.Listbox(root)
# listbox.pack(fill="both", expand=True)

tree = ttk.Treeview(tree_frame,
                    columns=("Serial", "Task", "Status", "Due Date"), 
                    show="headings" )

# tree.pack(side="left", fill="both", expand=True) 

tree.heading("Serial", text="Serial")
tree.heading("Task", text="Task")
tree.heading("Status", text="Status")
tree.heading("Due Date", text="Due Date")


scrollbar = ttk.Scrollbar(
    tree_frame,
    orient="vertical",
    command=tree.yview
)

# scrollbar.pack(side="right", fill="y")

tree.configure(yscrollcommand=scrollbar.set)


tree.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

tree_frame.grid_rowconfigure(0, weight=1)
tree_frame.grid_columnconfigure(0, weight=1)


def generateID():
    if finaldata:
        # print('my list is not empty')
        last_item_id = finaldata[-1]['id']
        return last_item_id + 1
        # last_item = my_list[-1]
    else:
        return 1
        # print("The list is empty!")
        
def dateTime(): 
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M")

    return str(current_time) 



def searchTask():

    search_keyword = search_input.get().strip()

    for row in tree.get_children():
        tree.delete(row)

    sln = 1

    for item in finaldata:
        if search_keyword.lower() in item["title"].lower():

            status = "Pending"

            if item["completed"] == True:
                status="Completed"


            tree.insert(
                "", tk.END,
                values=(
                    sln,
                    item["title"],
                    status,
                    item["due_date"]
                )
            )

            sln = sln+1







def updateJSON(data):
    
    write_file= open("data.json", "w")
    json.dump(data, write_file, indent=4)


def viewAllTasks():

    global search_input

    search_input.delete(0, tk.END)

    for widget in msg_frame.winfo_children():
        widget.destroy()

    for row in tree.get_children():
        tree.delete(row)


    if len(finaldata) == 0:
        msg = "No tasks found."
        label = tk.Label(msg_frame, text= f"{msg}")
        label.pack() 

       
    else:
        sln = 1
        for item in finaldata:
            # item_id = item["id"]
            status= "Pending"
            if item["completed"] == True:
                status = "Completed"
            txt = f"{sln} . {item["title"]} ({status})\n Due date-{item["due_date"]}"
            # label = tk.Label(msg_frame, text= f"{txt}")
            # label.pack()

            tree.insert("",
                        tk.END,
                        values=(sln,
                                item["title"],
                                status,
                                item["due_date"]
                                ))


            sln += 1

def addTask(taskParam):
    finaldata.append(taskParam)
    # write_file= open("data.json", "w")
    # json.dump(finaldata, write_file, indent=4)


    updateJSON(finaldata)
    print("Task added")


def updateStatus(sln, status):
    # finaldata.append(taskParam)
    index = sln - 1 
    item = finaldata[index]
    # print("write 1 if completed, write 2 if due")

    if status == 1:
        item["completed"] = True
    elif status == 2:
        item["completed"] = False
    else:
        print("wrong input")
        

    # item["completed"] = status
    # write_file= open("data.json", "w")
    # json.dump(finaldata, write_file, indent=4)
    updateJSON(finaldata)
    print("Task Updated")

def updateData(sln, title, date, status):
  
    index = sln - 1 
    item = finaldata[index]
    item["title"] = title
    item["due_date"]= date

    if status == "Completed":
        item["completed"] = True
    elif status == "Pending":
        item["completed"] = False
        
    updateJSON(finaldata)
    print("Task Updated")

def removeTask(sln):
    viewAllTasks()
    toRemove = int(sln)
    finaldata.pop(toRemove-1)
    updateJSON(finaldata)





viewAllTasks()




task_label= tk.Label(button_frame, text="Enter your task: ")
task_label.pack(side="left", padx=5)

task_title_input = tk.Entry(button_frame)
task_title_input.pack(side="left", padx=5)

due_date_input = DateEntry(button_frame, date_pattern="dd-mm-yyyy")
due_date_input.pack(side="left", padx=5)


is_edit= False


def submitTask():

    global is_edit

    task_title = task_title_input.get().strip()
    due_date= due_date_input.get().strip()
    if task_title == "" or due_date == "":
        return 
        
    if is_edit == False :
        
        newID= generateID()
        current_time= dateTime()
        new_task = {
            "id": newID,
            "title": task_title,
            "completed": False,
            "created_at": current_time,
            "due_date": due_date
        }

        addTask(new_task)
    else:
        selected_row = tree.selection()
        
        if selected_row:
            row_data = tree.item(selected_row[0], "values") 

        sln = int(row_data[0])

        task_status = status.get()

        updateData(sln, task_title, due_date, task_status)

        is_edit = False

    task_title_input.delete(0, tk.END)


    viewAllTasks()



# submit_btn = tk.Button(root, text="Submit", command = submitTask)
# submit_btn.pack()



def editTask():

    global is_edit

    is_edit = True
    selected_row = tree.selection()

    if selected_row:
        row_data = tree.item(selected_row[0], "values") 

        task_title_input.delete(0, tk.END)
        task_title_input.insert(0, row_data[1])

        due_date_input.set_date(row_data[3])


def delTask():
    selected_row = tree.selection()
    
    if selected_row:
        row_data = tree.item(selected_row[0], "values") 

    removeTask(row_data[0])

    viewAllTasks()









submit_btn = tk.Button(button_frame, text="Submit", command = submitTask)
submit_btn.pack(side="left")

status = tk.StringVar()
status.set("Pending")

status_dropdown = tk.OptionMenu(
    button_frame,
    status,
    "Pending",
    "Completed"
)
status_dropdown.pack(side="left", padx=5)

edit_btn = tk.Button(button_frame, text="Edit", command = editTask)
edit_btn.pack(side="left")

search_btn = tk.Button(search_frame, text="Search", command=searchTask)
search_btn.pack(side="left", padx=5)

view_all_btn = tk.Button(search_frame, text="View All Tasks", command=viewAllTasks)
view_all_btn.pack(side="left", padx=5)

del_btn = tk.Button(button_frame, text="Delete", command = delTask)
del_btn.pack(side="left")


root.mainloop()