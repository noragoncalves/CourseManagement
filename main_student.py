#Student 1:
#Spire ID:
#Student 2: Maryam Ahsan Syeda
#Spire ID: 35238104

from course_management import CourseItem, Course, CourseManager, DEFAULT_WEIGHTS


def display_menu():
    print("\nCourse Management System")
    print("1.  Add a new course")
    print("2.  View all courses")
    print("3.  Add an item to a course")
    print("4.  View all items in a course")
    print("5.  Mark an item as completed")
    print("6.  Update an item's score")
    print("7.  View pending items")
    print("8.  Calculate course grade")
    print("9.  Customize category weights")
    print("10. Exit")


def prompt_course_code(manager):
    
    print("Current courses:")
    for course in manager.display_courses():
        print (" " + course) #concatenation because display_courses is a list of strings

    code = input("Enter course code: ")
    object1 = manager.find_course_by_code(code)

    if object1 == None:
        print("Course not found.")
        return None
    
    return object1
                   


def main():
    manager = CourseManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter course name: ")
            code = input("Enter course code: ")
            instructor = input("Enter instructor name: ")
            Course1 = Course(name, code, instructor)
            manager.add_course(Course1)
            print("Course added successfully.")

        elif choice == "2":
            for item in manager.display_courses():
                print(item)

        elif choice == "3":
            
            course = prompt_course_code(manager)
            if course is None:
                continue
            else:
                title = input("Enter item title: ")
                category = input("Enter category (Homework/Quiz/Exam/Lecture Note/Project): ")
                due_date = input("Enter due date: ")
                points_possible = float(input("Enter points possible: "))
                CourseItem3 = CourseItem(title, category, due_date, points_possible)
                course.add_item(CourseItem3)
                print("Item added successfully.")
    
        elif choice == "4":
            course = prompt_course_code(manager)
            if course is None:
                continue
            else:
                for item in course.display_items():
                    print(item)

        elif choice == "5":
            course = prompt_course_code(manager)
            if course is None:
                continue
            else:
                item_title = input("Enter item title: ")
                search = course.find_item(item_title)
                if search is None:
                    print("Item not found.")
                else:
                    search.mark_complete()
                    print("Item marked as completed.")

        elif choice == "6":

            course = prompt_course_code(manager)
            
            if course == None:
                continue
            else:
                prompt_item_title = input("Enter item title: ")
                item = course.find_item(prompt_item_title)
                if item == None:
                    print("Item not found.")
                else:
                    score = float(input("Enter score earned: "))
                    item.update_score(score)
                    print("Score updated successfully.")



        elif choice == "7":
            
            course = prompt_course_code(manager)

            if course == None:
                continue

            else:
                for item in course.display_pending_items():
                    print(item)


        elif choice == "8":

            course = prompt_course_code(manager)

            if course == None:
                continue
            else:
                grade = course.calculate_grade()
                if grade == None:
                    print("No graded items yet.")
                else:
                    print(f"Course Grade for {course.course_code}: {course.course_name}")
                    print(f"  Weighted average : {grade[0]:.2f}%") #does this work for a tuple?
                    print(f"  Letter grade     : {grade[1]}")
                    print("  Category breakdown:")
                    
                    for cat in course.weights:
                        graded_items = [] 
                        for i in course.items:
                            if (i.points_earned == None) and (i.category == cat):
                                    graded_items = graded_items
                            elif(i.points_earned != None) and (i.category == cat):
                                    graded_items.append(i)
                    
                        if len(graded_items) == 0:
                            print(f"{cat} ({course.weights[cat]}%): No graded items")
                        else:
                            earned= 0.0
                            possible= 0.0
                            for i in graded_items:
                                earned += i.points_earned
                                possible += i.points_possible
                            percentage = (earned/possible) * 100
                            print(f"{cat} ({course.weights[cat]}%): {earned}/{possible} = {percentage:.1f}%")



        elif choice == "9":
            course = prompt_course_code(manager)

            if course is None:
                continue
            
            else: 
                print(f"Current weights for {course.course_code}:")
                for i in course.display_weights():
                    print(i)

                print("Enter new weights (pressing Enter keeps the current value)")
                new_weight = {}
                for cat in course.weights:
                    value = course.weights[cat]
                    user_weights = (input(f"{cat} (current: {value}%): ")) 
                    if user_weights == "":
                        new_weight[cat]=value
                    else:
                        new_weight[cat]= float(user_weights)
                total = sum(new_weight.values())
                if (100.00 - total) == 0: # would this need tolerance?
                    course.set_weights(new_weight)
                    print("Weight updated sucessfully")
                else:
                    print(f"Weights must sum to 100 (got {total:.2f}). No changes made.")

        elif choice == "10":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")
            pass


if __name__ == "__main__":
    main()
