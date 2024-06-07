# DIS-Project

# Installing packages
Start by running the following command to ensure the required packages are installed:

    pip install -r requirements.txt

# Initializing database
Using pgAdmin4 create a new database called BeatThemAll. Inside the file "load_data.py", replace

    DB_PASS = "postgres_user_password"

with the relevant password for the user that created the database. With this run one of the following commands:

    python load_data.py
    python3 load_data.py

This reads our datasets, creates tables in the database and inserts the read data into those tables. If the script is run succesfully the database is now ready.

# Running the server
When all above is done correctly the server can be started by using the following command:

    flask run

# Interacting with the server
Interaction with the server takes place on a single page. There is a search bar that takes user input. Descriptive text guides the user and explains how to enter a sport into the search bar. Make sure to spell the sport correctly; however, by using a regular expression, the search bar is not case-sensitive. Searching for a sport that is present in our dataset, for example tennis, bowling, fishing and boxing, results in a list of Pokémon that, based on their attributes, an athlete from the given sport could beat. Make sure to hover over the pokemons to check their personal attributes.

Enjoy :)