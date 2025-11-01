class student:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z

    def display(self):
        print("Student Name:{}\nrollno: {}\nMarks:{}".format(self.name,self.rollno,self.marks))
s1=student("Trisha",214,95)
s1.display()
s2=student("Sunny",126,100)
s2.display()
