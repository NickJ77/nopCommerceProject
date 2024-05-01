# nopCommerce-Automation-Testing-Project


## Project Overview<a id="project-overview"></a>

This project is an automation testing suite for the nopCommerce e-commerce platform, built using Python, Selenium WebDriver, and the Page Object Model (POM) design pattern. The goal of this project is to create a comprehensive and maintainable set of automated tests to ensure the functionality and reliability of the nopCommerce application.



## Table of Contents:

- [About The App](#about-the-app)
- [Tools](#tools)
- [Setup](#setup)
- [Approach](#approach)

## About The App

NopCommerce is an open-source e-commerce platform that provides a comprehensive set of features and functionalities for building and managing online stores. nopCommerce is a robust, feature-rich and customizable open-source e-commerce platform suitable for businesses that need a high degree of control and flexibility over their online store.

## Tools
I used `Python`, `Selenium`, `Pytest`, `Pycharm`

## Setup
- Install Python 3.9 or higher on your system.
- Set up a virtual environment using a tool like `venv`
- Install the required Python packages by running `pip install -r requirements.txt` or by creating a new file and naming it `requirements.txt`
- Install the required Python packages by running `pip install -r pytest.ini` or by creating a new file and naming it `pytest.ini`
- Install `pip install webdriver-manager` or intall using the python interpreter in pycharm
- Install `pip install pytest` or intall using the python interpreter in pycharm
- Install `pip install pytest-xdist` or intall using the python interpreter in pycharm
- Install `pip install pytest-html` or intall using the python interpreter in pycharm
- Configure the WebDriver path and other settings in the `conftest.py` file.
- Open the project in PyCharm and ensure the interpreter is set to the virtual environment.



## Approach

Here is some information about an automation testing project. It's built using the Page Object Model (POM) design pattern to ensure a maintainable test suite. Each page of the nopCommerce application is represented by a corresponding Page Object class, which contains the page's elements and actions. The test cases are organized by functionality, and each test module focuses on a specific aspect of the application. The Base Page class contains the common functionality and elements shared across multiple application pages, making the test suite more maintainable.

**Challenge:** However, I encountered some challenges while working on this project. One of the main challenges I faced was that the nopCommerce website did not consistently save the user account credentials after a new account was created, causing issues with the login process during test execution. This led to inconsistent test results and made it difficult to maintain the test suite.

**Solution:** To address this challenge, I created an AccountCreationPage class containing the account creation functionality, including input fields for personal information, username, password, and other relevant elements. I ensured that the AccountCreationPage class was inherited from the BasePage class, which handled the common functionality and setup for all the page objects. In the AccountCreationPage class, I defined a create_account() method that takes the necessary user information as parameters and performs the account creation process. In the test cases that require a new user account, I used the account creation fixture to create a new account. After the account was created, I used the login workflow to ensure the user could successfully log in with the newly created credentials. I also implemented assertions to validate the successful login processes.

**Challenge:** In this project, I encountered issues that caused pages to load unexpectedly long, render elements, or perform specific actions, leading to timeout exceptions in the Selenium-based test suite. These timeout exceptions caused test failures, making the test suite unreliable.

**Solution:** In the BasePage class, I used the provided  wait_until_element_is_visible() and _wait_until_element_is_clickable() 
methods to handle element visibility and clickability checks. In the individual Page Object classes, I used a combination of element attributes, such as CSS selectors and XPath, to create more resilient locator strategies. This approach made the locators less susceptible to changes in the DOM structure, reducing the likelihood of exceptions and improving the overall reliability of the test suite. I analyzed the nopCommerce application and identified any pages or sections that were particularly slow to load or render. I then Integrated the test suite with a reporting framework, such as pytest-html or allure-pytest, to generate detailed reports about timeout-related failures. I identified and addressed recurring timeout issues in the nopCommerce application.

**Challenge:** Finally, I encountered some test cases that exhibited inconsistent or "flaky" behavior, passing in one run and failing in another.
 
**Solution:** To address this, I identified the root causes of the flaky test cases by analyzing the test logs and debugging the failures.
