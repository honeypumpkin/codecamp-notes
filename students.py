# Need to know HOW to make an inheritance class, and how to use it.

class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return first_name + ' ' + last_name

class Student(Person):
    # data
    def __init__(self, first_name, last_name, student_id, quality_score=0, number_of_credits=0):
        #note that any parameter with a default value needs to be last in the list
        
        Person.__init__(self, first_name, last_name) #tells the class to initialize  the sub for info
        #super().__init__(first_name, last_name)  can also use this

        self.student_id = student_id
        self.quality_score = quality_score
        self.number_of_credits = number_of_credits

    # behavior
    def get_fullname(self):
        return self.first_name + ' ' + self.last_name

    def add_grade(self, score, num_credits):
        self.number_of_credits += num_credits
        self.quality_score += score * num_credits

    def compute_gpa(self):
        if not self.number_of_credits:
            return 0
        else:
            return self.quality_score / self.number_of_credits

    def __str__(self):
        object_string = ''
        object_string += (self.last_name + ', ' + self.first_name + '\n')
        object_string += ('ID: ' + str(self.student_id) + '\n')
        object_string += ('GPA: ' + str(self.compute_gpa()))
        return object_string

class Instructor(Person):
    
    def __init__(self, first_name, last_name, department, instructor_id):

        Person.__init__(self, first_name, last_name)
        
        self.department = department
        self.instructor_id = instructor_id

class Course:

    def __init__(self, name, course_id, department, instructor, number_of_credits=3):
        self.name = name
        self.course_id = course_id
        self.department = department
        self.instructor = instructor
        self.number_of_credits = number_of_credits
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def enroll_students(self, students):
        for student in students:
            self.enroll_student(student)

    def print_roster(self):
        for student in self.students:
            print(student)
            print('----------')

    def __str__(self):
        object_string = ''
        object_string += (self.department + ' ' + str(self.course_id) + ': ' + self.name +  '\n')
        object_string += ('Enrolled: ' + str(len(self.students)))
    

codecamp = Course('Immersive CodeCamp' , 102, 'LC' , 'Chris Bay')
dom = Student('Dom' , 'Hallan', 1)
robin = Student('Robin', 'Avila', 2)
carolyn = Student('Carolyn', 'Peters', 3)

codecamp.enroll_students([dom, robin, carolyn])

codecamp.print_roster()




