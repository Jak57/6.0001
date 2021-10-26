# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 09:45:48 2021

@author: jakir
"""

###########
# Book
###########

###
# Example: Inheritance - MIT Person
###

# import datetime

# class Person(object):
    
#     def __init__(self, name):
#         """
#         Create a person

#         """
#         self.name = name
        
#         try:
#             lastBlank = name.rindex(' ')
#             self.lastName = name[lastBlank+1:]
#         except:
#             self.lastName = name
        
#         self.birthday = None
        
        
#     def getName(self):
#         """
#         Returns self's full name

#         """
#         return self.name
     
#     def getLastName(self):
#         """
#         Returns self's last name

#         """
#         return self.lastName
    
#     def setBirthday(self, birthdate):
#         """
#         Assumes birthdate of type datetime.date
#         Set's self's birthday to birthdate

#         """
        
#         self.birthday = birthdate
    
#     def getAge(self):
#         """
#         Returns self's current age ind days

#         """
#         if self.birthday == None:
#             raise ValueError
#         else:
#             return (datetime.date.today() - self.birthday).days
    
#     def __lt__(self, other):
#         """
#         Returns True if self preceds other in alphabetical order on last
#         names, but if they are same full names are compared.

#         """
#         if self.lastName == other.lastName:
#             return self.name < other.name
        
#         return self.lastName < other.lastName
    
#     def __str__(self):
#         """
#         Returns self's name

#         """
#         return self.name


# # subclass of parent class
# class MITPerson(Person):
    
#     nextIdNum = 0 # identification number
    
#     def __init__(self, name):
#         Person.__init__(self, name)
#         self.idNum = MITPerson.nextIdNum
#         MITPerson.nextIdNum += 1
    
#     def getIdNum(self):
#         return self.idNum
    
#     def __lt__(self, other):
#         return self.idNum < other.idNum
    
#     def isStudent(self, other):
#         return isinstance(self, other)
    
# # p1 = MITPerson("Barbara Beaver")
# # print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))
    
# # p2 = MITPerson("Justin Beaver")
# # print(str(p2) + '\'s id number is ' + str(p2.getIdNum()))

# # p1 = MITPerson("Mark Guttag")
# # p2 = MITPerson("Billy Bob Beaver")
# # p3 = MITPerson("Billy Bob Beaver")
# # p4 = Person("Billy Bob Beaver")

# # print("p1 < p2 =", p1 < p2)
# # print("p3 < p2 =", p3 < p2)
# # print("p4 < p1 =", p4 < p1)

# # # print("p1 < p4 =", p1 < p4) # AttributeError: Person object has no attribute idName


# class Student(MITPerson):
#     pass

# class UG(Student):
    
#     def __init__(self, name, classYear):
#         MITPerson.__init__(self, name)
#         self.classYear = classYear
        
#     def getClass(self):
#         return self.classYear
    
# class Grad(Student):
#     pass
#     # pass indicates this class has no attributes other
#     # than those are inherited from superclass.

# # p5 = Grad("Buzz Aldrin")
# # p6 = UG("Billy Beaver", 1984)

# # print(p5,"is a graduate student =", type(p5) == Grad)
# # print(p5, "is a undergraduate student =", type(p5) == UG)

# # print(p5, "is a student is", p5.isStudent(Student))
# # print(p6, "is a student is", p6.isStudent(Student))
# # print(p3, "is a student is", p3.isStudent(Student))

# class TransferStudent(Student):
    
#     def __init__(self, name, fromSchool):
#         MITPerson.__init__(self, name)
#         self.fromSchool = fromSchool
    
#     def getOldSchool(self):
#         return self.fromSchool

# # p7 = TransferStudent("David Malan", "Harvard University")
# # print(p7, "is a student is", p7.isStudent(Student))


# class Grades(object):
    
#     def __init__(self):
#         """
#         Creates empty grade book.

#         """
#         self.students = []
#         self.grades = {}
#         self.isSorted = True
        
#     def addStudent(self, student):
#         """
#         Assumes student of type Student. Add student to the grade book.

#         """
        
#         if student in self.students:
#             raise ValueError("Duplicate student")
        
