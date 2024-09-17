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

2. For nltk, also need to run:

   ```
   python
   >>> import nltk
   >>> nltk.download('punkt')
   >>> nltk.download('stopwords')
   ```

3. Initialize the database:
   The app will automatically create the SQLite database on first run.

4. Run the application:

   ```
   python app.py
   ```

5. Access the app at `http://localhost:5000`

## Usage

- Register as a new user or admin
- Log in to access the chat interface or admin dashboard
- Interact with the chatbot

## File Structure

- `app.py`: Main application file
- `templates/`: HTML files for the web interface
- `static/`: CSS/js files for the web interface
- `NN/bot.py`: Chatbot logic
- `NN/nltk_funcs.py`: Natural language processing functions
- `NN/train.py`: Training script for the chatbot
- `NN/model.py`: Neural network model definition for the chatbot
- `NN/dataset.json`: Training data for chatbot
- `model.pth`: Trained model automatically created after training
- `users.db`: SQLite database for user information

## Notes

- Website is not hosted; it only runs locally
- Admin dashboard is not fully functioning

## License

See the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgements

- NN inspired from [Patrick Loeber's pytorch-chatbot](https://github.com/patrickloeber/pytorch-chatbot.git)
