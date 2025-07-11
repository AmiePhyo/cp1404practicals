import datetime
from operator import attrgetter

from project import Project

FILENAME = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management!")
    projects = load_projects()
    MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "l":
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save projects to: ")
            save_projects(projects,filename)
        elif choice == "d":
            display_projects(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "f":
            filter_projects(projects)
        else:
            print("Invalid choice.")

        MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
        print(MENU)
        choice = input(">>> ").lower()

    save_choice = input(f"Would you like to save to {FILENAME}? (Y/n): ").lower()
    if save_choice.startswith("y") or save_choice == "":
        save_projects(projects)
    print("Thank you for using custom-built project management software.")

def load_projects(filename=FILENAME):
    """Loads projects from a file."""
    projects = []
    with open(filename, "r") as file:
        file.readline()
        for line in file:
            parts = line.strip().split("\t")
            name, date_str, priority, cost, completion = parts
            start_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority), float(cost), int(completion)))
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects

def save_projects(projects, filename=FILENAME):
    """Saves projects to a file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            line = f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percent}\n"
            file.write(line)
    print(f"Saved {len(projects)} projects to {filename}")

def display_projects(projects):
    """Displays projects group;ed by completion and sorted by priority."""
    incomplete_projects = sorted([project for project in projects if not project.is_complete()])
    complete_projects = sorted(([project for project in projects if project.is_complete()]))
    print("Incompleted projects:")
    for project in incomplete_projects:
        print(f"{project}")

    print("Completed projects:")
    for project in complete_projects:
        print(f"{project}")

def update_project(projects):
    """Update a project's completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    print(project)
    new_completion = input("New Percentage: ").strip()
    new_priority = input("New Priority: ").strip()
    if new_completion:
        try:
            project.completion_percent = int(new_completion)
        except ValueError:
            print("Invalid completion input, not updated.")
    if new_priority:
        try:
            project.priority = int(new_priority)
        except ValueError:
            print("Invalid priority input, not updated.")

def add_new_project(projects):
    """Adds a new project to the list of projects."""
    print("Let's add a new project")
    name = input("Name: ")
    date_str = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    start_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    projects.append(Project(name, start_date, priority, cost, completion))
    print("Project added.")

def filter_projects(projects):
    """Filters projects by date."""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = [project for project in projects if project.start_date > filter_date]
    filtered.sort(key=attrgetter("start_date"))

    for project in filtered:
        print(project)

main()