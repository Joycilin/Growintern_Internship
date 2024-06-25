import requests
import re
import json
from bs4 import BeautifulSoup

def scan_website(url):
    """
    Scans a website for common vulnerabilities.
    Args:
        url: The URL of the website to scan.
    Returns:
        A dictionary containing the vulnerabilities found and their remediation steps.
    """

    vulnerabilities = {}

    # Check for XSS vulnerabilities
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for script in soup.find_all('script'):
            if 'src' in script.attrs:
                script_url = script['src']
                if re.match(r'^http', script_url):
                    # Check if the script is loaded from an external source
                    vulnerabilities['XSS'] = {
                        'description': 'Cross-site scripting (XSS) vulnerability found in the website.',
                        'remediation': 'Sanitize all user input before displaying it on the website. Validate all data from external sources before using it.'
                    }
                    break
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    # Check for SQL injection vulnerabilities
    try:
        response = requests.get(url + '?id=1')
        soup = BeautifulSoup(response.text, 'html.parser')
        if 'You are logged in' in soup.text:
            vulnerabilities['SQL Injection'] = {
                'description': 'SQL injection vulnerability found in the website.',
                'remediation': 'Use parameterized queries to prevent SQL injection attacks.'
            }
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    # Check for other vulnerabilities (e.g., open ports, weak passwords)
    # ...

    return vulnerabilities

def main():
    """
    Main function to run the automated scanner.
    """

    url = input("Enter the URL of the website to scan: ")
    vulnerabilities = scan_website(url)

    if vulnerabilities:
        print("\nVulnerabilities found:")
        for vulnerability, details in vulnerabilities.items():
            print(f"  - {vulnerability}:")
            print(f"    Description: {details['description']}")
            print(f"    Remediation: {details['remediation']}")
    else:
        print("\nNo vulnerabilities found.")

if __name__ == "__main__":
    main()
 