#         self.students.append(student)
#         self.grades[student.getIdNum()] = []
#         self.isSorted = False
#         # print(self.grades)
    
#     def addGrade(self, student, grade):
#         """
#         Assumes grade is a float. Add grade to the list of grades for student.

#         """
#         try:
#             self.grades[student.getIdNum()].append(grade)
#             # print("hi", self.grades)
#         except:
#             raise ValueError("Student not in mapping.")
            
#     def getGrades(self, student):
#         """
#         Returns a list of grades for student.

#         """
    
#         try:
#             # print("hello")
#             # print(student, student.getIdNum())
#             # print(self.grades[student.getIdNum()])
#             return self.grades[student.getIdNum()] # return copy of grades
#         except:
#             raise ValueError("Student not in mapping.")
    
#     def getStudents(self):
#         """
#         Returns a sorted list of students in the grade book
#         """
        
#         if not self.isSorted:
#             self.students.sort()
#             self.isSorted = True
#         return self.students[:] # return copy of list of students
    
# #****#
# def gradeReport(course):
#     """
#     Assumes grade of type Grades.

#     """   
#     report = ""
#     for s in course.getStudents():
#         tot = 0.0
#         numGrades = 0
#         for g in course.getGrades(s):
#             tot += g
#             numGrades += 1
        
#         try:
#             average = tot/numGrades
#             report = report + '\n' + str(s) + '\'s mean grade is ' + str(average)
#         except ZeroDivisionError:
#             report = report + '\n' + str(s) + ' has no grades'
    
#     return report

# ug1 = UG("Jane Doe", 2014)
# ug2 = UG("John Doe", 2015)
# ug3 = UG("David Henry", 2003)

# g1 = Grad("Billy Buckner")
# g2 = Grad("Bucky F. Dent")

# sixHundred = Grades()

# sixHundred.addStudent(ug1)
# sixHundred.addStudent(ug2)
# sixHundred.addStudent(g1)
# sixHundred.addStudent(g2)

# for s in sixHundred.getStudents():
#     sixHundred.addGrade(s, 75)

# sixHundred.addGrade(g1, 25)
# sixHundred.addGrade(g2, 100)
# sixHundred.addStudent(ug3)

# print(gradeReport(sixHundred))


####
# Example: Information hiding
####

# class InfoHiding(object):
    
#     def __init__(self):
#         self.visible = 'Look at me'
#         self.__alsoVisible__ = 'Look at me too'
#         self.__invisible = 'Don\'t look at me directly'

#     def printVisible(self):
#         print(self.visible)
        
    
#     def printInvisible(self):
#         print(self.__invisible)
    
#     def __printInvisible(self):
#         print(self.__invisible)
        
    
#     def __printInvisible__(self):
#         print(self.__invisible)

# # test = InfoHiding()
# # print(test.visible)
# # print(test.__alsoVisible__)
# # print(test.__invisible)

# # test.printInvisible()
# # test.__printInvisible__()
# # test.__printInvisible()

# class SubClass(InfoHiding):
#     def __init__(self):
#         print('from subclass', self.__invisible)
        

# testSub = SubClass()



##########
# Slide
##########


########
# Animal abstract data type
########

# class Animal(object):
    
#     def __init__(self, age):
#         self.age = age
#         self.name = None
    
#     # Getter methods
#     def get_age(self):
#         return self.age
    
#     def get_name(self):
#         return self.name
    
#     # Setter methods
#     def set_age(self, newage):
#         self.age = newage
    
#     def set_name(self, newname=""):
#         self.name = newname
        
#     def __str__(self):
#         return "animal:" + str(self.name) + ":" + str(self.age)
    

# print("\n-----animal tests------")
# a = Animal(4)
# print(a)

# a.set_name("fluffy")
# print(a)
# a.set_name()
# print(a)

# #######
# # Inheritance example
# #######

# class Cat(Animal):
#     def speak(self):
#         print("meow")
    
#     def __str__(self):
#         return "animal:" + str(self.name) + ":" + str(self.age)
    
# print("\n------cat tests -----")

