
# tasks = []
from datetime import datetime
import json
file= open("data.json", "r")
x=file.read()
finaldata=json.loads(x)



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




def updateJSON(data):
    write_file= open("data.json", "w")
    json.dump(data, write_file, indent=4)


def viewAllTasks():
    if len(finaldata) == 0:
        print("No tasks found.")
    else:
        sln = 1
        for item in finaldata:
            # item_id = item["id"]
            status= "Pending"
            if item["completed"] == True:
                status = "Completed"
            print(f"{sln} . {item["title"]} ({status})")
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


def removeTask():
    viewAllTasks()
    toRemove = int(input("Enter task number: "))
    finaldata.pop(toRemove-1)
    updateJSON(finaldata)

while True:
    print("-TO-DO LIST-")
    print("1. View All Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Update status")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        viewAllTasks()

    elif choice == "2":
        task_title = input("Enter a task: ")
        due_date= input("Due date(d-m-y): ")
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
        viewAllTasks()

    elif choice == "3":
        if len(finaldata) == 0:
            print("No tasks to remove")
        else:
            removeTask()

            viewAllTasks()

    elif choice == "4":
        print("Update")
        viewAllTasks()
        task_to_update = int(input("Enter task number: "))
        task_status = int(input("write 1 if completed, write 2 if due: "))
        updateStatus(task_to_update, task_status)
        viewAllTasks()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")