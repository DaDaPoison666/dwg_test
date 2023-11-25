# Automated Tests for the Wikipedia pages

This repository contains automated tests for the Wikipedia search engine. The tests are written in Python using the pytest library. Allure is used for reporting.

## Requirements

- Python 3.11 and above
- PostgreSQL
- Allure (for reports)

## Installing Dependencies

```pip install -r requirements.txt```
Setting up the Database
The tests use a PostgreSQL database.

## Running Tests

```pytest -s --alluredir results```
```allure generate ./allure-results --clean```
- The -s flag prints the test output to the console.
- Allure reports are stored in the results folder.
- Link for allure reports: https://dadapoison666.github.io/dwg_test/allure-report/
## GitLab CI/CD Integration
This project is set up to automatically run tests on every commit in GitLab. Test results and Allure reports are available in the GitLab CI/CD interface.

