from file_handler import read_jobs, read_applications
def show_dashboard():
    jobs = read_jobs()
    applications = read_applications()

    total_jobs = len(jobs)
    total_applications = len(applications)

    applied = 0
    interview = 0
    selected = 0
    rejected = 0

    for application in applications:
        status = application["status"].lower()

        if status == "applied":
            applied += 1
        elif status == "interview":
            interview += 1
        elif status == "selected":
            selected += 1
        elif status == "rejected":
            rejected += 1

    print("\n===== JOB APPLICATION DASHBOARD =====")
    print("Total Jobs         :", total_jobs)
    print("Total Applications :", total_applications)
    print("Applied            :", applied)
    print("Interview          :", interview)
    print("Selected           :", selected)
    print("Rejected           :", rejected)