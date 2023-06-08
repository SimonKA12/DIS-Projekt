# Salary predicter. On this side you can check what salary you should get in your future job
# or if you should ask for a raise at your current job

# How to run the Salary predict project:

(1) Run the code below to install the dependencies.
>$ pip install -r requirements.txt

(2) Initialize the database, by running the SQL files (Creating the necessary tables) 
IMPORTANT: In the 'create_salaries_table.SQL' change the directory to the full path of the 'ds_saleries.csv' file. 


(3) Set your own database username and password in the app.py-file

(4) Execute the SQL file using: psql -U your_username -d your_database_name -f create_salaries_table.sql

(5) Run the program:
>$ export FLASK_APP=app.py
If you want to go into debugging mode do:
>$ export FLASK_ENV=development
To turn of debugging use:
>$ export FLASK_ENV=production 
Run the application:
>$ flask run

# Incase that the code isn't running as it should, see proof_of_function.pdf
# where there will be screenshots from the webapplication.

----------------------------------------------------------------------------------------------

# How to use the application:

(1) Start by choosing if you have a job or not 

(2) if you have a job, you can type your job-information into the calculator, 
and then the calculater will tell you if you are paid enough. 

(3) if you don't have a job, you can also type in your information, and then the calculator 
will tell you how much you should expect to earn.


