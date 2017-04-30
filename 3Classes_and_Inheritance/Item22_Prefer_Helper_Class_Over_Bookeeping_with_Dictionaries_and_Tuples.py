class SimleGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grad(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


# book = SimleGradebook()
# book.add_student('Isaac Newton')
# book.report_grade('Isaac Newton', 90)
# print(book.average_grad('Isaac Newton'))
#
# grades = []
# grades.append((95, 0.45, 'Great job'))
# grades.append((85, 0.55, 'Better next time'))
# total = sum(score * weight for score, weight, _ in grades)
# total_weight = sum(weight for _, weight, _ in grades)
# average_grade = total / total_weight
# print(average_grade)

import collections

Grade = collections.namedtuple('Grade', ('score', 'weight'))


class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student(object):
    def __init__(self):
        self._subjects={}

    def subject(self,name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0,0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count+=1
        return total/count


class Gradebook(object):
    def __init__(self):
        self.__students = {}

    def student(self,name):
        if name not in self.__students:
            self.__students[name] = Student()
        return self.__students[name]


# Example 15
book = Gradebook()
albert = book.student('Albert Einstein')
math = albert.subject('Math')
math.report_grade(80, 0.10)
math.report_grade(80, 0.10)
math.report_grade(70, 0.80)
gym = albert.subject('Gym')
gym.report_grade(100, 0.40)
gym.report_grade(85, 0.60)
print(albert.average_grade())