from pytest_check import check

class Assertion:

    @staticmethod
    @check.check_func
    def assertion_equal(actual, expected):
        assert actual == expected, f'we expected {expected} but got {actual}'

    @staticmethod
    def assertion_more_then(actual, number):
        assert actual > number, f'we expected that {actual} is more then {number}, but actually it does not'

    @staticmethod
    def assertion_not_equal(actual, expected):
        assert actual != expected
