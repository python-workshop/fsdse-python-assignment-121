from unittest import TestCase


class TestBuild(TestCase):
    #check whether the values are there
    #check whether its number else false
    #check the result is true
    def test_check_whether_the_values_are_there(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Not defiend")

        result = build(None)
        self.assertEqual(False,result)

    def test_check_whether_its_number_else_false(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Not defiend")

        result = build([])
        self.assertEqual(False, result)

    def test_check_the_result_is_true(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Not defiend")

        result = build([12,13,12])
        self.assertTrue([12,13], result)
