#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main() {
  string password;
  cout << "Enter your password: ";
  cin >> password;

  int strength = 0;

  // Check password length
  int length = password.length();
  cout << "Length of the password is: " << length << endl;

  // Check for uppercase letters
  bool hasUppercase = false;
  for (char c : password) {
    if (isupper(c)) {
      hasUppercase = true;
      break;
    }
  }
  if (hasUppercase) {
    strength += 1;
  }

  // Check for lowercase letters
  bool hasLowercase = false;
  for (char c : password) {
    if (islower(c)) {
      hasLowercase = true;
      break;
    }
  }
  if (hasLowercase) {
    strength += 1;
  }

  // Check for digits
  bool hasDigit = false;
  for (char c : password) {
    if (isdigit(c)) {
      hasDigit = true;
      break;
    }
  }
  if (hasDigit) {
    strength += 1;
  }

  // Check for special characters
  bool hasSpecialChar = false;
  for (char c : password) {
    if (!isalnum(c)) {
      hasSpecialChar = true;
      break;
    }
  }
  if (hasSpecialChar) {
    strength += 1;
  }

  // Determine password strength level
  string strengthLevel;
  if (strength >= 5) {
    strengthLevel = "Very Strong";
  } else if (strength >= 3) {
    strengthLevel = "Strong";
  } else if (strength >= 1) {
    strengthLevel = "Weak";
  } else {
    strengthLevel = "Very Weak";
  }

  cout << "Password strength: " << strengthLevel << endl;

  return 0;
}