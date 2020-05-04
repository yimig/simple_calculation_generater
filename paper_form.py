import tkinter as tk
from examination_paper import *
import shapes
import shapepainter as sp
from point import *
import tkinter.messagebox


class PaperForm:

    def __build_header(self):
        label_width = 5
        entry_width = 10
        frm_header = tk.Frame(self.__window)
        frm_name = tk.Frame(frm_header)
        tk.Label(frm_name, text="姓名：", width=label_width).pack(side="left")
        en_name = tk.Entry(frm_name, width=entry_width)
        en_name.pack(side="left")
        frm_name.pack(side="left")
        tk.Label(frm_header, width=10).pack(side="left")
        frm_info = tk.Frame(frm_header)
        tk.Label(frm_info, text="班级：", width=label_width).pack(side="left")
        en_info = tk.Entry(frm_info, width=entry_width)
        en_info.pack(side="right")
        frm_info.pack(side="left")
        tk.Label(frm_header, width=10).pack(side="left")
        tk.Button(frm_header, text="随机生成试题", width=10, command=self.__load_paper).pack(side="left")
        frm_header.pack()
        return [en_name, en_info]

    def __build_question_template(self, father_frm):
        frm_template = tk.Frame(father_frm)
        canvas = tk.Canvas(frm_template, width=50, height=50)
        shape = shapes.Oval(Point(25, 25), 25, 25)
        spointer = sp.ShapePainter(canvas, shape)
        spointer.fill("yellow")
        canvas.pack(side='left')
        lb_question = tk.Label(frm_template, text="? + ? =", width=10)
        lb_question.pack(side='left')
        en_answer = tk.Entry(frm_template, width=10)
        en_answer.pack(side='left')
        lb_answer = tk.Label(frm_template, text="", width=10)
        lb_answer.pack(side='left')
        return [frm_template, spointer]

    def __build_content(self):
        frm_content = tk.Frame(self.__window)
        frm_package = [self.__build_question_template(frm_content) for _ in range(10)]
        frm_questions = [frm_package[i][0] for i in range(10)]
        frm_colors = [frm_package[i][1] for i in range(10)]
        for i in range(5):
            for j in range(2):
                frm_questions[i * 2 + j].grid(row=i, column=j, padx=50, pady=20)
        frm_content.pack()
        return [frm_questions, frm_colors]

    def __build_footer(self):
        frm_footer = tk.Frame(self.__window)
        tk.Button(frm_footer, text="提交", width=20, command=self.__submit).pack(side="left")
        tk.Label(frm_footer, width=10).pack(side="left")
        btn_show = tk.Button(frm_footer, text="显示答案", width=20, command=self.__show_right_answer)
        btn_show["state"] = "disabled"
        btn_show.pack(side="left")
        frm_footer.pack()
        return btn_show

    def __load_paper(self):
        self.__paper = ExaminationPaper()
        for i in range(10):
            self.__shapes_pointer[i].fill("yellow")
            self.__question_group[i].winfo_children()[1]['text'] = str(self.__paper.questions[i])
            self.__question_group[i].winfo_children()[2].delete(0, tk.END)
            # 把之前做的清空
            self.__question_group[i].winfo_children()[3]['text'] = ""
        self.__btn_show_answer["state"] = "disabled"

    def __submit(self):
        if self.__paper is None:
            tkinter.messagebox.showinfo(title='Oops....', message='请先生成试题再提交')
        else:
            self.__btn_show_answer["state"] = "normal"
            self.__paper.student_name = self.__header_group[0].get()
            self.__paper.student_info = self.__header_group[1].get()
            self.__paper.check([self.__question_group[i].winfo_children()[2].get() for i in range(10)])
            self.__fill_color()
            tkinter.messagebox.showinfo(title='成绩公布', message=str(self.__paper.grades) + " 分\n试卷文件已保存在Exam_puple2020.txt")
            file = open("Exam_puple2020.txt", "a")
            file.write(str(self.__paper))

    def __fill_color(self):
        for i in range(10):
            if self.__question_group[i].winfo_children()[2].get() == str(self.__paper.questions[i].answer):
                self.__shapes_pointer[i].fill("green")
            else:
                self.__shapes_pointer[i].fill("red")

    def __show_right_answer(self):
        for i in range(10):
            self.__question_group[i].winfo_children()[3]['text'] = "答案：" + str(self.__paper.questions[i].answer)

    def __init__(self, window):
        self.__window = window
        self.__paper = None
        self.__header_group = self.__build_header()
        package = self.__build_content()
        self.__question_group = package[0]
        self.__shapes_pointer = package[1]
        self.__btn_show_answer = self.__build_footer()
