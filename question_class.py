"""
Question classes

"""


class Question:
    """
    Base Question class

    Attributes:
        question: The question.
        answers: Possible answers to choose from.
        solution: The correct answer/s to the question.
    """
    pass


class TextQ(Question):
    """
    Question class with question and answers solely composed of text.
    """
    def __init__(self,
                 question_text: str,
                 answers: tuple,
                 solution: tuple=None):
        self.question_text = question_text
        self.answers = answers
        self.num_answers = len(answers) + 1  # for use with 'in range(num_answers)
        # for more than one answer, use tuple, or slice? This will output a list
        # eg answers = [1, 2, 3, 4] => correct = [1:4:2] => correct >>> [2, 4]
        self.solution = solution

        # assert all solutions  are in the answer choices
        if solution is not None:
            assert set(solution) & set(answers) == set(solution),\
                "Answer not in answer choices."

# These methods should be inherited or extend methods from base class.
# They may need to be decorated to enable correction/modification via GUI


# test cases
# test_q1 = TextQ('Hope this works', ('1', '2', 3), (3, '1'))
# test_q2 = TextQ('Hope this works to throw an error', (1, 2, 3), (3, 7))