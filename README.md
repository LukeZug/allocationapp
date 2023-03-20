# Team 24 - Barclays Team-Graduate Allocation App

## The Project
For our third year team project, Barclays tasked us to develop an application that would automate the assignment of graduates to new teams in their graduate rotation programme.
We took this broad requirement and developed it as a Django webapp that takes in data input by an admin and matches graduates to teams based on their expressed preference using a maximum-flow minimum-cost algorithm taken from the NetworkX Python library.

## Installation (Locally)
The project was built using python 3.9 and all the project dependencies can be installed by running `pip install -r requirements.txt` while in the 'django-backend' folder.

NOTE: You must manually run `pip install python-magic-bin` after installing from requirements. This is due to a bug with one of the packages.

To run locally, run the following commands:
`python manage.py makemigrations`
`python manage.py migrate`
`python populate.py`

Also make sure you set `debug=True` within the settings.py file.

## Installation (Server)
Setup on desired web hosting platform -- we used pythonanywhere. Current implementation of the website can be viewed [here](sh24.eu.pythonanywhere.com)

Navigate to the django-backend directory and enter the following commands in the terminal:
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py shell`
  - `from allocationapp.models import CustomUser, Admin`
  - `admin = Admin.objects.create(user=CustomUser.objects.create_user(first_name="admin", email="example@email.com", username="admin", password="1234"))`
      - change email, username and password fields to whatever logins details you wish for the admin account 
  - `admin.save()`
- Deploy on server

## Setting up email server for live use:
- Instructions to configure email server at the bottom of settings.py

## Usage
The general workflow of the app is as following:
- An admin logs in and uploads/enters all the data necessary for the allocation to happen
    - There is the possibility to upload a csv file for Graduates and Teams. After the file is uploaded, the database will be populated with the data extracted from the csvs.
    - Alternatively the admin can enter teams and graduates manually
- All the graduates input in the system will receive an email with an auto-generated password that they can use to login into the webapp. They will be prompted to change the password on their first access
- Graduates will be prompted with all the possible teams that have been input by the admin and they will be able to access information about the teams, which can guide them in expressing their preference. Their preference is expressed in a form of inputting from 0 to 5 thumbs up, which will impact the allocation of graduates to a particular team
- The admin will run the allocation once all the preferences have been received
- Graduates will be able to log back in to check which team they have been assigned to
- Managers can see their managed teams and can add and drop people from their teams manually


## Authors
Alaa Wardeh - 2572872w@student.gla.ac.uk <br>
Daniel Flynn - 2469113f@student.gla.ac.uk <br>
Gianmarco Cornacchia - 2575307c@student.gla.ac.uk <br>
Luke Mullen - 2542408M@student.gla.ac.uk <br>
Yuqi Li - 2512344L@student.gla.ac.uk <br>
Feel free to contact any one of us via email for any questions, comments or concerns.

## License
This project is under the BSD 3-Clause License. Please see the LICENSE file for further information.

## Project status
The project will be worked on until the 17th of March 2023, the code-freeze date for our project. After that, we will hand our project over to our customer and write a dissertation about our project.
