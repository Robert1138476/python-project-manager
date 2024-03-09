import os
import shutil
import time
import subprocess

print("Robert's python project organizer")

projects = os.listdir("projects")
print(f"Found {len(projects)} projects")

templates = os.listdir("templates")
print(f"Found {len(templates)} templates")

while True:
    print(
        f"\ntype a command and press enter.\nc - create new project\no - open project\nm - manage projects\nt - manage templates\nin other menus press b for back"
    )
    command = input("> ").lower()

    while True:
        if command == "c":
            print(f"\nselect a template to create a new project")
            for i, template in enumerate(templates):
                print(f"{i+1} - {template}")
            try:
                selection = input("> ")
                if selection == "b":
                    break
                selection = int(selection) - 1
            except:
                print("invalid selection")
            name = input("give your project a name: ")
            try:
                shutil.copytree(f"{templates[selection]}", f"projects/{name}")
                print("Project created successfully!")
            except FileExistsError:
                print("Error: Project already exists.")
            except Exception as e:
                print("An error occurred:", e)
            print("project created")
            print("opening project...")
            time.sleep(1)
            command = os.path.abspath(f"projects/{name}")
            command = f'code "{command}"'
            subprocess.run(command, shell=True, capture_output=False)
            quit()

        elif command == "o":
            print("open project")
        elif command == "m":
            print("manage projects")
        elif command == "t":
            print("manage templates")
        else:
            print("invalid command")
