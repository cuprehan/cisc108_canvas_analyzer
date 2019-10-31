"""
Project 4C
Canvas Analyzer
CISC108 Honors
Fall 2019

Access the Canvas Learning Management System and process learning analytics.

Edit this file to implement the project.
To test your current solution, run the `test_my_solution.py` file.
Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Rehan Amir
"""
__version__ = 7

# 1) main
import canvas_requests
def main(name):
    user = canvas_requests.get_user(name)
    print_user_info(user)
    courses = canvas_requests.get_courses(name)
    courses = filter_available_courses(courses)
    print_courses(courses)
    course_ids = get_course_ids(courses)
    course_id = choose_course(course_ids)
    submissions = canvas_requests.get_submissions(name,course_id)
    summarize_points(submissions)
    summarize_groups(submissions)
    plot_scores(submissions)
    plot_grade_trends(submissions)
# 2) print_user_info
def print_user_info(user):
    print("Name: " + user["name"])
    print("Title: " + user["title"])
    print("Primary Email: " + user["primary_email"])
    print("Bio: " + user["bio"])

bio = {
    "name": "Hermione Granger",
    "title": "Student",
    "primary Email": "hgranger@hogwarts.edu",
    "bio": "Interested in Magic, Learning, and House Elf Rights"
    }
# 3) filter_available_courses
def filter_available_courses(courses):
    available_courses = []
    for course in courses:
        if course["workflow_state"] == "available":
            available_courses.append(course)
    return available_courses

# 4) print_courses
def print_courses(courses):
    for course in courses:
        print(course["id"] + " : " + "name")
# 5) get_course_ids
def get_course_ids(courses):
    course_ids = []
    for course in courses:
        course_ids.append(course["id"])
    return course_ids
# 6) choose_course
def choose_course(course_ids):
    chosen_course = input("Pick a course id:")
    chosen_course = int(chosen_course)
    while chosen_course not in course_ids:
        chosen_course = int(input("Pick a course id:"))
    return chosen_course
# 7) summarize_points
def summarize_points(submissions):
    points_possible = 0
    points_obtained = 0
    for submission in submissions:
        points_possible = points_possible + (submission["assignment"]["points_possible"] * submission["assignment"]["points_possible"]["group"]["group_weight"])
        points_obtained = points_obtained + (submission["score"] * submission["assignment"]["points_possible"]["group"]["group_weight"])
    print("Points possible so far: " + str(points_possible))
    print("Points obtained: " + str(points_obtained))
    print("Current grade: " + str(round((points_obtained/points_possible) * 100), 1))
# 8) summarize_groups
def summarize_groups(submissions):
    group_score = {}
    group_points = {}
    for submission in submissions:
        group_name = submission["assignment"]["group"]["name"]

# 9) plot_scores
def plot_scores(submissions):

# 10) plot_grade_trends

# Keep any function tests inside this IF statement to ensure
# that your `test_my_solution.py` does not execute it.
if __name__ == "__main__":
    main('hermione')
    # main('ron')
    # main('harry')
    
    # https://community.canvaslms.com/docs/DOC-10806-4214724194
    # main('YOUR OWN CANVAS TOKEN (You know, if you want)')