"""
This module provides a PasswordChecker class to evaluate the strength of passwords
and provide feedback on how to improve them.
"""

import re

class PasswordChecker:
    """
    A class to check the strength of passwords and provide feedback.
    """
    def __init__(self):
        """
        Initializes the PasswordChecker with a list of common passwords and an empty list of previous passwords.
        """
        self.common_passwords = [
            "123456", "password", "123456789", "12345678", "12345",
            "1234567", "1234567890", "qwerty", "abc123", "password1",
            "111111", "123123", "admin", "letmein", "welcome",
            "UNKNOWN", "Password", "Admin123", "iloveyou", "user"
        ]
        self.previous_passwords = []

    def check_strength(self, password):
        """
        Checks the strength of the given password.

        Args:
            password (str): The password to check.

        Returns:
            str: The strength of the password.
        """
        if password in self.common_passwords:
            return "Very Weak (Common Password)"
        if password in self.previous_passwords:
            return "Very Weak (Previously Used Password)"
        
        length_criteria = len(password) >= 8
        lowercase_criteria = bool(re.search(r'[a-z]', password))
        uppercase_criteria = bool(re.search(r'[A-Z]', password))
        number_criteria = bool(re.search(r'[0-9]', password))
        special_criteria = bool(re.search(r'[\W_]', password))

        criteria_met = sum([
            length_criteria, lowercase_criteria, uppercase_criteria, 
            number_criteria, special_criteria
        ])

        if not length_criteria:
            return "Very Weak (Too Short)"
        if criteria_met == 5:
            return "Very Strong"
        if criteria_met == 4:
            return "Strong"
        if criteria_met == 3:
            return "Moderate"
        if criteria_met == 2:
            return "Weak"
        return "Very Weak"

    def add_previous_password(self, password):
        """
        Adds the given password to the list of previous passwords.

        Args:
            password (str): The password to add.
        """
        if len(self.previous_passwords) >= 5:
            self.previous_passwords.pop(0)
        self.previous_passwords.append(password)

    def provide_feedback(self, password):
        """
        Provides feedback on how to make the password stronger.

        Args:
            password (str): The password to provide feedback for.

        Returns:
            list: A list of feedback suggestions.
        """
        feedback = []
        if len(password) < 8:
            feedback.append("Password should be at least 8 characters long.")
        if not re.search(r'[a-z]', password):
            feedback.append("Password should include at least one lowercase letter.")
        if not re.search(r'[A-Z]', password):
            feedback.append("Password should include at least one uppercase letter.")
        if not re.search(r'[0-9]', password):
            feedback.append("Password should include at least one number.")
        if not re.search(r'[\W_]', password):
            feedback.append("Password should include at least one special character.")
        return feedback

    def create_and_check_password(self):
        """
        Prompts the user to enter a new password and checks its strength.
        """
        while True:
            password = input("Enter a new password (or type 'quit' to exit): ")
            if password.lower() == 'quit':
                print("Exiting password checker.")
                break
            strength = self.check_strength(password)
            print(f"Password strength: {strength}")
            if strength in {'Strong', 'Very Strong'}:
                self.add_previous_password(password)
                print("Password accepted.")
            else:
                feedback = self.provide_feedback(password)
                print("Password is not strong enough. Please try again.")
                for suggestion in feedback:
                    print(f"- {suggestion}")

# Example usage:
if __name__ == "__main__":
    checker = PasswordChecker()
    checker.create_and_check_password()
