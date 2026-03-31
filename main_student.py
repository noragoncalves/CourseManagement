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
            # TODO: Prompt for course name, course code, and instructor name
            # Create a Course object and add it to manager via manager.add_course()
            # Print "Course added successfully."
            pass

        elif choice == "2":
            # TODO: Print each string returned by manager.display_courses()
            pass

        elif choice == "3":
            # TODO: Call prompt_course_code(manager) to get the course
            # If None, use 'continue' to go back to the menu
            # Otherwise, prompt for item title, category, due date, and points possible
            # Create a CourseItem and add it to the course via course.add_item()
            # Print "Item added successfully."
            pass

        elif choice == "4":
            # TODO: Call prompt_course_code(manager) to get the course
            # If None, use 'continue'
            # Otherwise, print each string returned by course.display_items()
            pass

        elif choice == "5":
            # TODO: Call prompt_course_code(manager) to get the course
            # If None, use 'continue'
            # Prompt for item title, call course.find_item()
            # If None, print "Item not found."
            # Otherwise, call item.mark_complete() and print "Item marked as completed."

            pass

        elif choice == "6":
            # TODO: Call prompt_course_code(manager) to get the course
            # If None, use 'continue'
            # Prompt for item title, call course.find_item()
            # If None, print "Item not found."
            # Otherwise, prompt for score (float), call item.update_score()
            # Print "Score updated successfully."
            
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
            # TODO: Call prompt_course_code(manager) to get the course
            # If None, use 'continue'
            # Print each string returned by course.display_pending_items()
            
            course = prompt_course_code(manager)

            if course == None:
                continue

            else:
                for item in course.display_pending_items():
                    print(item)


        elif choice == "8":
            # TODO: Call prompt_course_code(manager) to get the course
            # If None, use 'continue'
            # Call course.calculate_grade()
            # If None, print "No graded items yet."
            # Otherwise:
            #   Print "Course Grade for <course_code>: <course_name>"
            #   Print "  Weighted average : <percentage:.2f>%"
            #   Print "  Letter grade     : <letter>"
            #   Print a per-category breakdown (see project spec for format)

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
                    print("  Category Breakdown:")
                    
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
            # TODO: Call prompt_course_code(manager) to get the course
            # If None, use 'continue'
            # Print "Current weights for <course_code>:"
            # Print each string from course.display_weights()
            # Print instructions, then prompt the user for a new weight per category
            #   (pressing Enter keeps the current value)
            # Validate that the new weights sum to ~100
            # If valid, call course.set_weights() and print "Weights updated successfully."
            # If invalid, print "Weights must sum to 100 (got <total:.2f>). No changes made."
            pass

        elif choice == "10":
            # TODO: Print "Exiting program." and break out of the loop
            print("Exiting program.")
            break

        else:
            # TODO: Print "Invalid choice. Please try again."
            pass


if __name__ == "__main__":
    main()
