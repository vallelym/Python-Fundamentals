import unittest
from password_checker import PasswordChecker

class TestPasswordChecker(unittest.TestCase):
    def setUp(self):
        self.checker = PasswordChecker()

    def test_common_password(self):
        self.assertEqual(self.checker.check_strength("123456"), "Very Weak (Common Password)")

    def test_previous_password(self):
        self.checker.add_previous_password("P@ssw0rd123")
        self.assertEqual(self.checker.check_strength("P@ssw0rd123"), "Very Weak (Previously Used Password)")

    def test_too_short_password(self):
        self.assertEqual(self.checker.check_strength("F1v£"), "Very Weak (Too Short)")

    def test_weak_password(self):
        self.assertEqual(self.checker.check_strength("password"), "Very Weak (Common Password)")
        self.assertEqual(self.checker.check_strength("12345678"), "Very Weak (Common Password)")

    def test_moderate_password(self):
        self.assertEqual(self.checker.check_strength("Password1"), "Moderate")

    def test_strong_password(self):
        self.assertEqual(self.checker.check_strength("Password1!"), "Strong")

    def test_very_strong_password(self):
        self.assertEqual(self.checker.check_strength("P@ssw0rd123!"), "Very Strong")

    def test_feedback_too_short(self):
        feedback = self.checker.provide_feedback("F1v£")
        self.assertIn("Password should be at least 8 characters long.", feedback)

    def test_feedback_missing_lowercase(self):
        feedback = self.checker.provide_feedback("PASSWORD1!")
        self.assertIn("Password should include at least one lowercase letter.", feedback)

    def test_feedback_missing_uppercase(self):
        feedback = self.checker.provide_feedback("password1!")
        self.assertIn("Password should include at least one uppercase letter.", feedback)

    def test_feedback_missing_number(self):
        feedback = self.checker.provide_feedback("Password!")
        self.assertIn("Password should include at least one number.", feedback)

    def test_feedback_missing_special(self):
        feedback = self.checker.provide_feedback("Password1")
        self.assertIn("Password should include at least one special character.", feedback)

if __name__ == '__main__':
    unittest.main()
