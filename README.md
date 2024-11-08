# Assessment Instructions
There are three different tasks for you to complete, all contained within this repository. Two can be found in the `tasks` directory, within the files: `parentheses_matching.py` and `transactions.py`. The other is the Flask webapp ShiftScheduler, instructions for which can be found below. 

Please create a new branch before starting the development of any solutions. When you're ready to submit, open a pull request with your changes.

# ShiftScheduler

## Overview
ShiftScheduler is a flexible code template designed to help businesses efficiently schedule and manage employee shifts. Your task is to build upon this foundation, enhancing its functionality to meet the specific needs outlined below. We encourage you to bring your creativity and unique approach to the project as you expand its capabilities.  To ensure an accurate assessment of your individual coding skills, please refrain from using LLMs such as ChatGPT during the development process.

### Functional Requirements

1. **View All Shifts**  
   - **Route**: `/`  
   - **Method**: `GET`  
   - **Description**: Display a list of all employee shifts with details like employee name, start time, end time, and role.
   - **Note**: This requirement has already been implemented, but was included here to indicate that candidates should ensure it remains functional.

2. **Add a Shift**  
   - **Route**: `/add_shift`  
   - **Method**: `POST`  
   - **Description**: Adds a new shift to the database using form data (employee name, start time, end time, role). Ensure that the shift being added does not clash with an existing shift for the same employee. Redirect to the main page after adding.

3. **Delete a Shift**  
   - **Route**: `/delete_shift`  
   - **Method**: `POST`  
   - **Description**: Deletes a shift from the database using the shift's unique ID. Redirect to the main page after deletion.

4. **Edit a Shift**  
   - **Route**: `/edit_shift`  
   - **Method**: `POST`  
   - **Description**: Edits an existing shift's details (e.g., update start/end times or role). Redirect to the main page after editing.

### Non-Functional Requirements

1. **Database**  
   - Store shifts in the existing database. Each shift should include: `id`, `employee_name`, `start_time`, `end_time`, and `role`.

2. **Form Validation**  
   - Validate form input to ensure required fields are filled out and times are correct (e.g., start time is before end time).

3. **User Interface**  
   - Simple UI to display shifts and manage them (add, edit, delete). Forms should be easy to use and provide basic error messages.


## Setup Instructions

### Step 1: Clone the repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/ArborCarbon/Tech-Assessment.git
cd Tech-Assessment
```

### Step 2: Create a Virtual Environment
It’s highly recommended to create a virtual environment to manage project dependencies:
```bash
python3 -m venv venv
```

### Step 3: Activate the Virtual Environment 
On macOS/Linux:
```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```

### Step 4: Install Required Dependencies
Now, install the necessary Python dependencies specified in requirements.txt:
```bash 
pip install -r requirements.txt
```

### Step 5: Populate the Database with Fake Data
Run the populatedb.py script to add fake entries to the database for testing purposes:
```bash
python populatedb.py
```

### Step 5: Run the Application
```bash 
flask run 
```