# c = Cat(5)
# c.set_name("fluffy")
# print(c)
# c.speak()
# print(c.get_age())
# # a.speak()

# ###########

# class Person(Animal):
    
#     def __init__(self, name, age):
#         Animal.__init__(self, age)
#         self.set_name(name)
#         self.friends = []
    
#     def get_friends(self):
#         return self.friends
    
#     def speak(self):
#         print("hello")
        
#     def add_friend(self, fname):
#         if fname not in self.friends:
#             self.friends.append(fname)
            
#     def age_diff(self, other):
#         diff = self.age - other.age
#         print(abs(diff), "year difference")
    
#     def __str__(self):
#         return "person:" + str(self.name) + ":" + str(self.age)
    
# print("\n----- person tests -----")  
# p1 = Person("jack", 30)
# p2 = Person("jill", 25)

# print(p1.get_name())
# print(p1.get_age())
# print(p2.get_name())
# print(p2.get_age())

# print(p1)
# p1.speak()
# p1.age_diff(p2)


# ##########
# import random

# class Student(Person):
    
#     def __init__(self, name, age, major=None):
#         Person.__init__(self, name, age)
#         self.major = major

#     def change_major(self, major):
#         self.major = major
    
#     def speak(self):
#         r = random.random()
        
#         if r < 0.25:
#             print("i have homework")
#         elif r >= 0.25 and r < 0.5:
#             print("i need sleep")
#         elif r >= 0.5 and r < 0.75:
#             print("i should eat")
#         else:
#             print("i am watching tv")
    
#     def __str__(self):
#         return "student:" + str(self.name) + ":" + str(self.age) + ":" + str(self.major)
    

# print("\n------ student tests ------")
# s1 = Student('alice', 20, 'CS')
# s2 = Student('beth', 18)

# print(s1)
# print(s2)
# print(s1.get_name(), "says:", end=" ")
# s1.speak()
# print(s2.get_name(), "says:", end=" ")
# s2.speak()

# #######
# # Use of class variable
# #######

# class Rabbit(Animal):
#     tag = 1
    
#     def __init__(self, age, parent1=None, parent2=None):
#         Animal.__init__(self, age)
#         self.parent1 = parent1
#         self.parent2 = parent2
        
#         self.rid = Rabbit.tag
#         Rabbit.tag += 1
        
#     def get_rid(self):
#         return str(self.rid).zfill(3)
    
#     def get_parent1(self):
#         return self.parent1
    
#     def get_parent2(self):
#         return self.parent2
    
#     def __add__(self, other):
#         return Rabbit(0, self, other)
    
#     def __eq__(self, other):
#         parents_same = self.parent1.rid == other.parent1.rid\
#             and self.parent2.rid == other.parent2.rid
        
#         parents_opposite = self.parent1.rid == other.parent2.rid\
#             and self.parent2.rid == other.parent1.rid
        
#         return parents_same or parents_opposite
    
#     def __str__(self):
#         return "rabbit:" + self.get_rid()
    
# print("\n----- rabbit tests -----")
# print("---- testing creating rabbits -----")
# r1 = Rabbit(3)
# r2 = Rabbit(4)
# r3 = Rabbit(5)

# print("r1:", r1)
# print("r2:", r2)
# print("r3:", r3)

# print("r1 parent1:", r1.get_parent1())
# print("r1 parent2:", r1.get_parent2())

# print("----- testing rabbit addition ----")
# r4 = r1+r2
# print("r1:", r1)
# print("r2:", r2)
# print("r4:", r4)

# print("r4 parent1:", r4.get_parent1())
# print("r4 parent2:", r4.get_parent2())

# print("---- testing rabbit equality ----")
# r5 = r3 + r4
# r6 = r4 + r3

# print("r3:", r3)
# print("r4:", r4)
# print("r5:", r5)
# print("r6:", r6)

# print("r5 parent1:", r5.get_parent1())
# print("r5 parent2:", r5.get_parent2())
# print("r6 parent1:", r6.get_parent1())
# print("r6 parent2:", r6.get_parent2())

# print("r5 and r6 have same parents?", r5 == r6)
# print("r4 and r6 have same parents?", r4 == r6)



