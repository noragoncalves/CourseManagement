class CourseItem:
    def __init__(self, title, category, due_date, points_possible):
        self.title = title
        self.category = category
        self.due_date = due_date
        self.points_possible = points_possible
        self.points_earned = None
        self.completed = False
    

    def mark_complete(self):
        self.completed = True

    def score_to_percentage(self, percentage):
        if percentage < 65:
            status = "F"
        elif 65 <= percentage < 70:
            status = "D"
        elif 70 <= percentage < 80:
            status = "C"
        elif 80 <= percentage < 90:
            status = "B"
        else:
            status = "A"

        return status

    def update_score(self, score):
        self.points_earned = score


    def display_info(self):
        if self.completed == True:
            status = "Completed"
        else:
            status = "Incomplete"

        if self.points_earned == None:
            score_text = "Not graded"
        else:
            score_text = (f"{self.points_earned}/{self.points_possible}")

        return str(f"{self.category}: {self.title} | Due: {self.due_date} | Score: {score_text} | Status: {status}")



# Default category weights — must sum to 100.
# Each Course gets its own copy of these weights, which can be customized.
DEFAULT_WEIGHTS = {
    "Homework":     20.0,
    "Quiz":         10.0,
    "Exam":         30.0,
    "Lecture Note": 5.0,
    "Project":      35.0,
}


def score_to_letter(percentage):
    # TODO: Implement the letter grade scale above using if/elif/else
    if percentage >= 93:
        letter = "A"
        return letter
    elif (percentage >= 90) and (percentage < 93):
        letter = "A-"
        return letter
    elif (percentage >= 87) and (percentage < 90):
        letter = "B+"
        return letter
    elif (percentage >= 83) and (percentage < 87):
        letter = "B"
        return letter
    elif (percentage >= 80) and (percentage < 83):
        letter = "B-"
        return letter
    elif (percentage >= 77) and (percentage < 80):
        letter = "C+"
        return letter
    elif (percentage >= 73) and (percentage < 77):
        letter = "C"
        return letter
    elif (percentage >= 70) and (percentage < 73):
        letter = "C-"
        return letter
    elif (percentage >= 67) and (percentage < 70):
        letter = "D+"
        return letter
    elif (percentage >= 63) and (percentage < 67):
        letter = "D"
        return letter
    elif (percentage >= 60) and (percentage < 63):
        letter = "D-"
        return letter
    else:
        letter = "F"
        return letter



class Course:
    def __init__(self, course_name, course_code, instructor_name):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.items = []
        self.weights = dict(DEFAULT_WEIGHTS)



    # ── Weight management ─────────────────────────────────────────────────

    def set_weights(self, new_weights):
        total = sum(new_weights.values())
        if abs(total - 100) <= 0.01:
            self.weights = new_weights
            return True
        else:
            return False


    def display_weights(self):
        list = []

        Format for each entry:
            "  <category>: <weight>%"

        Returns:
            list[str]: One string per category in self.weights.
        """
        # TODO: Build and return the list of weight strings


    # ── Item management ───────────────────────────────────────────────────

    def add_item(self, item):
        """
        Add a CourseItem to this course's items list.

        Parameters:
            item (CourseItem): The item to add.

        Rules:
            - Must not print anything.
        """
        # TODO: Append item to self.items


    def remove_item(self, item_title):
        """
        Remove an item from this course by title (case-insensitive).

        Parameters:
            item_title (str): Title of the item to remove.

        Returns:
            bool: True if the item was found and removed, False otherwise.

        Rules:
            - Comparison must be case-insensitive.
            - Must not print anything.
        """
        # TODO: Loop through self.items, find the match, remove it, return True
        # If not found, return False


    def find_item(self, item_title):
        item_title = item_title.lower()

        for i in self.items:
            check = i.title.lower()
            if check == item_title:
                return i     
        else:
            return None



    def display_items(self):
        if not self.items:
            list1=["No items found."]

        else:
            for i in self.items:
                info = i.display_info()
                list1.append(info)
        
        return list1


    def display_pending_items(self):
        list2=[]

        for i in self.items:
            if i.completed == False:
                info2 = i.display_info()
                list2.append(info2)
        
        if not list2:
            list2=["No pending items."]

        return list2


    # ── Grade calculation ─────────────────────────────────────────────────

    def calculate_grade(self):
        """
        Calculate the weighted overall grade for this course.

        Algorithm:
            For each category in self.weights that has weight > 0:
              1. Collect all graded items in that category
                 (items where points_earned is not None).
              2. If none exist, skip this category entirely.
              3. Compute category_pct = sum(points_earned) / sum(points_possible) * 100.
              4. Add category_pct * weight to a running weighted_sum.
              5. Add weight to a running active_weight.
            Final percentage = weighted_sum / active_weight.

        Returns:
            tuple(float, str) or None:
                A tuple of (percentage rounded to 2 decimal places, letter grade string)
                if at least one item has been graded.
                None if no items have been graded yet.

        Rules:
            - Only items with points_earned != None count as graded.
            - Categories with no graded items are excluded from the calculation.
            - Use score_to_letter() to convert the final percentage to a letter grade.
            - Must not print anything.
        """
        # TODO: Implement the weighted grade algorithm described above
        pass


class CourseManager:
    def __init__(self):
        self.courses=[]
    


    def add_course(self, course):
        """
        Add a Course object to the manager's list.

        Parameters:
            course (Course): The Course object to add.

        Rules:
            - Must not print anything.
        """
        # TODO: Append course to self.courses
        pass

    def find_course(self, course_name):
        course_search_cleaned = course_name.lower()

        for i in self.courses:
            cleaned_course = i.course_name.lower()
            if cleaned_course == course_search_cleaned:
                return i
    
        return None

    def find_course_by_code(self, course_code):
        course_code_cleaned = course_code.lower()
        for i in self.courses:
            cleaned = i.course_code.lower()
            if cleaned == course_code_cleaned:
                return i

        return None


    def display_courses(self):
        list2 = []
        
        if not self.courses:
            list2 = ["No courses available."]
        
        else:
            for i in self.courses:
                code = i.course_code
                name = i.course_name
                instructor = i.instructor_name
                course_info = f"{code}: {name} ({instructor})"
                list2.append(course_info)
        
        return list2
