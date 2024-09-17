# Chatbot App

A Flask-based web application featuring a chatbot with user authentication and admin functionality.

## Authors

- Rodolfo Lopez
- Andrew Kirraine
- Dalton Kohl
- Julia Paley

## Date

Fall 22 - Spring 23

## Features

- User registration and login
- Admin dashboard
- Chatbot interface
- SQLite database for user management

## Setup

1. Install dependencies:

   ```
   pip install torch numpy nltk flask
   ```

2. Initialize the database:
   The app will automatically create the SQLite database on first run.

3. Run the application:

   ```
   python app.py
   ```

4. Access the app at `http://localhost:5000`

## Usage

- Register as a new user or admin
- Log in to access the chat interface or admin dashboard
- Interact with the chatbot

## File Structure

- `app.py`: Main application file
- `templates/`: HTML templates for the web interface
- `static/`: CSS/js files for the web interface
- `NN/bot.py`: Chatbot logic
- `NN/nltk_funcs.py`: Natural language processing functions
- `NN/train.py`: Training script for the chatbot
- `NN/model.py`: Neural network model definition for the chatbot
- `users.db`: SQLite database for user information
- `model.pth`: Trained model automatically created after training

## Notes

- Admin dashboard not fully set up yet...
