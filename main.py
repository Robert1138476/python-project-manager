import os
import shutil
import time
import subprocess

print("Robert's python project organizer")

if not os.path.exists("projects"):
    os.makedirs("projects")

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

            selection = input("> ")
            if selection == "b":
                break

            try:
                selection = int(selection) - 1
            except ValueError:
                print("invalid selection")
                break

            name = input("give your project a name: ")
            try:
                shutil.copytree(f"templates/{templates[selection]}", f"projects/{name}")
                print("Project created successfully!")
            except FileExistsError:
                print("Error: Project already exists.")
            except Exception as e:
                print("An error occurred:", e)
                time.sleep(5)
                quit()

            print("opening project...")
            time.sleep(1)
            command = os.path.abspath(f"projects/{name}")
            command = f'code "{command}"'
            subprocess.run(command, shell=True, capture_output=False)
            quit()

        elif command == "o":
            print(f"\nselect a project to open")

            for i, project in enumerate(projects):
                print(f"{i+1} - {project}")

            selection = input("> ")
            if selection == "b":
                break
            try:
                selection = int(selection) - 1
            except ValueError:
                print("invalid selection")
                break

            command = os.path.abspath(f"projects/{projects[selection]}")
            command = f'code "{command}"'
            subprocess.run(command, shell=True, capture_output=False)
            quit()

        elif command == "m":
            print("select a project to manage")

            for i, project in enumerate(projects):
                print(f"{i+1} - {project}")

            selection = input("> ")
            if selection == "b":
                break
            try:
                selection = int(selection) - 1
            except ValueError:
                print("invalid selection")
                break

            print(
                f"\nselect a option to manage {projects[selection]}\nd - delete project\nr - rename project"
            )

            option = input("> ")
            if option == "d":
                shutil.rmtree(f"projects/{projects[selection]}")
                print("project deleted")
            elif option == "r":
                name = input("give your project a new name: ")

                shutil.move(f"projects/{projects[selection]}", f"projects/{name}")
                print("project renamed")
            elif option == "b":
                break
            else:
                print("invalid selection")

            time.sleep(2)
            quit()

        elif command == "t":
            print("select a template to manage or n to create a new one")

            for i, template in enumerate(templates):
                print(f"{i+1} - {template}")

            selection = input("> ")
            if selection == "b":
                break
            elif selection == "n":
                name = input("give your template a name: ")

                os.mkdir(f"templates/{name}")
                print("template created")
                print("opening template...")
                time.sleep(1)

                command = os.path.abspath(f"templates/{name}")
                command = f'code "{command}"'
                subprocess.run(command, shell=True, capture_output=False)
                quit()
            try:
                selection = int(selection) - 1
            except ValueError:
                print("invalid selection")
                break

            print(
                f"\nselect a option to manage {templates[selection]}\ne - edit template\nd - delete template\nr - rename template"
            )

            option = input("> ")
            if option == "e":
                print("opening template...")
                time.sleep(1)

                command = os.path.abspath(f"templates/{templates[selection]}")
                command = f'code "{command}"'
                subprocess.run(command, shell=True, capture_output=False)
                quit()
            elif option == "d":
                shutil.rmtree(f"templates/{templates[selection]}")
                print("template deleted")
            elif option == "r":
                name = input("give your template a new name: ")

                shutil.move(f"templates/{templates[selection]}", f"templates/{name}")
                print("template renamed")
            elif option == "b":
                break
            else:
                print("invalid selection")

            time.sleep(2)
            quit()
        else:
            print("invalid command")
            break
