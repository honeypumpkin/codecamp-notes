# lets build dictionaries that represent students at college

student1 = {
    'first': 'Chris',
    'last' : 'xx',
    'id': 1234567,
    'date_of_birth': '7/30/82',
    'number_of_credits': 45,
    'quality_score': 180
}

student2 = {
    'first': 'Robin',
    'last' : 'Avila',
    'id': 9876543,
    'date_of_birth': '12/07/71',
    'number_of_credits': 55,
    'quality_score': 108

}


class Student:
    # data
    def __init__(self, first_name, last_name, student_id, quality_score=0, number_of_credits=0):
        #note that any parameter with a default value needs to be last in the list
        self.first_name = first_name
        self.last_name = last_name
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


# objects
chris = Student('Chris', 'Bay', 123456)
chris.add_grade(4.0, 5)
chris.add_grade(2, 3)
chris.add_grade(3, 4)

corey = Student('Corey', 'Lewis', 65432)


