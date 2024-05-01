# nopCommerce-Automation-Testing-Project


## Project Overview<a id="project-overview"></a>

This Postman-based API testing project allows for efficient and thorough testing of the Jira API, ensuring the reliability and functionality of the Jira platform for the project team and stakeholders.



## Table of Content:

- [About The App](#about-the-app)
- [Tools](#tools)
- [Setup](#setup)
- [Approach](#approach)

## About The App

NopCommerce is an open-source e-commerce platform that provides a comprehensive set of features and functionalities for building and managing online stores. nopCommerce is a robust, feature-rich and customizable open-source e-commerce platform suitable for businesses that need a high degree of control and flexibility over their online store.

## Tools
I used `Jira`, `Postman`,  and `macOS screenshot`,

## Setup
- Install and configure the postman software on your local machine
- Ensure you have access to jira cloud for api documentation and testing
- Generate a Jira API token from your Atlassian account settings.


## Approach

I've set up a new request in Postman using the "Basic Auth" type. For authentication, I entered my Jira email as the username and my API token as the password. Then, I created four GET requests to gather information such as instance info, projects, issue types, and users assignable to projects. After that, I created a POST request to create a new issue and followed that up with a GET request to retrieve issue details. To edit the issue, I used a PUT request, and finally, I deleted the issue using a DELETE request.

**Challenge:** Complexity of Jira API: Jira API has many endpoints and features. Understanding the API documentation and identifying the relevant endpoints for testing can be time-consuming.

**Solution:** Review the Jira REST API documentation thoroughly to understand the available endpoints, their parameters, and the expected responses. Maintain a reference guide for the team.

**Challenge:** Jira projects often involve complex data structures, such as issues, projects, and custom fields, which make dynamic data and test data management challenging. In addition to dealing with dynamic data, maintaining relevant test data is also difficult.

**Solution:** Handle dynamic data and maintain relevant test data using Postman's variables, data files, and scripts. Using Postman's data-driven testing features will enhance the robustness and reusability of your tests.
