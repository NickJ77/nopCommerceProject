# nopCommerce-Automation-Testing-Project


## Project Overview<a id="project-overview"></a>

This project is an automation testing suite for the nopCommerce e-commerce platform, built using Python, Selenium WebDriver, and the Page Object Model (POM) design pattern. The goal of this project is to create a comprehensive and maintainable set of automated tests to ensure the functionality and reliability of the nopCommerce application.



## Table of Content:

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

The automation testing project follows the Page Object Model (POM) design pattern to ensure a modular and maintainable test suite. Each page of the nopCommerce application is represented by a corresponding Page Object class, which encapsulates the page's elements and actions. The test cases are organized by functionality, with each test module (e.g., test_login.py) focusing on a specific aspect of the application. The test cases utilize the Page Object classes to interact with the nopCommerce UI and validate the expected behavior. The Base Page class typically encapsulates the common functionality and elements shared across multiple pages of the application.
