# Minute-Pitches-App
## Author

[Zakiya Adam, https://github.com/bintadam/]

# Description
This  is a flask application that allows users to post a short pitch and also allows other users who have signed up to comment and vote for a pitch. It also allows a user to sign-up to be able to access  the application


## User Story

A user can see the pitches other people have posted.
A user can vote vote on the pitch they liked and give it a downvote or upvote.
A user can signed in for me to leave a comment
A user can receive a welcoming email once I sign up.
A user can view the pitches I have created in my profile page.
A user can comment on the different pitches and leave feedback.
A user can submit a pitch in any category.
A user view the different categories.

## BDD
| Behavior | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, Select between sign-up and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments template with your comment and other comments|





## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/bintadam/Minute-Pitches-App.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd pitch-world
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3 manage.py server
  ```
5. Testing the application
  ```bash
  python3 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.8]
* [Flask]
* [Heroku]


## Known Bugs
*  bugs... still under development

## Contact Information 

If you have any question or contributions, please email me at [zakiyadan12@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2022 **Zakiya ADAM
