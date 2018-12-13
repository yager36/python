class student: # open a student class
    grade=0        
    ages=0
    num_student=0     # static variable
    avg_grades=0
    avg_age=0
    def __init__(self,name,grade,age):
        self.name=name            
        self.grade=grade     #constructor
        self.age=age
        student.num_student +=1  #sum the number of student
        student.sum_num_student(self)
    def print(self):      # print funcion print the details  is the student
        print("student name: {} student age: {} student grade: {}".format(self.name,self.age,self.grade))       
     
    def sum_num_student (self):                # sum the grades and the ages
        student.grade +=int(self.grade)  
        student.ages += int(self.age)
    @classmethod
    def avg(avg_all):     # funcion calculates the average in the class
        avg=avg_all.grade/avg_all.num_student
        print("the grades average is:{f:1.4}" .format(f=avg))
s1=student("ben",90,29)
s2=student("naor",86,24)    
s3=student("yanay",92,27) 
s4=student("igal",55,31) 
student.print(s1)
student.print(s2)
s3.print()
s4.print()
student.avg()



   





