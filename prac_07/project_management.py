import datetime

from project import Project

FILENAME = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management!")
    projects = load_projects()
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "l":
            filename = input("Filename to load projects from: ")
            load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save projects to: ")
            save_projects(projects,filename)


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

main()