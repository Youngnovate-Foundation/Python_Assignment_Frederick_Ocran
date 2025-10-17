class Student:    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
    # Private attribute (encapsulation)
        self.__grade = grade  
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.__grade}")
        print("-" * 20)
    
    # Getter method for grade (encapsulation)
    def get_grade(self):
        return self.__grade
    
    # Setter method for grade (encapsulation)
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")

class GraduateStudent(Student):    
    def __init__(self, name, age, grade, degree):
        # Call the parent (Student) constructor
        super().__init__(name, age, grade)
        self.degree = degree  # New attribute for GraduateStudent
    
    # Override display_info to also show degree
    def display_info(self):
        super().display_info()  # Call the parent display_info()
        print(f"Degree: {self.degree}")
        print("-" * 20)


# Create students
student1 = Student("Fred", 20, 81)
student2 = Student("Helios", 19, 75)
grad_student = GraduateStudent("Ocran", 24, 85, "MSc Python Programming")

# Use setter to update a grade (Encapsulation)
student2.set_grade(80)

# Print details (Polymorphism: GraduateStudent's display_info is different!)
print("STUDENT DETAILS")
student1.display_info()
student2.display_info()
grad_student.display_info()

# Demonstrate getter use
print(f"{student1.name}'s grade: {student1.get_grade()}")
print(f"{student2.name}'s grade: {student2.get_grade()}")
print(f"{grad_student.name}'s grade: {grad_student.get_grade()}")
