# The Web Cookbook App

This Python application utilizes the Streamlit library to create a simple web interface for searching recipes using the Spoonacular API.

## Overview

The application allows users to:

- Search for recipes based on a query, dietary preferences, and intolerances.
- Display a list of recipes based on the search query.
- View ingredients and cooking instructions for a selected recipe.

## Prerequisites

- Python 3.x installed
- Necessary Python packages: `requests`, `streamlit`

## Getting Started

1. Clone or download the repository.
2. Install the required packages by running: `pip install -r requirements.txt`.
3. Run the application using: `streamlit run app.py`.

## Usage

- Run the application and visit the provided URL in the browser.
- Enter a search query for a recipe.
- Select dietary preferences and intolerances.
- Click the "Search" button to display matching recipes.
- Click on "View Ingredients" to see the ingredients and cooking instructions for a specific recipe.

## File Structure

- `app.py`: Contains the main code for the Streamlit application.
- `requirements.txt`: Lists the required Python packages.

## Notes

- The application uses the Spoonacular API to fetch recipe data based on user input.
- Error handling is included to manage potential API request failures.
