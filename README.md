# Workout Plan Creator
Workout Plan Creator is a Python application that helps fitness enthusiasts create a customized workout plan based on their goals, level of experience, and preferred workout style.

The application uses a SQLite database of exercises to generate a workout plan consisting of various exercises for different muscle groups, along with recommended sets and reps for each exercise. The user can choose between different workout styles, such as free weights, machine-based workouts, or a combination of both. They can also select the number of days per week they want to work out and the level of difficulty.

## Requirements
* Python 3.6 or higher
* SQLite 3
* XlsxWriter

## Installation
Clone this repository or download the ZIP file and extract it to a local folder.
Open a terminal and navigate to the folder where the repository was downloaded.
Create a virtual environment using the following command: python3 -m venv env
Activate the virtual environment: source env/bin/activate (Linux/Mac) or .\env\Scripts\activate (Windows PowerShell)
Install the required Python packages: pip install -r requirements.txt
Run the application: python workout_plan_creator.py

## Usage
Choose your workout style, number of days per week, and level of difficulty on the first page of the application.
Select the muscle groups you want to target on the second page.
Click the "Create Workout Plan" button to generate a workout plan in an Excel spreadsheet.

## Credits
Workout Plan Creator was developed by swifteddy as a personal project. The exercise database used by the application was created personally.
