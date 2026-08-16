from application import (
    view_jobs,
    apply_for_job,
    view_applications,
    update_application_status,
    recommend_jobs_for_user
)

from dashboard import show_dashboard


def main():
    print("SMART JOB APPLICATION & CAREER TRACKER")

    while True:
        print("\n1. View Jobs")
        print("2. Apply for Job")
        print("3. View Applications")
        print("4. Update Application Status")
        print("5. Recommend Jobs")
        print("6. Dashboard")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_jobs()

        elif choice == "2":
            apply_for_job()   

        elif choice == "3":
            view_applications()

        elif choice == "4":
            update_application_status()

        elif choice == "5":
            recommend_jobs_for_user()

        elif choice == "6":
            show_dashboard()

        elif choice == "7":
            print("Thank you for using Smart Job Career Tracker!")
            break


if __name__ == "__main__":
    main()        