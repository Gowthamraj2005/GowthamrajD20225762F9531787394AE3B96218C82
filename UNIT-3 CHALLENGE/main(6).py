class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"{self.name} (Roll No: {self.roll_number}, CGPA: {self.cgpa})"

def sort_students(student_list):
    
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students


if __name__ == "__main__":
  
   
    students = [ 
        Student("Mark", "100", 3.9),
        Student("Antony","106",3.7),
        Student("Jakey","108",3.8),
        Student("Madhan", "112", 3.0),
    ]

   
    sorted_students = sort_students(students)
  
    
    for student in sorted_students:
      print(student)
      
        
      