import csv


def read_jobs():
    with open("data/jobs.csv", "r") as file:
        reader = csv.DictReader(file)
        jobs = list(reader)
        return jobs


def read_applications():
    with open("data/applications.csv", "r") as file:
        reader = csv.DictReader(file)
        applications = list(reader)
        return applications


def save_application(application):
    with open("data/applications.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=application.keys())
        writer.writerow(application)


def save_applications(applications):
    with open("data/applications.csv", "w", newline="") as file:
        fieldnames = applications[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(applications)         
