# class to test
class AnonymousSurvey:
    """collect anonymous answers to a survey questions"""
    def __init__(self, question):
        """ Store a question, and prepare to store responses """
        self.question = question
        self.responses = []

    def show_question(self):
        """"""
        print(self.question)

    def store_response(self,response):
        """"""
        self.responses.append(response)

    def show_response(self):
        """"""
        for response in self.responses:
            print(response)
