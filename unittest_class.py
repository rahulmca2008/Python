# we will write test for class
# in order to have common setup for all test case , setUp() method is used in Test class
from dev_class import AnonymousSurvey
import unittest

class TestAnonymousSurvey(unittest.TestCase):
    """ Test class Anonymous Survey """
    def setUp(self):
        """
        create a survey and a set of response for use in all test methods
        """
        question = "What language did you first learn to speak ?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Kannada','Hindi','English']

    def test_store_single_response(self):
        """ Test that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_response(self):
        """ Test that 3 responses are stored properly """
        for response in self.responses[:3]:
            self.my_survey.store_response(response)
        for response in self.responses[:3]:
            self.assertIn(response,self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()

