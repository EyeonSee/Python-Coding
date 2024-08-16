from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        """Abstract method to print the question."""
        pass
    
    @abstractmethod
    def check(self, answer: str):
        """Abstract method to check the user's answer."""
        pass

class YesNoQuestion(Question):
    def __init__(self, question: str, answer: bool):
        self.question = question
        self.answer = answer

    def print(self):
        print(f"[?] {self.question} (yes/no)")

    def check(self, user_answer: str):
        if user_answer.lower() == 'yes' and self.answer:
            return True
        elif user_answer.lower() == 'no' and not self.answer:
            return True
        else:
            return False

class OpenQuestion(Question):
    def __init__(self, question: str, answers: list):
        self.question = question
        self.answers = answers

    def print(self):
        print(f"[?] {self.question}")

    def check(self, user_answer: str):
        return user_answer in self.answers


class MultiOptionsQuestion(Question):
    def __init__(self, question: str, options: list, answer_index: int):
        self.question = question
        self.options = options
        self.answer_index = answer_index

    def print(self):
        print(f"[?] {self.question}\n")
        for i, option in enumerate(self.options, start=1):
            print(f"[{i}] {option}")

    def check(self, user_answer: str):
        try:
            return int(user_answer) == self.answer_index + 1
        except ValueError:
            return False

class Quiz:
    def __init__(self, questions: list):
        self.questions = questions


    def start(self):
        results = []
        for question in self.questions:
            question.print()
            print("")
            answer = input('[+] ')
            is_correct = question.check(answer)
            results.append(is_correct)
            print("")  # Add spacing after each question
            print("")
        self.print_results(results)


    def print_results(self, results):
        correct_count = sum(results)
        total_count = len(results)
        print(f'Your score is {correct_count}/{total_count}')
        print("")
        for i, result in enumerate(results, start=1):
            status = "Pass" if result else "Fail"
            print(f'[{i}] {status}')