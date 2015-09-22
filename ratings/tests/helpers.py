"""
This file provides convenient access to specific values for use in tests.
"""

class RatingValues(object):
    """
    Provides values for use in Rating objects. Each value is weighted by a
    preferred attribute.
    """
    @staticmethod
    def prefer_code():
        """
        Provides rating values weighted toward code quality
        """
        return {
            'code_quality': 100,
            'documentation': 50,
            'problem_solving': 50,
            'effort': 50,
            'creativity': 50,
            'originality': 50,
        }

    @staticmethod
    def prefer_problem_solving():
        """
        Provides rating values weighted toward problem solving
        """
        return {
            'code_quality': 50,
            'documentation': 50,
            'problem_solving': 100,
            'effort': 50,
            'creativity': 50,
            'originality': 50,
        }

    @staticmethod
    def prefer_effort():
        """
        Provides rating values weighted toward effort
        """
        return {
            'code_quality': 50,
            'documentation': 50,
            'problem_solving': 50,
            'effort': 100,
            'creativity': 50,
            'originality': 50,
        }

    @staticmethod
    def prefer_creativity():
        """
        Provides rating values weighted toward creativity
        """
        return {
            'code_quality': 25,
            'documentation': 25,
            'problem_solving': 50,
            'effort': 75,
            'creativity': 100,
            'originality': 50,
        }
