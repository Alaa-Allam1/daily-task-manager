tasks = input("Enter your tasks for today separated by a comma: ").split(", ")

done_tasks = []
ongoing_tasks = []

for tasks_today in tasks:
    print (f"\n{tasks_today}\n")
    choice = input (f"Did you finish {tasks_today} already?\n")


    if choice == "yes":
        print("Nice Job")
        print("--------")
        done_tasks.append(tasks_today)
    else:
        print("Try not to put it off")
        print("---------------------")
        ongoing_tasks.append(tasks_today)

progress_tasks = input("Do you want to see your todays progress?(yes , no)")

if progress_tasks == "no":
    input("Please hit Enter to exit")
else:
    print("""
             ***** Done Tasks *****         
""")
    print(done_tasks)

    print("""
             ***** Ongoing Tasks *****   
""")
    print(ongoing_tasks)
