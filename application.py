from file_handler import (
    read_jobs,
    read_applications,
    save_application,
    save_applications
)
from skill_matcher import calculate_match, recommend_jobs

def view_jobs():
    jobs = read_jobs()

    print("\nAvailable Jobs")
    print("-" * 70)

    for job in jobs:
        print(
            job["job_id"],
            job["job_title"],
            job["company"],
            job["location"],
            job["salary"]
        )

    print("-" * 70)


def apply_for_job():
    jobs = read_jobs()

    try:
        job_id = input("Enter Job ID: ")
        if not job_id:
            raise ValueError("Job ID cannot be empty")
    except ValueError as e:
        print("Error:", e)
        return
       
    for job in jobs:
        if job["job_id"] == job_id:
            name = input("Enter Applicant Name: ")
            user_skills = [
                skill.strip()
                for skill in input("Enter Your Skills (comma separated): ").split(",")
            ]
            job_skills = job["skills"].split()

            match_percentage = calculate_match(
                job_skills,
                user_skills
            )

            print(f"Skill Match: {match_percentage:.2f}%")
            application = JobApplication(
                f"A{len(read_applications()) + 1:03d}",
                job_id,
                name,
                "Applied"
            )    

            application_data = {
                "application_id": application.application_id,
                "job_id": application.job_id,
                "applicant_name": application.applicant_name,
                "status": application.get_status(),
                "match_percentage": f"{match_percentage:.2f}%"
}

            save_application(application_data)
            application.display()

            print("Application submitted successfully!")
            return

    print("Job not found.")

def view_applications():
    applications = read_applications()

    print("\nMy Applications")
    print("-" * 70)

    for application in applications:
        print(
            application["application_id"],
            application["job_id"],
            application["applicant_name"],
            application["status"],
            application["match_percentage"]
        )

    print("-" * 70)    


def update_application_status():
    applications = read_applications()
    try:
        application_id = input("Enter Application ID: ")
        if not application_id:
            raise ValueError("Application ID cannot be empty")

    except ValueError as e:
        print("Error:", e)
        return
    for application in applications:
        if application["application_id"] == application_id:
            new_status = input("Enter New Status: ")

            application["status"] = new_status

            save_applications(applications)

            print("Status updated successfully!")
            return

    print("Application not found.")


def recommend_jobs_for_user():
    jobs = read_jobs()

    user_skills = [
        skill.strip()
        for skill in input("Enter Your Skills: ").split(",")
    ]

    recommendations = recommend_jobs(jobs, user_skills)

    print("\nRecommended Jobs")
    print("-" * 70)

    for job, match_percentage in recommendations:
        print(
            job["job_id"],
            job["job_title"],
            job["company"],
            f"{match_percentage:.2f}% Match"
        )

    print("-" * 70)    

class JobApplication:
    def __init__(self, application_id, job_id, applicant_name, status):
        self.application_id = application_id
        self.job_id = job_id
        self.applicant_name = applicant_name
        self.__status = status



    def display(self):
        print("Application ID :", self.application_id)
        print("Job ID         :", self.job_id)
        print("Applicant Name :", self.applicant_name)
        print("Status         :", self.__status)

    def update_status(self, new_status):
        self.__status = new_status  
    def get_status(self):
        return self.__status 

class EmployeeApplication(JobApplication):
    def display(self):
        print("Employee Application")
        print("Application ID :", self.application_id)
        print("Job ID         :", self.job_id)
        print("Applicant Name :", self.applicant_name)
        print("Status         :", self.get_status())




