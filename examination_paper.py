import time
from question import *


class ExaminationPaper:
    @property
    def student_name(self):
        return self.__student_name

    @student_name.setter
    def student_name(self, value):
        self.__student_name = value

    @property
    def student_info(self):
        return self.__student_info

    @student_info.setter
    def student_info(self, value):
        self.__student_info = value

    @property
    def date(self):
        return self.__date

    @property
    def questions(self):
        return self.__questions

    @property
    def grades(self):
        return self.__grades

    def is_finish(self):
        return True if self.grades != -1 else False

    @staticmethod
    def __include(li, item):
        result = False
        for i in li:
            if item == i:
                result = True
        return result

    # 生成试题时，检测试题是否重复
    def __generate_questions(self, question_number):
        index = 0
        while index < question_number:
            q = Question(100)
            if self.__include(self.questions, q):
                continue
            else:
                self.questions.append(q)
                index += 1


    def check(self, answers):
        self.__answers = answers
        right_num = 0
        index = 0
        while index < len(self.questions):
            try:
                answer = int(answers[index])
                if self.questions[index].answer == answer:
                    right_num += 1
            except ValueError:
                None
            index += 1
        self.__grades = 100 * right_num / len(self.questions)

    def __init__(self, question_number=10):
        self.__grades = -1
        self.__answers = []
        self.__student_info = ""
        self.__student_name = ""
        self.__date = time.asctime(time.localtime(time.time()))
        self.__questions = []
        self.__generate_questions(question_number)

    def get_right_answer(self):
        index = 0
        result = ""
        while index < len(self.questions):
            result += str(index + 1) + ". " + str(self.questions[index].answer) + ";\n"
            index += 1
        return result

    def __str__(self):
        result = "================================================================================================\n"
        result += "试卷生成时间：" + self.date+"\n"
        result += "姓名：" + self.student_name + "\n"
        result += "学校信息：" + self.student_info + "\n"
        result += "============================================密封线===============================================\n"
        index = 0
        while index < len(self.questions):
            result += str(self.questions[index]) + " " + self.__answers[index] + "\t正确答案：" + str(self.questions[index].answer) + "\n"
            index += 1
        result += "============================================得分=================================================\n"
        result += str(self.grades) + " 分\n"
        result += "=================================================================================================\n\n"
        return result
