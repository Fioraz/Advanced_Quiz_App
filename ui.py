from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="helloooooooo", font=("Arial", 15, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        self.correct_img = PhotoImage(file="images/true.png")
        self.wrong_img = PhotoImage(file="images/false.png")

        self.correct_button = Button(image=self.correct_img, highlightthickness=0, command=self.tick_pressed)
        self.correct_button.grid(column=0, row=2)
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2)

        self.score_label = Label(bg=THEME_COLOR, fg="white", text=f"Score: 0")
        self.score_label.grid(column=1, row=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz!")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def tick_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
