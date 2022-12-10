
class Assertion:

    @staticmethod
    def assertion(actual, expected):
        assert actual == expected, f'we expected {expected} but got {actual}'