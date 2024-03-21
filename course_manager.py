# import the csv module for handling CSV files
import csv

# first row of the CSV file will be treated as column names
header = None

# defining a class to represent a course
class Course:
    def __init__(self, code, name, teacher, credits, extras, midterm, final, difficulty):

# initialize a course object with the given attributes
        self.code = code
        self.name = name
        self.teacher = teacher
        self.credits = credits
        self.extras = extras
        self.midterm = midterm
        self.final = final
        self.difficulty = difficulty

# a function to load courses from a CSV file
def load_courses(filename="courses.csv"):
    courses = []  # creates an empty list to store course objects
    try:
# opens the CSV file in read mode
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile) # creates a DictReader() object from the CSV file
            for row in reader: # go through over each row in the CSV file
                course = Course(row['code'], row['name'], row['teacher'], 
                                row['credits'], row['extras'],  row['midterm'],
                                row['final'], row['difficulty'])
                courses.append(course) # add the course object to the list
    except FileNotFoundError: 
      # if the file is not found, print a message
        print("No courses.csv file found. Starting fresh.")
    return courses

def save_courses(courses, filename="courses.csv"):
    """Saves courses to a CSV file.""" 
     # open the CSV file in write mode
    with open(filename, 'w', newline='') as csvfile: 
        fieldnames = ['code', 'name', 'teacher', 'credits', 'extras', 'midterm', 'final', 'difficulty']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for course in courses:
            # write each course's attributes as a row in the CSV file
            writer.writerow({
                'code': course.code,
                'name': course.name,
                'teacher': course.teacher,
                'credits': course.credits,
                'extras': course.extras,
                'midterm': course.midterm,
                'final': course.final,
                'difficulty': course.difficulty
            })
 # a function to display the course information         
def display_courses(courses):
    if not courses: # if the list of courses is empty
        print("No courses saved yet.")
        return  # exit the function

    for i, course in enumerate(courses, start=1): # go through over each course and its index, starting from 1
        print(f"\nCourse {i}:")
        print(f"Code: {course.code}")
        print(f"Name: {course.name}")
        print(f"Teacher: {course.teacher}")
        print(f"Credits: {course.credits}")
        print(f"Extras: {course.extras}")
        print(f"Midterm: {course.midterm}")
        print(f"Final: {course.final}")
        print(f"Difficulty: {course.difficulty}")

# a function to add a new course
def add_course(courses):
    while True:
        code = input("Enter the course code: ")  # get the course code from the user
        if code:  # if the course code is not empty
            break  # Exit the loop
        else:
            print("Course code cannot be empty.")  # print an error message

    name = input("Enter your name: ")  # get the student's name from the user
    teacher = input("Enter the teacher's name: ")  # get the teacher's name from the user

    while True:
        try:
            credits = int(input("Enter the number of credits: "))  # get the number of credits from the user
            break  # exit the loop if the input is valid
        except ValueError:
            print("Invalid input. Please enter a number.")  # print an error message if the input is invalid

    extras = input("Enter extra points (or leave blank): ")  # get the extra points from the user
    midterm = input("Enter midterm grade (or leave blank): ")  # get the midterm grade from the user
    final = input("Enter final exam grade (or leave blank): ")  # get the final exam grade from the user

    while True:
        difficulty = input("Enter difficulty (easy, medium, hard): ").lower()  # get the difficulty level from the user (case-insensitive)
        if difficulty in ("easy", "medium", "hard"):  # if the input is valid
            break  # exit the loop
        else:
            print("Invalid difficulty. Please enter 'easy', 'medium', or 'hard'.")  # print an error message if the input is invalid

    new_course = Course(code, name, teacher, credits, extras, midterm, final, difficulty)  # create a new Course object
    courses.append(new_course)  # add the new course to the list
    print("Course added!")  # print a success message

# function to modify an existing course
def modify_course(courses):
  if not courses:  # if the list of courses is empty
        print("No courses saved yet.") 
        return  # exit the function
  
  display_courses(courses)

  while True:
        try:
            course_index = int(input("Enter the number of the course to modify: ")) - 1  # get the course index from the user
            if 0 <= course_index < len(courses):  # if the index is valid
                break  # exit the loop
            else:
                print("Invalid course number.")  # print an error message if the index is invalid
        except ValueError:
            print("Invalid input. Please enter a number.")  # print an error message if the input is invalid

  print("\nWhat would you like to modify?") # print the options for modification
  print("1. Code")
  print("2. Name")
  print("3. Teacher")
  print("4. Credits")
  print("5. Extras")
  print("6. Midterm")
  print("7. Final")
  print("8. Difficulty")
  print("9. Done")

  modify_choice = input("Enter your choice: ") # get the user's choice

  while modify_choice not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):  # if the choice is invalid
        print("Invalid choice.")  # print an error message and
        modify_choice = input("Enter your choice: ")  # get the user's choice again

  if modify_choice == '9': # if the user chooses "Done"
    print("Course modifications complete!")
    return # exit the function

  # modify the course
  while True:
    if modify_choice == '1':
      new_code = input("Enter the new course code: ")
      courses[course_index].code = new_code
      break
    elif modify_choice == '2':
      new_name = input("Enter the new course name: ")
      courses[course_index].name = new_name
      break
    elif modify_choice == '3':
      new_teacher = input("Enter the new teacher's name: ")
      courses[course_index].teacher = new_teacher
      break
    elif modify_choice == '4':
       new_credits = int(input("Enter the new number of credits: "))
       courses[course_index].credits = new_credits
       break
    elif modify_choice == '5':
      new_extras = input("Enter new extra points (or leave blank): ")
      courses[course_index].extras = new_extras
      break
    elif modify_choice == '6':
      new_midterm = input("Enter new midterm grade (or leave blank): ")
      courses[course_index].midterm = new_midterm
      break
    elif modify_choice == '7':
      new_final = input("Enter new final exam grade (or leave blank): ")
      courses[course_index].final = new_final
      break
    elif modify_choice == '8':
      while True:
        new_difficulty = input("Enter new difficulty (easy, medium, hard): ").lower() # get the new difficulty level from the user (case-insensitive)
        if new_difficulty in ("easy", "medium", "hard"): # if the input is valid
          courses[course_index].difficulty = new_difficulty # update the difficulty level
          break
        else:
          print("Invalid difficulty. Please enter 'easy', 'medium', or 'hard'.")
    else:
      print("An unexpected error occurred. Please try again.")
      break

# main program loop
courses = load_courses() # load the courses from the CSV file

while True:
    print("\nCourse Management Menu:") # print the menu 
    print("1. Display courses")
    print("2. Add a new course")
    print("3. Modify a course")
    print("4. Exit")

    choice = input("Enter your choice: ") # get the choice

    if choice == '1':  # display courses
        display_courses(courses)
    elif choice == '2':  # add a new course
        add_course(courses)
        save_courses(courses)  # save the updated courses to the CSV file
    elif choice == '3':  # modify a course
        modify_course(courses)
        save_courses(courses)  # save the updated courses to the CSV file
    elif choice == '4':  # exit the program
        print("Exiting...")
        break  # exit the loop
    else:
        print("Invalid choice.")  # print an error message if the choice is invalid
