#Student 1
#Nora Goncalves
#Spire ID:

#Student 2
#Maryam Ahsan Syeda
#Spire ID:

#CourseItem Class

class CourseItem:
    def __init__(self, category, due_date, points_possible, points_earned, completed):
        self.category=category
        self.due_date=due_date
        self.points_possible=points_possible
        self.points_earned=points_earned
        self.completed=completed
course_items = []
course_items.append(CourseItem('ECE122',02.10, 100, 85, True))
course_items.append(CourseItem('ECE201', 02.13, 20, 13, True))
course_items.append(CourseItem('COMPSCI250', 02.09, 15, 0, False))

for item in course_items:
    print(f"Category: {item.category}")
    print(f"Due Date: {item.due_date}")
    print(f"Points Possible: {item.points_possible}")
    print(f"Points Earned: {item.points_earned}")
    print(f"Completed Status: {item.completed}")

mark_complete()

score_to_letter(percentage)

#Course Class

set_weights(new_weights)

display_weights()

add_item()

remove_item(title)

calculate_grade()

#CourseManager Class
__init__()

add_course(course)

#main.py

#menu options 1, 2, 3, 4, 5